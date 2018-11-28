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

#define LL long long
#define fr(i,n) for(i=0;i<n;i++)
#define INF (2000000000)
#define FOR(n) for(int i = 0;i < n;i++)
#define CLEAR(x) memset(x,0,sizeof(x))
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back((a))

using namespace std;

bool can(int m,int p){
	int c = m/3+1;
	if (m%3 == 2)
		c++;
	return c>=p;
}

bool ns(int m,int p){
	int c = m/3+1;
	if (m%3 == 0)
		c--;
	return c>=p;
}

int main()
{
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t,n,s,p,m;
	cin >> t;
	for (int cc=0;cc<t;cc++){
		cin >> n >> s >> p;
		int cnt = 0;
		int t[3];
		t[0]=0;
		t[1]=0;
		t[2]=0;
		FOR(n){
			bool x=false,y=false;
			cin >> m;
			x = (m>=2&&m<=28)&&can(m,p);
			y = ns(m,p);
			if(x&&y)
				t[0]++;
			else if(x)
				t[1]++;
			else if(y)
				t[2]++;
		}
		if (t[1]>s)
			t[1]=s;
		if (t[2]>n-s)
			t[2]=n-s;
		t[1] = t[1]+t[0];
		t[0]=0;
		if (t[1]>s){
			t[0]=(t[1]-s);
			t[1]=s;
		}

		t[2] = t[2]+t[0];
		t[0]=0;
		if (t[2]>n-s){
			t[0]=(t[2]-(n-s));
			t[2]=n-s;
		}

		if (t[0]!=0)
			cout << "FATAL";

		cnt = t[1]+t[2];

		cout << "Case #" << cc+1 << ": " << cnt << endl;
	}
	return 0;
}

