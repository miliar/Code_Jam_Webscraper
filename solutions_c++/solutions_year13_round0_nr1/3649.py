//==========================================================================
// Author      : NIRWAN DOGRA
// Version     : 4.3.2
// Copyright   : Your copyright notice
// Description : C++, Ansi-style
//============================================================================
#include<algorithm>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<sstream>
#include<bitset>
#include<cstdio>
#include<cmath>
#include<ctime>
#include<string>
#include <stdio.h>
#include <stdlib.h>
//////////definitions
#define dd cout<<"HERE"<<endl;
#define gg getch();
#define pi pair<int,int>
#define pii pair<pi,int>
#define ff first
#define ss second
#define ST set<int>
#define VEC vector<int>
#define QU queue<int>
#define MAP map<int ,int>
#define l long
#define ll long long
#define forr(i,n) for(int i=0;i<n;i++)
#define forrr(i,j,n) forr(i,n){forr(j,n)
#define S(n) scanf("%d",&n);
#define P(n) printf("%d\n",n);
#define SL(n) scanf("%lld",&n);
#define PL(n) printf("%lld\n",n);
#define C(n) cin>>n;
#define DEBUG if(0)
#define PAUSE system("pause");
#define SET(a,val) memset(a,val,sizeof a);
#define pb push_back
#define CO(n) cout<<n<<endl;
#define MOD 1000000007
#define INF 1000000007

using namespace std;
//power function
inline int max_(int a,int b){if(a>=b){return a;}else return b;}
inline int min_(int a,int b){if(a>=b){return b;}else {return a;}}
inline int mod(int a,int b){return (a < b ? a : a % b); }

template< class T > T sq(T &x) { return x * x; }
template< class T > T abs(T &n) { return (n < 0 ? -n : n); }
template< class T > T max(T &a, T &b) { return (!(a < b) ? a : b); }
template< class T > T min(T &a, T &b) { return (a < b ? a : b); }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > T mod(T &a, T &b) { return (a < b ? a : a % b); }
template< class T > bool inside(T &a, T &b, T &c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }


////MAIN CODE BEGINS NOW...........
int N,M;
int a[111][111];int k=0;

int check(int x,int y)
{
	int flag;
	flag=1;
	 forr(i,N)
	 {
	 	if(a[i][y]!=a[x][y] && a[i][y]!=-1)
	 	{
	 		 flag=0;
			 break;
	 	}
	 }
	 if(flag==1)
	 {
	 	return 1;
	 }
	 flag=1;
	  forr(i,M)
	 {
	 	if(a[x][i]!=a[x][y] &&a[x][i]!=-1 )
	 	{
	 		flag=0;
	 		break;
	 	}
	 }
	 if(flag==1)
	 {
	 	return 1;
	 }
	  
	   if(x!=y && (x+y)!=3)
     {
     	return 0;
     }
     
	
	  if(x==y)
	  {
	  	flag=1;
	    forr(i,M)
	    {
	 	if(a[i][i]!=a[x][y] &&a[i][i]!=-1 )
	 	 {
	 		flag=0;
	 		break;
	 	 }
	    }	
	  }
	  
	  if(flag==1)
	  {
	  	return 1;
	  }
	  
	  
	  if(x+y==3)
	  {
	  	flag=1;
	    forr(i,4)
	    {
	 	if(a[i][3-i]!=a[x][y] && a[i][3-i]!=-1 )
	 	 {
	 		flag=0;
	 		break;
	 	 }
	    }	
	  }
	    if(flag==1)
	  {
	  	return 1;
	  }	  
	  /////flag=1;
	  return 0;
}

int solve()
{
	int dots=0;;int val;
      forr(i,N)
     {
     	forr(j,M)
     	{
     		val=0;
     		if(a[i][j]==-1 || a[i][j]==0)
     		{
     			if(a[i][j]==0)
     			{
     				dots++;
     			}
     			continue;
     		}
     		val=check(i,j);;;
     		//CO(i<<" "<<j<<" "<<val)
     		if( val==1 && a[i][j]==2)
     		{
     			CO("Case #"<<(++k)<<": O won")
     			return 0;
     		}
     			if( val==1 && a[i][j]==1)
     		{
     			CO("Case #"<<(++k)<<": X won")
     			return 0;
     		}
     	}
     }
     if(dots!=0)
     {
		CO("Case #"<<(++k)<<": Game has not completed")
	 return 0;
     }
     CO("Case #"<<(++k)<<": Draw")
return 0;
}
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
int T;C(T);///int k=0;
k=0;;;char str[11];
while(T--)
{
        //C(N>>M)
        N=4;M=4;
		forr(i,4)
		{
			C(str)
			forr(j,4)
			{
				if(str[j]=='X')
			    {
			    	a[i][j]=1;
			    }
			    else if(str[j]=='O')
			    {
			    	a[i][j]=2;
			    }
			    else if(str[j]=='T')
			    {
			    	a[i][j]=-1;
			    }
			    else
			    {
			    	a[i][j]=0;
			    }
			}
		}
	    solve();;;;
}
return 0;
}


