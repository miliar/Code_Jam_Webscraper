#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;


char tb[60][60];
char tb2[60][60];
int N,K;

main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-output.txt","w",stdout);
	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-output.txt","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large-output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		scanf("%d %d",&N,&K);
		int i,j;
		for(i=0;i<N;i++)
			scanf("%s",tb[i]);
// 		for(i=0;i<N;i++)
// 		{
// 			for(j=0;j<N;j++)
// 				putchar(tb[i][j]);
// 			putchar('\n');
// 		}
// 		putchar('\n');
		for(i=0;i<N;i++)for(j=0;j<N;j++)
			tb2[j][N-i-1]=tb[i][j];
		
		memset(tb,'.',sizeof(tb));
		for(j=0;j<N;j++)
		{
			i=N-1;
			int t= N-1;
			while(i>=0)
			{
				while(tb2[i][j]=='.' && i>=0)i--;
				while(tb2[i][j]!='.' && i>=0)tb[t--][j]=tb2[i--][j];
			}
			
		}

// 		for(i=0;i<N;i++)
// 		{
// 			for(j=0;j<N;j++)
// 				putchar(tb[i][j]);
// 			putchar('\n');
// 		}
		bool Rwin=false,Bwin=false;
		for(i=0;i<N;i++)for(j=0;j<N;j++)
		{
			if(tb[i][j]=='.')continue;
			if(tb[i][j]=='R')
			{
				int k=0;
				for(k=0;k<K && i+k<N;k++)if(tb[i+k][j]!='R')break;
				if(k>=K)Rwin=true;
				for(k=0;k<K && j+k<N;k++)if(tb[i][j+k]!='R')break;
				if(k>=K)Rwin=true;
				for(k=0;k<K && j+k<N && i+k<N;k++)if(tb[i+k][j+k]!='R')break;
				if(k>=K)Rwin=true;
				for(k=0;k<K && i-k>=0 && j+k<N;k++)if(tb[i-k][j+k]!='R')break;
				if(k>=K)Rwin=true;
			}
			if(tb[i][j]=='B')
			{
				int k=0;
				for(k=0;k<K && i+k<N;k++)if(tb[i+k][j]!='B')break;
				if(k>=K)Bwin=true;
				for(k=0;k<K && j+k<N;k++)if(tb[i][j+k]!='B')break;
				if(k>=K)Bwin=true;
				for(k=0;k<K && j+k<N && i+k<N;k++)if(tb[i+k][j+k]!='B')break;
				if(k>=K)Bwin=true;
				for(k=0;k<K && i-k>=0 && j+k<N;k++)if(tb[i-k][j+k]!='B')break;
				if(k>=K)Bwin=true;
			}
		}

		if(Rwin&&Bwin)
			printf("Case #%d: Both\n",Case);
		else if(Rwin)
			printf("Case #%d: Red\n",Case);
		else if(Bwin)
			printf("Case #%d: Blue\n",Case);
		else
			printf("Case #%d: Neither\n",Case);
	}

}