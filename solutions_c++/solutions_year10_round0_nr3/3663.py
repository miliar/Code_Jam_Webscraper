/* 
 * File:   main.cpp
 * Author: enmand
 *
 * Created on May 8, 2010, 7:27 PM
 */
#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

/*
 *
 */
int main()
{
	long T;
	long R = 0, k = 0, N = 0;
	ifstream input;
	long E = 0;
	input.open("input1");
	input >> T; // First line - Test Cases T
	for(long i = 0; i < T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		queue<long> Q;
		input >> R; input >> k; input >> N;
		long onCoaster = 0;
		long* g = new long[N];
		for(long j = 0; j < N; j++)
		{
			input >> g[j];
			Q.push(g[j]);
		}
		for(long m = 0; m < R; m++)
		{
			for(long n = 0; n < N; n++)
			{
				long group = Q.front();
				if(onCoaster + group <= k)
				{
					onCoaster += group;
					E += group;
					Q.pop();
					Q.push(group);
				}
			}
			onCoaster = 0;
		}
		cout << E << endl;
		E = 0;
	}

}