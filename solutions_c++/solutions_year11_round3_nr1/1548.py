/*
 * a.cpp
 *
 *  Created on: May 22, 2011
 *      Author: greenvirag
 */

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <list>

using namespace std;

typedef long long int llint;

#define RMAX 50
#define CMAX 50


void run(int testcase)
{
	register int i,j;
	int R, C;
	scanf("%d", &R);
	scanf("%d", &C);

//	cout << "R: " << R << ", C: " << C << endl;

	char maze[RMAX][CMAX];
	memset(maze,0,RMAX*CMAX);

	int Bcount = 0;

	for(i=0; i<R; i++) {
		scanf("\n");
		fread(maze[i],1,C, stdin);
//		cout << maze[i] << endl;
		for(j=0; j<C; j++) {
			if(maze[i][j]=='#') { Bcount++; }
		}
	}

//	cout << "Bcount: " << Bcount << endl;

	bool oke = true;
	if (Bcount==0) {
		cout << "Case #" << testcase << ": " << endl;
		for(i=0; i<R; i++) {
			cout << maze[i] << endl;
		}
		return;
	}

	if (Bcount%4 != 0) {
		cout << "Case #" << testcase << ": " << endl;
		cout << "Impossible\n";
		return;
	}

	for(i=0; i<R; i++) {
		for(j=0; j<C; j++) {
			if(maze[i][j]=='#') {
				// check degree
				int d = 0;
				bool neigh[] = {false,false,false,false};

				int x, y;

				{
					x=i;
					y=j-1;
					if (y >= 0 && y < C) {
						if (maze[x][y] == '#') {
							d++;
							neigh[0]=true;
						}
					}
				}
				{
					x=i;
					y=j+1;
					if (y >= 0 && y < C) {
						if (maze[x][y] == '#') {
							d++;
							neigh[1]=true;
						}
					}
				}
				{
					x=i-1;
					y=j;
					if (x >= 0 && x < R) {
						if (maze[x][y] == '#') {
							d++;
							neigh[2]=true;
						}
					}
				}
				{
					x=i+1;
					y=j;
					if (x >= 0 && x < R) {
						if (maze[x][y] == '#') {
							d++;
							neigh[3]=true;
						}
					}
				}


				if (d==0 || d==1) {
					cout << "Case #" << testcase << ": " << endl;
					cout << "Impossible\n";
					return;
				}

				if ( (d==2) && ( (neigh[0] && neigh[1]) ||
						 (neigh[2] && neigh[3])  ) ) {
					cout << "Case #" << testcase << ": " << endl;
					cout << "Impossible\n";
					return;
				}

				if ( d==2 ) {
					if (neigh[1] && neigh[3]) {
						if (maze[i+1][j+1] == '#') {
							maze[i][j] = '/';
							maze[i][j+1] = '\\';
							maze[i+1][j] = '\\';
							maze[i+1][j+1] = '/';
						}
					}
				}
			}
		}
	}


	for(i=0; i<R; i++) {
		for(j=0; j<C; j++) {
			if (maze[i][j] == '#') {
				oke = false;
			}
		}
	}

	if (oke == false) {
		cout << "Case #" << testcase << ": " << endl;
		cout << "Impossible\n";
		return;
	}

	cout << "Case #" << testcase << ": " << endl;
	for(i=0; i<R; i++) {
		for(j=0; j<C; j++) {
			cout << maze[i][j];
		}
		cout << endl;
	}
	return;
}


int main()
{
	int i=1, testcase;
	scanf("%d", &testcase);
	for (; i<=testcase; i++) {
		run(i);
	}

//	cout << "Bye.\n";
	return 0;
}
