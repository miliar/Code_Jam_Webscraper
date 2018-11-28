// program.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#pragma warning(disable:4786)
#include <stdafx.h>
// END CUT HERE
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;

void process(int num)
{
	int N,M,A;
	cin>>N>>M>>A;

	/*for(int i=0;i<=N;i++)
	{
		for(int j=0;j<=M;j++)
		{
			int sum=i*j;
			if(sum>=A)
			{
				int r=sum-A;
				if(r==0)
				{
					cout<<"Case #"<<num<<": 0 0 "<<i<<" 0 0 "<<j<<endl;
					return;
				}
				for(int xx=1;xx<=N;xx++)
				{
					int yy=r/xx;
					if(r==xx*yy&&yy<=M)
					{
						cout<<"Case #"<<num<<": 0 "<<j<<" "<<xx<<" 0 "<<i<<" "<<j-yy<<endl;
						return;
					}
				}

			}
		}
	}
	cout<<"Case #"<<num<<": "<<"IMPOSSIBLE"<<endl;*/

	if(A>N*M)
	{
		cout<<"Case #"<<num<<": "<<"IMPOSSIBLE"<<endl;
		return;
	}
	
	int W=A/M+(A%M!=0),H=M;
	int v=(A%M!=0),h;
	if(A%M==0) h=0; else h=M-(A%M);
	cout<<"Case #"<<num<<": 0 "<<H<<" "<<v<<" 0 "<<W<<" "<<H-h<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}