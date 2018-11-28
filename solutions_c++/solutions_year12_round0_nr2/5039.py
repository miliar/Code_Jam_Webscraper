//============================================================================
// Name        : DANCING.cpp
// Author      : Loc Ngo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;
ifstream fin("B-small-attempt2.in");
ofstream fout("B-small-attempt2.out");
int Max;

void search(int A[],int index,int k,int N,int S,int s,int p)
{
	if(index == N)
	{
		if(s==S)
			Max = max(Max,k);
		return;
	}

	for(int i1=0;i1<=30;i1++)
		for(int i2=0;i2<=30;i2++)
			for(int i3=0;i3<=30;i3++)
				if(i1+i2+i3==A[index]&&fabs(i1-i2)<=2&&fabs(i1-i3)<=2&&fabs(i2-i3)<=2)
					if(fabs(i1-i2)==2||fabs(i1-i3)==2||fabs(i2-i3)==2)
					{
						if(max(max(i1,i2),i3)>=p)
							search(A,index+1,k+1,N,S,s+1,p);
						else
							search(A,index+1,k,N,S,s+1,p);
					}
					else
					{
						if(max(max(i1,i2),i3)>=p)
							search(A,index+1,k+1,N,S,s,p);
						else
							search(A,index+1,k,N,S,s,p);
					}

}

void process(int T)
{
	int N,S,p;
	int A[100];
	fin>>N>>S>>p;
	for(int i=0;i<N;i++)
		fin>>A[i];
	Max = 0;
	search(A,0,0,N,S,0,p);
	fout<<"Case #"<<T<<": "<<Max<<endl;
}

int main() {
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
		process(i);
	return 0;
}
