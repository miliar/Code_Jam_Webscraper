#include <algorithm>
#include <cctype>
#include <iostream>
#include <iomanip>
#include <utility>
#include <sstream>
#include <set>
#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <queue>
#include <stack>
typedef long long LL;
const double PI = acos(-1.0);
using namespace std;
int A[20];
int Ans;
int N;
void Fun(int x)
{
	int i,j,k;
	int aa=0;
	int bb=0;
	int a=0;
	int b=0;
	for(i=0;i<N;++i)
	{
		if((x>>i)&1)
		{
			a^=A[i];
			aa+=A[i];
		}
		else 
		{
			b^=A[i];
			bb+=A[i];
		}
	}
	if(a==b)
	{
		Ans=max(Ans,max(aa,bb));
	}
}
int main()
{
	int T;
	int cas;
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("tt.txt","w",stdout);
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		printf("Case #%d: ",cas);
		int i,j,k;
		scanf("%d",&N);
		for(i=0;i<N;++i)
			scanf("%d",&A[i]);
		Ans=-1;
		for(i=1;i<(1<<N)-1;++i)
		{
			Fun(i);
		}
		if(Ans==-1)
		{
			printf("NO\n");
		}
		else 
			printf("%d\n",Ans);
	}
	return 0;
}