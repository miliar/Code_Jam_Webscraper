#define PATH "/home/tushar/Desktop/"
#define INPUTFILE PATH "B-large.in" 
#define OUTPUTFILE PATH "B-large.out"

#include <vector>
#include <cassert>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;
int X[50],V[50],res,T;
double t[50];

int main()
{
	assert (freopen (INPUTFILE, "r", stdin));
	assert (freopen (OUTPUTFILE, "w", stdout));
	
	int C,N,K,B,temp;
	
	cin>>C;
	for(int k=1;k<=C;++k)
	{
		cin>>N>>K>>B>>T;
		for(int i=0;i<N;++i)
			cin>>X[i],t[i] = B-X[i];
		for(int i=0;i<N;++i)
			cin>>V[i],t[i] /= V[i];
		int count=0;
		vector <double> A;
		for(int i=N-1;i>=0 && count<K;--i)
		{
			A.push_back(t[i]);
			if(t[i] <= T)count++;
			}
		temp = res = 0;
		memset(X,0,sizeof(X));
		for(int i=0;i<A.size();++i)
		{
			if(A[i]<=T)X[i] = temp;
			else temp++;
			}
		for(int i=0;i<N;++i)res += X[i];
		cout<<"Case #"<<k<<": ";
		((count<K)?cout<<"IMPOSSIBLE":cout<<res)<<endl;
		A.clear();
		}
	return 0;
	}
