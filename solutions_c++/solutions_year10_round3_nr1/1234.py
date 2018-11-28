#define PATH "/home/tushar/Desktop/"
#define INPUTFILE PATH "A-large.in" 
#define OUTPUTFILE PATH "A-large.out"

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

int A[1000],B[1000],S[1000];

int main()
{
	assert (freopen (INPUTFILE, "r", stdin));
	assert (freopen (OUTPUTFILE, "w", stdout));
	
	int T,N;
	cin>>T;
	for(int k=1;k<=T;++k)
	{
		cin>>N;
		for(int i=0;i<N;++i)
			cin>>A[i]>>B[i],S[i] = B[i]-A[i];
		int count = 0;
		for(int i=0;i<N;++i)
			for(int j=i+1;j<N;++j)
				if(S[i] != S[j] &&  (A[i]<A[j]&&B[i]>B[j]) || (A[i]>A[j]&&B[i]<B[j]))count++;
		cout<<"Case #"<<k<<": "<<count<<endl;
		}
	return 0;
	}
