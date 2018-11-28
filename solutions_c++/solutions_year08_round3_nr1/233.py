// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>

using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define pb(z) push_back(z)
#define forr(i,a,b) for(int i=a; i<=b; i++)
#define ford(i,a,b) for(int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz size
#define min(a,b) (a<b ? a : b) 
#define max(a,b) (a<b ? b : a)
#define sqr(a) a*a
#define X first
#define Y second
#define all(A) A.begin,A.end

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int,int> PII;
typedef long long i64;
typedef vector<string> VS; 

int a[5000];

int main()
{
	freopen("q.in","r",stdin);
	freopen("q.out","w",stdout);
	int kil;
	scanf("%d",&kil);
	int n,mb,k,md,d;
	i64 ans;
	rep(nt,kil)
 	{
		mset(a,0);
		scanf("%d %d %d",&mb,&k,&n);
		rep(i,n) scanf("%d",&a[i]);
		sort(a,a+n);
		reverse(a,a+n);	
		ans=0;
		md=0;d=1;
		rep(i,n)
		{
			if (a[i] >0) md=i;
			ans+=i64(d)*i64(a[i]);
			if (i%k == k-1) d++;
		}

		md++;
		if (md <= mb*k) printf("Case #%d: ",nt+1), cout << ans << endl;
		else printf("Case #%d: Impossible\n");		
	}





	return 0;
}

