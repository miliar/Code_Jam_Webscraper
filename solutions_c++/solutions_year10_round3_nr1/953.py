#include<math.h> 
#include "stdafx.h"
#include<ctype.h>
#include<stdlib.h> 
#include<stack>
#include<queue> 
#include<list>
#include<map>

#include<string.h> 
#include<algorithm> 
#include<iostream>
#include<sstream> 
#include<vector> 
#include<string> 

using namespace std; 

#define vi vector<int>
#define vd vector<double>
#define vs vector<string>

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) for(i=j;i<(int)v.size();++i)
#define Foo(i,j,v) for(i=(int)v.size()-1;i>=j;--i)
#define li(v) v.begin(),v.end()
#define sz(v) (int)v.size()
#define co continue;
#define re return
#define inf (1e8+1)

#define pi (2*acos(0))
#define eps 1e-9
typedef __int64 Long;
//typedef long long Long;

vector<int> L,R;
int main()
{
	freopen("c://Codejam//A.in","r",stdin);
	freopen("c://Codejam//A.out","w",stdout);
	int i,j,t,T,su,n,n1,n2;
	scanf("%d",&T);
	fo(t,1,T+1)
	{
		L.clear(); R.clear(); su = 0;
		scanf("%d",&n);
		fo(i,0,n)
		{
			scanf("%d%d",&n1,&n2); L.push_back(n1); R.push_back(n2);
		}
		fo(i,0,n)fo(j,i+1,n)
		{
			if((L[i]<L[j])&&(R[i]<R[j]))co;
			if((L[i]>L[j])&&(R[i]>R[j]))co;
			su++;
		}
		printf("Case #%d: %d\n",t,su);
	}
} 

