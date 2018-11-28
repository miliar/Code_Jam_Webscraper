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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;

#define FRsmall(x,y) freopen(#x"-small-attempt"#y".in","r",stdin);freopen(#x"-small-attempt"#y".out","w",stdout);
#define FRlarge(x) freopen(#x"-large.in","r",stdin);freopen(#x"-large.out","w",stdout);

char d[11][10010][11];
int n[11];
int loc[11][10010];

int Q[2][10010],q[2];
int pre,now;

char s[11];
char m[27];

int main()
{
	//freopen("B.in","r",stdin);
	FRsmall(B,0)
	//FRlarge(B)

	int T,TC=0;
	scanf("%d",&T);
	while(++TC<=T)
	{
		printf("Case #%d:",TC);
		int N,M,i,j,k,a,b,l,p,mn,c,ml,mk;
		scanf("%d %d",&N,&M);
		memset(n,0,sizeof(n));
		for(i=0;i<N;i++)
		{
			scanf("%s",s);
			l=strlen(s);
			strcpy(d[l][n[l]],s);
			loc[l][n[l]]=i;
			n[l]++;
		}
		while(M--)
		{
			scanf("%s",m);p=-1;
			for(i=1;i<=10;i++)
			{
				for(j=0;j<n[i];j++)
				{
					pre=0;now=1;
					q[pre]=0;
					for(k=0;k<n[i];k++)Q[pre][q[pre]++]=k;
					c=0;
					for(k=0;k<26;k++)
					{
						for(a=0;a<q[pre];a++)
						{
							for(b=0;b<i;b++)if(d[i][Q[pre][a]][b]==m[k])break;
							if(b!=i)break;
						}
						if(a==q[pre])continue;
						for(b=0;b<i;b++)if(d[i][j][b]==m[k])break;
						if(b==i)c++;
						q[now]=0;
						for(a=0;a<q[pre];a++)
						{
							for(b=0;b<i;b++)if(d[i][j][b]==m[k] && d[i][Q[pre][a]][b]!=m[k] || d[i][j][b]!=m[k] && d[i][Q[pre][a]][b]==m[k])break;
							if(b==i)Q[now][q[now]++]=Q[pre][a];
						}
						swap(pre,now);
					}
					assert(q[pre]==1);
					if(c>p || c==p && loc[i][j]<mn)
					{
						p=c;
						mn=loc[i][j];
						ml=i;
						mk=j;
					}
				}
			}
			printf(" %s",d[ml][mk]);
		}
		putchar('\n');
	}
	return 0;
}
