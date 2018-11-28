#include <stdio.h>
#include <iostream>
#include <list>
#include <vector>
using namespace std;

#ifndef NULL
#define NULL 0x00000000
#endif

#ifdef WIN32
#pragma warning(disable:4996)
#pragma warning(disable:4258)
#endif

#undef _DEBUG
#ifdef _DEBUG

enum StepState {
	Wait,
	Move,
	Press
};

struct StepData {
	int time;
	StepState curStates[2];
	int index[2];
};

#endif

struct TestSequence {
	char robotColor;
	int buttonPos;

	inline TestSequence(void) : robotColor(0), buttonPos(1) {
	}

	inline TestSequence(const TestSequence &seq) : robotColor(seq.robotColor), buttonPos(seq.buttonPos) {
	}
};

struct Location {
	int location;
	int seqIdx;

	inline Location(void) : location(0), seqIdx(0) {
	}

	inline Location(const Location &loc) : 
		location(loc.location),
		seqIdx(loc.seqIdx) {
	}
};

struct Robot {
	list<Location> locations;
	char type;
	int curLoc;

	inline Robot(void) : curLoc(1) {
	}

	inline Robot(const Robot &robot) :
		locations(robot.locations),
		type(robot.type),
		curLoc(robot.curLoc) {
	}
};

struct TestCase {
	list<TestSequence> sequences;
	Robot robotO;
	Robot robotB;

	inline TestCase(void) {
		robotO.type = 'O';
		robotB.type = 'B';
	}

	inline TestCase(const TestCase &test) :
		sequences(test.sequences) ,
		robotO(test.robotO),
		robotB(test.robotB) {
	}
};

struct Input {
	list<TestCase> testCases;

	inline Input(void) {
	}

	inline Input(const Input &inputs) :
		testCases(inputs.testCases) {
	}
};

struct Case {
	int caseNum;
	int seconds;

	inline Case(int caseN = 0, int sec = 0) :
		caseNum(caseN), seconds(sec) {
	}

	inline Case(const Case &c) :
		caseNum(c.caseNum), seconds(c.seconds) {
	}
};

struct Output {
	int numTestCases;
	Case *cases;

	inline Output(int numTest) : 
		numTestCases(numTest) {
		
		cases = new Case[numTestCases];
	}

	inline ~Output(void) {
		if(cases != NULL) {
			delete [] cases;
			cases = NULL;
		}
	}
};

