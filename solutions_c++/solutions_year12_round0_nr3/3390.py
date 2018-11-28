// develo.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <utility>
#include <queue>
#include <iostream>
#include <sstream>
#include <map>
#include <ctype.h>
#include <set>

#define LL long long
#define fr(i,n) for(i=0;i<n;i++)
#define INF (2000000000)
#define FOR(n) for(int i = 0;i < n;i++)
#define CLEAR(x) memset(x,0,sizeof(x))
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back((a))

using namespace std;

set<int>* g = new set<int>[3001];

int size,tmp,a,b;

int poww[8] = {0,1,10,100,1000,10000,100000,1000000};

inline void find(int x){
	//cout << x << endl;
	size=0;
	tmp=x;
	while(tmp>0){
		size++;
		tmp/=10;
	}
	int tp=x;
	for (int  i = 1;i < size;i++){
		tp = (tp-tp%10)/10+(tp%10)*poww[size];
		if (tp>x)
			g[x].insert(tp);
	}
}

void calc(){
	for (int i = 1;i <=3000;i++)
		find(i);
}

int cft;

int f(int idx){
	cft=0;
	set<int>::iterator it = g[idx].begin();
	for(;it!=g[idx].end();it++){
		if (*it>=a && *it<=b)
			cft++;
	}
	return cft;
}

int main()
{
	calc();
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	int ans;
	FOR(t){
		ans=0;
		cin >> a >> b;
		for (int j = a;j<=b;j++)
			ans+=f(j);
		cout << "Case #" << i+1 << ": "<< ans<< endl;
	}
	return 0;
}
