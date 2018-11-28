// CodeJam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
#include <math.h>
using namespace std;

int cx1, cy1, cx2, cy2;

bool Permute(int M, int N, int A)
{
	int res;
	for (int x=M; x>0; x--)
	{
		for (int y=N; y>0; y--)
		{
			res = x*y - A;
			if(res<0)
				return false;

			for (int i=1; i<=N; i++)
			{
				if(res%i==0 && res/i<=M)
				{
					cx1 = x;	cy1 = i;
					cy2 = y;    cx2 = res/i;
					return true;
				}
			}
		}
	}
	return false;
}

int main(int argc, char* argv[])
{
	ifstream in("input.in");
	ofstream out("output.out");
	int CaseNum;
	int M, N, A;
	string line;
	int i=0;
	
	getline(in, line);
	CaseNum = atoi(line.c_str());
	while (i<CaseNum)
	{
		i++;
		in>>M>>N>>A;
		if(Permute(M, N, A))
		{
			out<<"Case #"<<i<<": "<<0<<" "<<0<<" "<<cx1<<" "<<cy1<<" "<<cx2<<" "<<cy2<<" "<<endl;
			cout<<i<<endl;
		}
		else
			out<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		
	}
	in.close();
	out.close();	
}

