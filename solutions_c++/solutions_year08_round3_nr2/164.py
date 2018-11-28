// b.cpp : Defines the entry point for the console application.
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

int a[6];
i64 ans;
int n;

//void per(int ind, int zl2,int zl3, int zl5, int zl7,int h2 int h3, int h5 int h7, int zn)
//{
//	if (ind == n)
//	{
//		if (zl2*zl3*zl5*zl7 == 0) ans++;
//		return;
//	}
//	
//
//	per(ind+1,
//		 zl2,zl3,zl5,zl7,
//		 a[ind]%2, (h3*10+a[ind])%3, a[ind]%5, (h7*10+a[ind])%7,zn );
//	per(ind+1,
//		(zl2+h2)%2, (zl3+h3)%3, (zl5+h5)%5, (zl7+h7*10+a[ind])%7,
//		0,0);
//	per(ind+1,
//		(zl2-a[ind])%2, (zl3-h3*10-a[ind])%3, (zl5-a[ind])%5, (zl7-h7*10-a[ind])%7,
//		0,0);
//}


void hid(int ind, int zl2,int zl3, int zl5, int zl7,int h2, int h3, int h5, int h7, int zn)
{
	if (ind == n)
	{
		if ( (zl2+zn*h2)%2 == 0 ) ans++;
		else if ( (zl3+zn*h3)%3==0 ) ans++;
		else if ( (zl5+zn*h5)%5==0 ) ans++;
		else if ( (zl7+zn*h7)%7==0 ) ans++;
		return ; 
	}

	hid(ind+1,
		zl2,zl3,zl5,zl7,
		a[ind]%2,(h3*10+a[ind])%3,a[ind]%5,(h7*10+a[ind])%7,
		zn);
	hid(ind+1,
		(zl2+zn*h2)%2,(zl3+zn*h3)%3,(zl5+zn*h5)%5,(zl7+zn*h7)%7,
		a[ind]%2,a[ind]%3,a[ind]%5,a[ind]%7,1
		);
	hid(ind+1,
		(zl2+zn*h2)%2,(zl3+zn*h3)%3,(zl5+zn*h5)%5,(zl7+zn*h7)%7,
		a[ind]%2,a[ind]%3,a[ind]%5,a[ind]%7,-1);
	
}

int main()
{
	freopen("q.in","r",stdin);
	freopen("q.out","w",stdout);
	int kil;
	scanf("%d\n",&kil);
	int mb,k,md,d;
	rep(nt,kil)
 	{
		mset(a,0);
		n=0;
		while ( (a[n]=getchar()) != '\n' && a[n]!=EOF ) a[n]-='0', n++;
		a[n]=0;
		ans=0;
		//per(1, a[0]%2,a[0]%3,a[0]%5,a[0]%7, a[0]%3,a[0]%7);
		hid(1,0,0,0,0,a[0]%2,a[0]%3,a[0]%5,a[0]%7,1);
		printf("Case #%d: ",nt+1); cout << ans << endl;
	}
	return 0;
}

