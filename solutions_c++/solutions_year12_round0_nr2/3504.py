// g2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define forr(i,a,b) for (int i=a; i<=b; i++)
#define ford(i,a,b) for (int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz(a) int( a.size() )
#define all(A) A.begin(),A.end()
#define sqr(q) q*q
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define X first
#define Y second

typedef long long i64;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;


int main()
{
	freopen("g2.in","r",stdin);
	freopen("g2.out","w",stdout);	
	int testNum;
	scanf("%d",&testNum);
	rep(test,testNum){
		int n,s,p;
		scanf("%d %d %d\n",&n,&s,&p);
		int ans = 0;
		rep(i,n){
			int ch;
			scanf("%d",&ch);
			if (0 == p) ans++;
			else if (1 == p) { if (ch) ans++; }
			else {
				if (ch>=3*p-2) ans++;
				else if (3*p-4==ch || 3*p-3==ch) {
					if (s) {ans++; s--;}
				}

			}
		}
		printf("Case #%d: %d\n",test+1,ans);

	}
	return 0;
}

