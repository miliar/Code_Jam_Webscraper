#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define rep(i,n) for(int i=0;i<(n);i++)
#define rept(i,m,n) for(int i=(m);i<(n);i++)
#define ull unsigned long long
#define lint long long
#define MX 10000001

int main()
{
	int i,j,k,n,t;
	char dummy;
	char mapping[27]="yhesocvxduiglbkrztnwjpfmaq";	
	char G[128];
	scanf("%d",&t);
	for(k=1;k<=t;++k)
	{
		scanf("\n");
		string ans="";
		char ch;
		while(1)
		{
			scanf("%c",&ch);
			if(ch=='\n')
				break;
			else if(ch==' ')
				ans+=' ';
			else
				ans+=mapping[ch-'a'];
		}
		cout<<"Case #"<<k<<": "<<ans<<"\n";
	}	
	return 0;
}









