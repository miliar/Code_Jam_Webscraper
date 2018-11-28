#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<int(b);++i)
#define SZ(v) ((int)v.size())
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define ALL(v) (v).begin(),(v).end()
#define SS stringstream
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define SQR(x) (x)*(x)
#define FILL(A,x) memset((A),(x),sizeof(A))

#define PLUS +1
#define MINUS -1

long long A[13][13];

string s;
long long N,ans;


long long getN(int l,int r)
{
	if(A[l][r]!=-1)
		return A[l][r];
	else
	{
	istringstream ss(s.substr(l,r-l+1));
	//long long ans;
	ss>>A[l][r];
	return A[l][r];
	}
}


void solve(int l,int r,int sign,long long value)
{
	if(l>r)
		return;
	long long a=getN(l,r),res;
	res=value+sign*a;
	
	if(res==0||res%2==0||res%3==0||res%5==0||res%7==0)
		ans++;
	FOR(i,l,r)
	{
		//if(i!=0)	
		{
			solve(i+1,r,PLUS,value+sign*getN(l,i));
			solve(i+1,r,MINUS,value+sign*getN(l,i));
		}
		
		
			
		

	}
	
}

int main()
{
freopen ("B-small-attempt1.in","r",stdin);
freopen ("out.txt","w",stdout);
	
	
	cin>>N;
	FOR(kk,0,N)
	{
		FILL(A,-1);
		cin>>s;
		ans=0;
		solve(0,SZ(s)-1,PLUS,0);
		cout<<"Case #"<<kk+1<<": "<<ans<<endl; 
	}
	return 0;
}
