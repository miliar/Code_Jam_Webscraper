//============================================================================
// Name        : codeJam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

void searchNextTaskO();
void searchNextTaskB();

FILE *fp;
FILE *fout;

int tc, buttons, i, j, k;
char R;
int P;
int result;

vector <pair<char,int> > tasks;
int seconds = 0;
int indexO, indexB;
bool nFoundIO, nFoundIB;
int stateO, stateB;
int objO, objB;
int posO, posB;

int main() {

	// >> Opening file
	fp = fopen("A-large.in", "r");
	fout = fopen("out.txt", "w");
	// >> Reading file
	fscanf(fp, "%d", &tc);
	for (k = 0; k < tc; k++) {
		tasks.erase(tasks.begin(), tasks.end());
		fscanf(fp, "%d", &buttons);
		for (j = 0; j < buttons; j++) {
			fscanf(fp, " %c", &R);
			fscanf(fp, " %d", &P);
			if (R == 'O')
				tasks.push_back(pair<char,int>(R, P));
			else if (R == 'B')
				tasks.push_back(pair<char,int>(R, P));
		}

		indexO = indexB = 0;
		nFoundIO = nFoundIB = true;
		posO = posB = 1;
		seconds = 0;

		do {
			// >> to find nextTaskEachRobot
			do {
				if (nFoundIO)
					searchNextTaskO();
				if (nFoundIB)
					searchNextTaskB();
			}while(nFoundIO || nFoundIB);

			if (indexO < buttons)
				objO = tasks[indexO].second;
			if (indexB < buttons)
				objB = tasks[indexB].second;

			// >> First orange
			if (indexO < indexB) {
				// >> Moving
				if (abs(posO - objO) > 0) {
					seconds++;
					if (posO > objO)
						posO--;
					else
						posO++;
				}
				// >> Pushing button
				else {
					seconds++;
					nFoundIO = true;
					indexO++;
				}
				// >> Moving
				if (abs(posB - objB) > 0) {
					if (posB > objB)
						posB--;
					else
						posB++;
				}
				// >> Stand-by
				else {}
			}

			// >> First blue
			if (indexO > indexB) {
				// >> Moving
				if (abs(posB - objB) > 0) {
					seconds++;
					if (posB > objB)
						posB--;
					else
						posB++;
				}
				// >> Pushing button
				else {
					seconds++;
					nFoundIB = true;
					indexB++;
				}
				// >> Moving
				if (abs(posO - objO) > 0) {
					if (posO > objO)
						posO--;
					else
						posO++;
				}
				// >> Stand-by
				else {}
			}
		}while(indexO < buttons || indexB < buttons);

		result = seconds;

		fprintf(fout, "Case #%d: %d\n", k+1, seconds);
	}

	cout << "Fin" << endl;

	return 0;
}

void searchNextTaskO() {

	for (i = indexO; i < buttons; i++) {
		if (tasks[i].first == 'O') {
			indexO = i;
			nFoundIO = false;
			return;
		}
	}
	indexO = buttons;
	nFoundIO = false;
}

void searchNextTaskB() {

	for (i = indexB; i < buttons; i++) {
		if (tasks[i].first == 'B') {
			indexB = i;
			nFoundIB = false;
			return;
		}
	}
	indexB = buttons;
	nFoundIB = false;
}
