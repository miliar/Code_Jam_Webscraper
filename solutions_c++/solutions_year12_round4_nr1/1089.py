// g2_1.cpp : Defines the entry point for the console application.
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

const int N = 20000;

PII a[N];
int n;
int d;
int h[N];

int main()
{
	freopen("g2_1.in","r",stdin);
	freopen("g2_1.out","w",stdout);
	int testCase;
	scanf("%d",&testCase);
	rep(testNum,testCase){
		scanf("%d",&n);
		bool f = false;
		rep(i,n) {
			int u,v;
			scanf("%d %d",&u,&v);
			a[i]=mp(u,v);
			h[i]=-1;
		}
		scanf("%d",&d);
		h[0]=a[0].X;

		rep(i,n)
		{
			int u=a[i].X+h[i];
			if (u>=d) {
				f=true;
				break;
			}
			int j=i+1;
			while (j<n && u>=a[j].X) {
				int v = min(a[j].X-a[i].X,a[j].Y);
				if (v>h[j]) h[j]=v;
				j++;
			}			
		}

		printf("Case #%d: ",testNum+1);
		if (f) printf("YES\n");
		else printf("NO\n");
	}
	
	return 0;
}

