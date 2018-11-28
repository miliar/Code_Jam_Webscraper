// g3.cpp : Defines the entry point for the console application.
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

int step[6] = {0,1, 10,100,1000,10000};
int a,b;

int countDigits(int ch){
 int k=0;
 while (ch) {
	 k++;
	 ch/=10;
 }
 return k;
}

int main()
{
	freopen("g3.in","r",stdin);
	freopen("g3.out","w",stdout);	
	int n;
	scanf("%d",&n);
	rep(testNum,n){
		scanf("%d %d",&a,&b);
		printf("Case #%d: ",testNum+1);
		int k=countDigits(a);
		int ans = 0;
		if (1 == k) printf("0\n"); 
		else {
			for(int i=a; i<b; i++){
				int ch=i;
				rep(j,k-1){
					int m = (ch%10)*step[k]+ch/10;
					if (m>i && m<=b) ans++;
					ch=m;
				}
			}
			printf("%d\n",ans);
		}
	}
	return 0;
}

