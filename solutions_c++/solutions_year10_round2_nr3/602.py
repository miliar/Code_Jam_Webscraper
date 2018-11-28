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

int x[]={0,0,1,2,3,5,8,14,24,43,77,140,256,472,874,1628,3045,5719,10780,20388,38674,73562,40265,68060,13335,84884};
int main()
{
	freopen("c://Codejam//C.in","r",stdin);
	//freopen("c://Codejam//A.txt","w",stdout);
	freopen("c://Codejam//C.out","w",stdout);
	/*int i,j,k,n,su,val;
	fo(n,2,26)
	{
		su=0;
		fo(i,1,1<<n)
		{
			if(i & 1)co;
			if(!(i & 1<<(n-1)))co; k = 0; val=1;
			fo(j,1,n)
			{
				if(!(i&(1<<j)))co;
				k++; if(k==val){val = j+1; if(val==n){su++;break;} }
			}
		}
		printf("%d,",su%100003);
	}
	printf("\n");
	*/
	int t,T,n;
	scanf("%d",&T);
	fo(t,1,T+1)
	{
		scanf("%d",&n);
		printf("Case #%d: %d\n",t,x[n]);
	}
} 

