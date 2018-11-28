#include<math.h> 

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
#define foo(i,j,v) for(i=j;i<v.size();++i)
#define li(v) v.begin(),v.end()
#define co continue;
#define re return 
#define max(a,b) ((a>b) ? a : b)

#define min(a,b) ((a<b) ? a : b)
#define max(a,b) ((a>b) ? a : b)

#define inf (1e8+1)
#define pi (2*acos(0))
#define eps 1e-9
typedef __int64 Long;

void main()
{
	freopen("c://Codejam//A.in","r",stdin);
	freopen("c://Codejam//A.out","w",stdout);
	Long i,T,N,K,M;
	string s = "";	
	scanf("%I64d",&T);
	fo(i,1,T+1)
	{
		scanf("%I64d%I64d",&N,&K);
		M = 1 << N; K%=M; M--;
		if( K == M )s = "ON"; else s = "OFF";
		printf("Case #%I64d: %s\n",i,s.c_str());
	}
	
} 

