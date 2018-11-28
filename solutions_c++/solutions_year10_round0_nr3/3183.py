#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main()
	{
ifstream inf("C-small.in");
ofstream ouf("C-small.out");
int T;
inf >> T;
for(int i=0;i<T;i++)
	{
	int R,k,N;
		inf >> R >> k >> N;
		int* q = new int[N];
		for(int j=0;j<N;j++) inf >> q[j];
		int point=0;
		long long sum=0;	
		while(R)
			{
			long long tmpsum=0;
			int zac=point;
			while(tmpsum+q[point]<=k&&(point!=zac||!tmpsum))
				{
				tmpsum+=q[point];
				sum+=q[point];
				if(point==N-1) point=0;	else point++;
				}
			R--;
			}
		ouf << "Case #" << i+1 << ": " << sum << endl;
		}
	}