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
char Mp[258][258];
int Op[258][258];
char Input[1000000];
char Ans[1000000];
int main()
{
	int T;
	int cas;
//	freopen("B-large.in","r",stdin);
	//freopen("in.txt","r",stdin);
	//freopen("tt.txt","w",stdout);
	scanf("%d",&T);
	int Tp;
	for(cas=1;cas<=T;++cas)
	{
		int C,D,N;
		int i,j,k;
		memset(Mp,-1,sizeof(Mp));
		memset(Op,0,sizeof(Op));
		Tp=0;
		scanf("%d",&C);
		for(i=0;i<C;++i)
		{
			char str[30];
			scanf("%s",str);
			Mp[str[0]][str[1]]=str[2];
			Mp[str[1]][str[0]]=str[2];
		}
		scanf("%d",&D);
		for(i=0;i<D;++i)
		{
			char str[30];
			scanf("%s",str);
			Op[str[0]][str[1]]=1;
			Op[str[1]][str[0]]=1;
		}
		scanf("%d",&N);
		scanf("%s",Input);
		int len=strlen(Input);
		for(i=0;i<len;++i)
		{
			char tmp=Input[i];
			while(Tp)
			{
				char tt;tt=Ans[Tp-1];
				if(Mp[tt][tmp]!=-1)
				{
					--Tp;
					tmp=Mp[tt][tmp];
				}
				else 
					break;
			}
			int flag=1;
			for(j=0;j<Tp;++j)
			{
				char aa=Ans[j];
				if(Op[Ans[j]][tmp])
				{
					flag=0;
					Tp=0;
					break;
				}
			}
			if(flag)
				Ans[Tp++]=tmp;
		}
		printf("Case #%d: [",cas);
		if(Tp)
		{
			printf("%c",Ans[0]);
			for(i=1;i<Tp;++i)
				printf(", %c",Ans[i]);
		}
		printf("]\n");
	}
	return 0;
}