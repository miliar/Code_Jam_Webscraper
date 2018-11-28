#include      <iostream>
#include      <fstream>

const int MAX = 101;

enum WantsTo {
	PUSH
	, MOVE
	, MOVE_BACK
	, STAY
};

void findNextPos(int &nCurPos, char ch, std::pair<char, int> aTasks[], int nTasks) {
	for (int i = nCurPos; i < nTasks; ++i) {
		if (aTasks[i].first == ch) {
			nCurPos = i;
			return;
		}
	}

	nCurPos = MAX;
}

int main(int argc, char **argv) {
	int nTests;
	int nTasks;
	int i;
	int nOTaskPos, nBTaskPos, nOPos, nBPos;
	WantsTo BWantsTo, OWantsTo;
	int nMoves;

	std::pair<char, int> aTasks[100];

	std::ifstream in("in");
	std::ofstream out("out");
	in >> nTests;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		in >> nTasks;

		for (i = 0; i < nTasks; ++i) {
			in >> aTasks[i].first >> aTasks[i].second;
		}


		nOTaskPos = 0;
		nBTaskPos = 0;
		nOPos     = 1;
		nBPos     = 1;
		BWantsTo  = MOVE;
		OWantsTo  = MOVE;
		nMoves    = 0;

		findNextPos(nBTaskPos, 'B', aTasks, nTasks);
		findNextPos(nOTaskPos, 'O', aTasks, nTasks);

		while (true) {
			if (nOTaskPos >= MAX) {
				OWantsTo = STAY;
			}

			if (nBTaskPos >= MAX) {
				BWantsTo = STAY;
			}

			if (OWantsTo == STAY && BWantsTo == STAY) {
				break;
			}

			++nMoves;

			if (OWantsTo != STAY) {
				if (nOPos < aTasks[nOTaskPos].second) {
					OWantsTo = MOVE;
				} else if (nOPos == aTasks[nOTaskPos].second) {
					OWantsTo = PUSH;
				} else {
					OWantsTo = MOVE_BACK;
				}
			}

			if (BWantsTo != STAY) {
				if (nBPos < aTasks[nBTaskPos].second) {
					BWantsTo = MOVE;
				} else if (nBPos == aTasks[nBTaskPos].second) {
					BWantsTo = PUSH;
				} else {
					BWantsTo = MOVE_BACK;
				}
			}

			if (BWantsTo == PUSH && OWantsTo == PUSH) {
				if (nBTaskPos < nOTaskPos) {
					//std::cout << "B push: " << nBPos << std::endl;
					//std::cout << "O stay: " << nOPos << std::endl;

					++nBTaskPos;
					findNextPos(nBTaskPos, 'B', aTasks, nTasks);
				} else if (nOTaskPos < nBTaskPos) {
					//std::cout << "O push: " << nOPos << std::endl;
					//std::cout << "B stay: " << nBPos << std::endl;

					++nOTaskPos;
					findNextPos(nOTaskPos, 'O', aTasks, nTasks);
				}
			} else {
				if (BWantsTo == PUSH) {
					if (nBTaskPos < nOTaskPos) {
						//std::cout << "B push: " << nBPos << std::endl;
						++nBTaskPos;
						findNextPos(nBTaskPos, 'B', aTasks, nTasks);
					} else {
						//std::cout << "B must stay: " << nBPos << std::endl;
					}
				}else if (BWantsTo == MOVE) {
					++nBPos;
					//std::cout << "B move to: " << nBPos << std::endl;
				}else if (BWantsTo == MOVE_BACK) {
					--nBPos;
					//std::cout << "B move to: " << nBPos << std::endl;
				}

				if (OWantsTo == PUSH) {
					if (nOTaskPos < nBTaskPos) {
						//std::cout << "O push: " << nOPos << std::endl;
						++nOTaskPos;
						findNextPos(nOTaskPos, 'O', aTasks, nTasks);
					} else {
						//std::cout << "O must stay: " << nOPos << std::endl;
					}
				}else if (OWantsTo == MOVE) {
					++nOPos;
					//std::cout << "O move to: " << nOPos << std::endl;
				}else if (OWantsTo == MOVE_BACK) {
					--nOPos;
					//std::cout << "O move to: " << nOPos << std::endl;
				}
			}
		}

		out << "Case #" << nTest << ": " << nMoves << std::endl;
	}

	in.close();
	out.close();

	return 0;
}
