// googlecode3.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

long long group[1000], total[1000];
int end[1000];

int _tmain(int argc, _TCHAR* argv[])
{
	int T, t = 0;
	long R, K, N;
	long long people, answer;

	ifstream in("in.txt");
	ofstream out("out.txt");

	in >> T;
	while(T){
		++t;
		--T;
		in >> R >> K >> N;
		for(int i = 0; i < N; ++i){
			in >> group[i];
			total[i] = 0;
			end[i] = 0;
		}
		for(int i = 0; i < N; ++i){
			people = 0;
			int j = i;
			while(people + group[j] <= K){
				people += group[j];
				++j;
				if(j >= N)
					j -= N;
				if(j == i)
					break;
			}
			total[i] = people;
			end[i] = j;
		}

		answer = 0;
		for(long i = 0, begin = 0; i < R; ++i){
			answer += total[begin];
			begin = end[begin];
		}
		out << "Case #" << t << ": " << answer << endl;
	}

	return 0;
}

