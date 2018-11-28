

#include <stdio.h>
#include <iostream>
#include "uni.hxx"
#include <math.h>
#include <vector>
#include <map>

using namespace std;
#define TESTCASE 0
#define BEGIN 1
#define TESTCASE_WORD_COUNT 3
#define TESTCASE_ENGINE_LIST 2
#define TEST_WORD_LIST 5

bool readfile(const char *filename);

int main(int argc, char **argv) {
	if(argc!=2) {
		cerr << "Usage " << argv[0] << " <filename>" << endl;
		return -1;
	}

	char *filename = argv[1];
	bool status = readfile(filename);
	if(!status) { return -1;}

}


//=======================

bool readfile(const char *filename) {
	FILE *fp = fopen(filename, "r");
	if(!fp) {
		cerr << "Could not open input file" << endl;
		return false;
	}

	char c;
	uniTestCase *currentCase =0;
	int engineCount_ =0;
	long curState = BEGIN;
	char currentString[512];
	long i =0;
	int wordCount_ =0;
	long j =0;
	long totalTestCaseCount_ =0;
	int N_ =0;
	long caseNumber =0;
	while((c=fgetc(fp))!=EOF) {

		switch(curState) {
			case BEGIN :
				{
					if(c==' ' || c=='\t') { continue; }
					if(c=='\n') {
						currentString[i] = '\0';
						i =0;
						N_ = atoi(currentString);
						curState = TESTCASE;
					} else {
						if(c>='0' && c<='9') {
							currentString[i++] = c;
						} else {
							cerr << "First line has a non-number" << endl;
							return false;
						}
					}
					break;
				}
			case TESTCASE :
				{
					if(totalTestCaseCount_>N_) {
						break;
					}
					if(c==' ' || c=='\t') { continue; }
					if(c=='\n') {
						currentString[i] = '\0';
						i =0;
						j =0;
						engineCount_ = atoi(currentString);
						if(currentCase) {
							int answer = currentCase->execute();
							cout << "Case #" << totalTestCaseCount_ << ": " << answer << endl;
							delete currentCase;
						}
						totalTestCaseCount_++;
						currentCase = new uniTestCase(engineCount_);
						curState = TESTCASE_ENGINE_LIST;
					} else {
						if(c>='0' && c<='9') {
							currentString[i++] = c;
						} else {
							cerr << "First line has a non-number" << endl;
							return false;
						}
					}
					break;
				}
			case TESTCASE_ENGINE_LIST:
				{
					if(c=='\n') {
						if(i !=0) {
							currentString[i] = '\0';
							i =0;
							j++;
							currentCase->addEngine(strdup(currentString));
							if(j==engineCount_) {
								engineCount_ =0;
								curState = TESTCASE_WORD_COUNT;
								j=0;
							}
						}
					} else {
						currentString[i++] = c;
					}
					break;
				}
			case TESTCASE_WORD_COUNT:
				{
					if(c==' ' || c=='\t') { continue; }
					if(c=='\n') {
						currentString[i] = '\0';
						i =0;
						wordCount_ = atoi(currentString);
						currentCase->wordCount_ = wordCount_;
						j =0;
						if(wordCount_==0) {
							curState = TESTCASE;
						}
						else {
							curState = TEST_WORD_LIST;
						}
					} else {
						if(c>='0' && c<='9') {
							currentString[i++] = c;
						} else {
							cerr << "First line has a non-number" << endl;
							return false;
						}
					}
					break;
				}
			case TEST_WORD_LIST :
				{
					if(c=='\n') {
						currentString[i] = '\0';
						currentCase->addWord(strdup(currentString));
						i =0;
						j++;
						if(j==wordCount_) {
							wordCount_ =0;
							curState = TESTCASE;
						}
					} else {
						currentString[i++] = c;
					}
					break;
				}
			default :
					break;
		}
	}
	if(currentCase) {
		int answer = currentCase->execute();
		cout << "Case #" << totalTestCaseCount_ << ": " << answer << endl;
	}
	return true;
}

//========================

uniTestCase::uniTestCase(int engineCount) {
	engineCount_ = engineCount;
}

uniTestCase::~uniTestCase() {
}

void uniTestCase::addEngine(const char *engineName) {
	engineList_.push_back(engineName);
}

void uniTestCase::addWord(const char *word) {
	wordList_.push_back(word);
}

void uniTestCase::dump() {
	cout << engineCount_ << endl;
	vector<string>::const_iterator iter = engineList_.begin() ;
    for(int i = 1 ; iter!= engineList_.end(); i++, iter++)
    {
		string item = *iter;
		cout << item << endl;
	}

	cout << wordCount_ << endl;
	vector<string>::const_iterator iter1 = wordList_.begin() ;
    for(int i = 1 ; iter1!= wordList_.end(); i++, iter1++)
    {
		string item = *iter1;
		cout << item << endl;
	}

}


int uniTestCase::execute() {

	map <string, bool> curMap =	getPositionMap();

	int switchCount =0;
	int engC = engineCount_;


	vector<string>::const_iterator iter = wordList_.begin() ;
    for(int i = 1 ; iter!= wordList_.end(); i++, iter++)
    {
		string item = *iter;
		if(!curMap[item]) {
			curMap[item] = true;
			engC--;
			if(engC==0) {
				switchCount++;
				curMap = getPositionMap();
				curMap[item] = true;
				engC = engineCount_;
				engC--;
			}
		}
	}

	return switchCount;	
}

map<string, bool> uniTestCase::getPositionMap() {
	map<string, bool> returnVector;
	vector<string>::const_iterator iter1 = engineList_.begin() ;
    for(int i = 1 ; iter1!= engineList_.end(); i++, iter1++)
    {
		string item = *iter1;
		returnVector[item] = false;
	}
	return returnVector;
}
		
