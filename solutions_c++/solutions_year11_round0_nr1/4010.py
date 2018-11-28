// test.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	//ifstream is("C:\\Users\\Masa\\Downloads\\A-small-practice.in");
	//ofstream os("C:\\Users\\Masa\\Downloads\\A-small-practice.out");
	
	ifstream is("C:\\Users\\Masa\\Downloads\\A-large.in");
	ofstream os("C:\\Users\\Masa\\Downloads\\A-large.out");

	const int ORA = 0;
	const int BLU = 1;
	int  T;
	is >> T;

	for (int icase=0; icase<T; icase++) {
		int N;
		is >> N;

		int pointer = 0;
		int pos[2] = {1,1};
		int next[2] = {0};
		int pointerRobo[2] = {-1,-1};
		bool finished[2] = {false};
		vector<int> dataRobo(N);
		vector<int> dataBtm(N);

		for (int i=0; i<N; i++) {
			char tc;
			is >> tc;
			dataRobo[i] = tc == 'O' ? ORA : BLU;
			is >> dataBtm[i];
		}

		// next point 
		for (int r=0; r<2; r++) {
			bool isFinished = true;
			for (int i=pointerRobo[r]+1; i<N; i++) {
				if (dataRobo[i] == r) {
					pointerRobo[r] = i;
					next[r] = dataBtm[i];
					isFinished = false;
					break;
				}
			}
			if (isFinished) {
				finished[r] = true;
			}
		}

		int t = 0;
		for (;;t++) {
			int finishCounter = 0;
			bool isPressed = false;
			for (int r=0; r<2; r++) {
				if (finished[r]) {
					finishCounter++;
				} else if (pos[r] != next[r]) {
					pos[r] += (pos[r] >  next[r] ? -1:1);
				} else if (pointer == pointerRobo[r] && isPressed == false) {
					// press
					pointer++;

					// next point 
					bool isFinished = true;
					for (int i=pointerRobo[r]+1; i<N; i++) {
						if (dataRobo[i] == r) {
							pointerRobo[r] = i;
							next[r] = dataBtm[i];
							isFinished = false;
							break;
						}
					}
					if (isFinished) {
						finished[r] = true;
					}
					isPressed = true;
				} else {
					// stay
				}
			}
			if (finishCounter == 2) {
				break;
			}
		}
		os << "Case #" << icase+1 << ": " << t;
		os << endl;
		cout << icase << endl;

	}

	cout << "finished";
	getchar();
		
	is.close();
	return 0;
}

/*
22:30 A start
A:30
move
press
stay

23:00 C start
問題理解でleareのアルゴリズムがわからないから後回し

23:16 B start
冒頭理解、A問題はleargeにも対応できるのでこっちにする

23:24 A start
23:47 A programing finished. start dbg
00:05 finished dbg

*/



/* A
	//
	//for (int i=0; i<T;i++) {
	//	int K,N;
	//	is >> N;

	//	int pointer = 0;
	//	int t = 0;
	//	int pos[2] = {1};		
	//	int next[2] = {0};
	//	int pointerRobot[2] = {0};

	//	for (;;t++) {
	//		for (int r=0; r<2; r++) {
	//			if (pos[r] != next[r]) {
	//				pos[r] = (pos[r] >  next[r] ? -1:1);
	//			} else if (pointer == pointerRobot[r]) {
	//				// press
	//			}

	//		}
	//	}

*/