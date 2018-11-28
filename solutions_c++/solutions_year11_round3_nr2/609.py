#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <list>
#include <bitset>
#include <complex>
#include <list>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
int TS,L,N,C;
unsigned long long t;
unsigned long long alllong;
unsigned long long res;
int dis[1500];
int todis[1500];
int a[1500];
vector<int> filter;
bool mycmp(int a,int b){
	return a>b;
}

/*
 The first line of the input gives the number of test cases, T. 
 T lines follow. Each contains integers, L, t, N and C, followed by C 
 integers ai, all separated by spaces. ai is the number of parsecs between 
 star k*C+i and star k*C+i+1, for all integer values of k. 
 */

int main(){
	cin>>TS;
	for (int testId=1; testId<=TS; ++testId) {
		res=0;
		cin>>L>>t>>N>>C;
		for (int i=0; i<C; ++i) {
			cin>>a[i];
			for (int j=i; j<=N; j+=C) {
				dis[j]=a[i];
			}
		}
		alllong=0;
		for (int i=0; i<N; ++i) {
			alllong+=dis[i];
			todis[i+1]=alllong;
		}
		if (t>=alllong*2) {
			res=alllong*2;
		}else {
			if(L==0){
				res=alllong*2;
			}else if (L==1) {
				int tdis=t/2;
				int index=0;
				int best=0;
				while (todis[index]<tdis && index< N) {
					++index;
				}
				best=max(todis[index]-tdis,best);
				for (; index<N; ++index) {
					best=max(best,dis[index]);
				}
				res=alllong*2-best;
			}else {
				filter.clear();
				int tdis=t/2;
				int index=0;
				int best=0;
				while (todis[index]<tdis && index< N) {
					++index;
				}
				filter.push_back(todis[index]-tdis);
				for (; index<N; ++index) {
					filter.push_back(dis[index]);
				}
				sort(filter.begin(),filter.end(),mycmp);
				for (int i=0; i<2 && i<filter.size(); ++i) {
					best+=filter[i];
				}
				res=alllong*2-best;
			}

		}
		cout << "Case #"<<testId<<": "<<res<<endl;

	}
	return 0;
}
