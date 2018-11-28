// test.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;



const int MAX_BIT = 28;

void toBinary(int val, int* bin) {
	for (int i=0; i<MAX_BIT; i++) {
		bin[i] = val % 2;
		val /= 2;
	}
}

string binToStr(int v) {
	int bin[MAX_BIT];
	toBinary(v, bin);

	string s = "";
	int point = 0;
	for (int i=MAX_BIT-1; i>=0; i--) {
		if (bin[i] != 0) {
			point = i;
			break;
		}
	}
	if (point == 0) {
		if (bin[0] == 1) return "1";
		if (bin[0] == 0) return "0";
	} else {
		for (int i=point; i>=0; i--) {
			if (bin[i] == 1) s.append("1");
			if (bin[i] == 0) s.append("0");
		}
	}
	return s;
}


int toDec(int* v) {
	int std = 1;
	int result = 0;
	for (int i=0; i<MAX_BIT; i++) {
		result += v[i] * std;
		std *= 2;
	}
	return result;
}

void sumNoCarry(int* result, int* v1) {
	for (int i=0; i<MAX_BIT; i++) {
		if (v1[i] != result[i]) {
			result[i] = 1;
		} else {
			result[i] = 0;
		}
	}
}


void test() {
	int bin[MAX_BIT];
	toBinary(512, bin);
	toBinary(1024, bin);
	toBinary(1048576, bin);
	toBinary(1048576*2+1, bin);
}

int power(int n) {
	int v=1;
	for (int i=0; i<n; i++) {
		v *= 2;
	}
	return v;
}

int _tmain(int argc, _TCHAR* argv[])
{
	test();
	//ifstream is("C:\\Users\\Masa\\Downloads\\A-small-practice.in");
	//ofstream os("C:\\Users\\Masa\\Downloads\\A-small-practice.out");
	
	ifstream is("C:\\Users\\Masa\\Downloads\\C-large.in");
	ofstream os("C:\\Users\\Masa\\Downloads\\C-large.out");

	int  T;
	is >> T;

	for (int icase=0; icase<T; icase++) {
		int N;
		int max = 0;
		is >> N;

		int val[1001];
		int bin[1001][MAX_BIT];

		for (int i=0; i<N; i++) {
			is >> val[i];
		}
		for (int i=0; i<N; i++) {
			toBinary(val[i], bin[i]);
		}

		// 分離可能判定
		bool possible = true;
		for (int j=0; j<MAX_BIT; j++) {
			int count = 0;
			for (int i=0; i<N; i++) {
				count += bin[i][j];
			}
			if (count % 2 == 1) {
				possible = false;
				break;
			}
		}

		os << "Case #" << icase+1 << ": ";


		if (possible) { // 欲張りでOK
			// min
			int min = INT_MAX;
			for (int i=0; i<N; i++) {
				if (min > val[i]) min = val[i];
			}

			int sum = -min;
			for (int i=0; i<N; i++) {
				sum += val[i];
			}
			os << sum;
		} else {
			os << "NO";
		}
		os << endl;
		cout << icase << endl;
	}
	
	is.close();
	os.close();
	cout << "finished";
	getchar();
		
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
00:10 A OK

00:24 C start
00:30 C think algorithm
00:35 B 

00:48 C start
00:57 B start
01:03 B start

01:25 B understood
01:35 C Alg understood
02:13 C finished programing
03:12 B programing



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