#include <QFileInfo>
#include <QFile>
#include <QString>
#include "QStringList"
#include <iostream>
#include <QTextStream>
#include <QList>
#include "QVector"
using namespace std;


struct Node {
	Node(int h) {
		height = h;
		verticalObstacle = false;
		horizontalObstacle = false;
	}
	int height;
	bool verticalObstacle;
	bool horizontalObstacle;
};

typedef QList<QList<int> > IntMatrix;
typedef QList<int> IntVector;


int main() {
	QFile smallIn("D:/Working/Merging/GCJ/LawnMower/debug/A-large.in");
	if (!smallIn.open(QIODevice::ReadOnly | QIODevice::Text)) {
		return 1;
	}

	QFile smallOut("D:/Working/Merging/GCJ/LawnMower/debug/A-large-out.txt");
	if ( ! smallOut.open(QIODevice::WriteOnly | QIODevice::Text)) {
		return 1;
	}

	QTextStream in(&smallIn);
	QTextStream out(&smallOut);
	QStringList inputStrList;
	while (!in.atEnd()) {
		QString line = in.readLine();
		inputStrList.push_back(line);
	}

	int currentLineNo = 0;
	int t = inputStrList.at(currentLineNo).toInt();
	currentLineNo++;

	for(int testCaseNo = 0; testCaseNo < t; testCaseNo++) {
		IntMatrix pattern;
		IntVector hSumVector, vSumVector;
		int d1 = 0, d2 = 0;
		
		bool isFinished = true;
		for (int rowNo = 0; rowNo < 4; rowNo++ ) {
			IntVector newRow;
			pattern.push_back(newRow);
			QString rowStr;
			while(rowStr.isEmpty() && currentLineNo < inputStrList.size() ) {
				rowStr = inputStrList.at(currentLineNo++);
			}
			for(int colNo = 0; colNo < 4; colNo++) {
				QString val = rowStr.at(colNo);
				int v;
				if ( val == "O" ) {
					pattern[rowNo].push_back(1);
					v = 1;
				} else if ( val == "X" ) {
					pattern[rowNo].push_back(-1);
					v = -1;
				} else if ( val == "T" ){
					pattern[rowNo].push_back(0);
					v = 0;
				} else if ( val == "." ){
					pattern[rowNo].push_back(10);
					v = 10;
					isFinished = false;
				} 
				if ( rowNo == 0 ) {
					vSumVector.push_back(0);
				} 
				if ( colNo == 0 ) {
					hSumVector.push_back(0);
				}
				vSumVector[colNo] += v;
				hSumVector[rowNo] += v;

				if ( rowNo == colNo ) {
					d1 += v;
				}
				if ( rowNo == 3 - colNo ) {
					d2 += v;
				}
			}
		}
		bool isOWin = false, isXWin = false;
		for(int i = 0; i < 4; i++ ) {
			if ( vSumVector.at(i) < 5 ) {
				if ( vSumVector.at(i) >= 3 ) {
					isOWin = true;
					break;
				} else if ( vSumVector.at(i) <= -3 ) {
					isXWin = true;
					break;
				}
			}
			if ( hSumVector.at(i) < 5 ) {
				if ( hSumVector.at(i) >= 3 ) {
					isOWin = true;
					break;
				} else if ( hSumVector.at(i) <= -3 ) {
					isXWin = true;
					break;
				}
			}
		}

		if ( ! isOWin && ! isXWin ) {
			if ( d1 < 5 ) {
				if ( d1 >= 3 ) {
					isOWin = true;
				} else if ( d1 <= -3 ) {
					isXWin = true;
				}
			}

			if ( d2 < 5 ) {
				if ( d2 >= 3 ) {
					isOWin = true;
				} else if ( d2 <= -3 ) {
					isXWin = true;
				}
			}
		}

		if ( isOWin ) {
			out << "Case #" << testCaseNo+1 << ": O won\n";
		} else if ( isXWin ) {
			out << "Case #" << testCaseNo+1 << ": X won\n";
		} else if ( isFinished ) {
			out << "Case #" << testCaseNo+1 << ": Draw\n";
		} else {
			out << "Case #" << testCaseNo+1 << ": Game has not completed\n";
		}
	}


	return 0;
}