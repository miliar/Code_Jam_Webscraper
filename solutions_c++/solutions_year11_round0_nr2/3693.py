#include <stdio.h>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
int C,D,N;
map<char,char> cb[129];
set<char> del[129];
char seq[102];
char res[102];
int rescnt;
void Solve()
{
	rescnt = 0;
	res[rescnt++] = seq[0];
	for (int i=1; i<N; i++)
	{
		char cchr = seq[i];
		if (rescnt>0 && cb[cchr].find(res[rescnt-1])!=cb[cchr].end())
		{
			char tchr = cb[cchr][res[rescnt-1]];
			res[rescnt-1] = tchr;
		}
		else
		{
			bool f = false;
			if (del[cchr].size())
			{
				
				for (int v=rescnt-1;v>=0;v--)
				{
					char xchr = res[v];
					if (del[cchr].find(xchr)!=del[cchr].end())
					{
						rescnt = 0;
						f = true;
						break;
					}
				}
			}
			if (f==false)
			{
				res[rescnt++] = cchr;
			}
		}
	}
	printf("[");
	for (int i=0; i< rescnt; i++)
	{
		if (i!=0)
		{
			printf(", ");
		}
		printf("%c",res[i]);
	}
	printf("]\n");
	//res[rescnt] = 0;
	//printf("[%s]\n",res);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ncase;
	scanf("%d",&ncase);
	for (int c=1; c<=ncase; c++)
	{
		for (int z=0; z<=128; z++)
		{
			cb[z].clear();
			del[z].clear();
		}
		printf("Case #%d: ",c);
		scanf("%d\n",&C);
		for(int i=1; i<=C; i++)
		{
			char b1,b2,t;
			scanf("%c%c%c",&b1,&b2,&t);
			cb[b1].insert(make_pair(b2,t));
			cb[b2].insert(make_pair(b1,t));
		}
		scanf("%d\n",&D);
		for(int i=1; i<=D; i++)
		{
			char b1,b2,t;
			scanf("%c%c",&b1,&b2);
			del[b1].insert(b2);
			del[b2].insert(b1);
		}
		scanf("%d\n",&N);
		gets(seq);
		Solve();
	}
}