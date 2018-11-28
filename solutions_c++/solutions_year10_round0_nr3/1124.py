// Theme_Park.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;
int T,R,K,N;
int *answers;
int *group, *nextPos, *count;
int _tmain(int argc, _TCHAR* argv[]) {
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin >> T;
	answers = new int[T+1];
	for(int i = 1; i <= T; i++)		{
		fin>>R>>K>>N;
		group = new int[N];
		nextPos = new int[N];
		count = new int [N];
		memset(count,-1,sizeof(count));
		for(int j = 0; j < N; j++)
			fin >> group[j];
		int start = 0, next = 0, sum = 0;
		while(count[start] < 0)	{
			sum = 0;
			while(1)	{
				sum += group[next];
				
				if(sum > K) {
					sum -= group[next];
					
					break;
				}
				next = (next+1)%N;
				if(next == start)
					break;
			}
			nextPos[start] = next;
			count[start] = sum;
			start = next;
		}
		sum = 0;
		start = 0;
		for(int j = 1; j <= R; j ++)	{
			sum += count[start];
			start = nextPos[start];

		}
		answers[i] = sum;
		delete []group;
		delete []nextPos;
		delete []count;

	}
	for(int i = 1; i <= T; i++)	{
		fout<<"Case #"<<i<<": "<<answers[i]<<endl;
	}
	fout.close();
	system("pause");
	return 0;
}