int main(int argc, const char *argv[]) {

	const int time = 100;

	char characters[] = "OB";
	char numbers[] = "0123456789";

	int readingState = 0;
	FILE *pInputfile = NULL;
	FILE *pOutputfile = NULL;

	Input *inputData = NULL;
	Output *outputData = NULL;

	if(argc >= 2) {
		pInputfile = fopen(argv[1], "r");
	} else {
		pInputfile = fopen("Sample.in", "r");
	}
	
	// First read problem
	int numTestCases = 0;
	if(pInputfile != NULL) {
		while(!feof(pInputfile)) {
			char buffer[1024];

			if(readingState == 0) {
				fgets(buffer, 1024, pInputfile);
				sscanf(buffer, "%d", &numTestCases);

				// Set number of test cases here
				inputData = new Input;
				outputData = new Output(numTestCases);

				readingState++;
			} else if(readingState == 1) {
				int numSeq = 0;

				for(int i = 0; i < numTestCases; i++) {
					
					TestCase testCase;
					char charType;
					int charLoc;

					fgets(buffer, 1024, pInputfile);
					sscanf(buffer, "%d ", &numSeq);

					char *charBuf = buffer;

					int offset = 0;
					for(int j = 0; j < numSeq; j++) {
						int location = strcspn(charBuf, characters);
						sscanf(charBuf + location, "%c %d", &charType, &charLoc);
						
						TestSequence sequence;
						sequence.buttonPos = charLoc;
						sequence.robotColor = charType;
						testCase.sequences.push_back(sequence);

						if(charType == 'O') { 
							Location loc;
							loc.location = charLoc;
							loc.seqIdx = j;
							testCase.robotO.locations.push_back(loc);
						} else if(charType == 'B') {
							Location loc;
							loc.location = charLoc;
							loc.seqIdx = j;
							testCase.robotB.locations.push_back(loc);
						}

						charBuf = strpbrk(charBuf + location + 1, characters);
					}
					
					inputData->testCases.push_back(testCase);
				}

				break;
			}
		}

	} else {
		return 0;
	}

	// Solve the problem
	int i = 0;

	int numtTestCases = inputData->testCases.size();
	
#ifdef _DEBUG	
	FILE *debugging = fopen("Debug.txt", "w");
#endif

	int itidx = 0;
	for(list<TestCase>::iterator itest = inputData->testCases.begin(); itest != inputData->testCases.end(); itest++) {
		TestCase *curCase = &(*itest);
		Robot *robotB = &curCase->robotB;
		Robot *robotO = &curCase->robotO;
		list<TestSequence> *sequence = &curCase->sequences;

#ifdef _DEBUG	
		vector<StepData> steps;
#endif

		while( !sequence->empty() ) {
			
#ifdef _DEBUG	
			StepData data;
			data.time = i + 1;
#endif

			/*
				Wait,
				Move,
				Press
			*/

			bool pressed = false;

			if(!robotB->locations.empty()) {
				if(robotB->curLoc < robotB->locations.front().location) {
					robotB->curLoc++;
#ifdef _DEBUG	
					data.curStates[0] = Move;
					data.index[0] = robotB->curLoc;
#endif
				} else if(robotB->curLoc > robotB->locations.front().location) {
					robotB->curLoc--;
#ifdef _DEBUG	
					data.curStates[0] = Move;
					data.index[0] = robotB->curLoc;
#endif
				} else {
					if(sequence->front().robotColor == 'B' && (robotB->curLoc == sequence->front().buttonPos)) {
						
#ifdef _DEBUG
						data.curStates[0] = Press;
						data.index[0] = robotB->curLoc;
#endif

						sequence->pop_front();
						robotB->locations.pop_front();
						pressed = true;
					} else {
						
#ifdef _DEBUG
						data.curStates[0] = Wait;
						data.index[0] = robotB->curLoc;
#endif
					}
				}
			}
			
			if(!robotO->locations.empty()) {
				if(robotO->curLoc < robotO->locations.front().location) {
					robotO->curLoc++;
#ifdef _DEBUG	
					data.curStates[1] = Move;
					data.index[1] = robotO->curLoc;
#endif
				} else if(robotO->curLoc > robotO->locations.front().location) {
					robotO->curLoc--;
#ifdef _DEBUG	
					data.curStates[1] = Move;
					data.index[1] = robotO->curLoc;
#endif
				} else {
					if(sequence->front().robotColor == 'O' && !pressed && (robotO->curLoc == sequence->front().buttonPos)) {

#ifdef _DEBUG
						data.curStates[1] = Press;
						data.index[1] = robotO->curLoc;
#endif

						sequence->pop_front();
						robotO->locations.pop_front();
					}
				}
			}
			
#ifdef _DEBUG
			steps.push_back(data);
#endif

			i++;
		}
#ifdef _DEBUG

		int stepCount = 1;
		fprintf(debugging, "Time                 |          O          |          B          |\n");
		fprintf(debugging, "------------------------------------------------------------------\n");

		for(vector<StepData>::iterator i = steps.begin(); i != steps.end(); i++) {

			char OBuffer[255];
			char BBuffer[255];

			if(i->curStates[0] == Move) {
				sprintf(OBuffer, "Moving to %d", i->index[0]);
			} else if(i->curStates[0] == Wait) {
				sprintf(OBuffer, "Waiting at %d", i->index[0]);
			} else {
				sprintf(OBuffer, "Press at %d", i->index[0]);
			}
			
			if(i->curStates[1] == Move) {
				sprintf(BBuffer, "Moving to %d", i->index[1]);
			} else if(i->curStates[1] == Wait) {
				sprintf(BBuffer, "Waiting at %d", i->index[1]);
			} else {
				sprintf(BBuffer, "Press at %d", i->index[1]);
			}

			fprintf(debugging, "%d                 |  %s  |  %s  |\n", stepCount, OBuffer, BBuffer);
			stepCount++;
		}

		fclose(debugging);
#endif

		outputData->cases[itidx].caseNum = itidx + 1;
		outputData->cases[itidx].seconds = i;
		itidx++;
		i = 0;
	}

	// Output the solution
	if(argc >= 3) {
		pOutputfile = fopen(argv[2], "w");
	} else {
		pOutputfile = fopen("Sample.out", "w");

		if(outputData != NULL) {
			for(int i = 0; i < outputData->numTestCases; i++) {
				fprintf(pOutputfile, "Case #%d: %d\n", outputData->cases[i].caseNum, outputData->cases[i].seconds);
			}
		}
	}

	// Cleanup
	if(inputData != NULL) {
		delete inputData;
		inputData = NULL;
	}

	if(outputData != NULL) {
		delete outputData;
		outputData = NULL;
	}

	if(pInputfile)
		fclose(pInputfile);

	if(pOutputfile)
		fclose(pOutputfile);

	return 0;
}
