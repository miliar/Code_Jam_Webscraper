#include<stdio.h>
#include<string>
#include<iostream>
#include<vector>
#include<map>
using namespace std;
#include<string.h>
const int N = 100+10;
vector<int>op[300];
struct node
{
	char c;
	char to;
};
vector<node>com[300];
char str[N];
char ans[N];
string tmp;
int visited[300];
int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int T;
	int i,j;
	scanf("%d",&T);
	int cases ;
	for(cases=1;cases<=T;cases++)
	{
      int c,d;
	
	  for(i=0;i<300;i++)
	  {
		  com[i].clear();
		  op[i].clear();
	  }
	  scanf("%d",&c);
	  node cur;
	  while(c--)
	  {
		  scanf("%s",str);
		  cur.c=str[1];
		  cur.to=str[2];
		  com[str[0]].push_back(cur);
		  cur.c=str[0];
		  com[str[1]].push_back(cur);
	  }

	  scanf("%d",&d);
	  while(d--)
	  {
		  scanf("%s",str);
		  op[str[0]].push_back(str[1]);
		  op[str[1]].push_back(str[0]);
	  }

	  int n;
	  scanf("%d",&n);
	  memset(visited,0,sizeof(visited));
	  scanf("%s",str);
	  int alen = 0;
	  
	  for(i=0;i<n;i++)
	  {
        ans[alen++]=str[i];
		visited[str[i]]++;
		if(alen>1)
		{
			char cc = ans[alen-1];
			char pc = ans[alen-2];
			int sz = com[cc].size();
			for(j=0;j<sz;j++)
				if(com[cc][j].c==pc)
				   break;
			if(j<sz)
			{
				visited[cc]--;
				visited[pc]--;
				visited[com[cc][j].to]++;
				alen-=2;
				ans[alen++]=com[cc][j].to;
			}
		}
	
		if(alen>1)
		{
            visited[ans[alen-1]]--;
			char cc = ans[alen-1];
		    int sz = op[cc].size();
		    for(j=0;j<sz;j++)
		    {
			   if(visited[op[cc][j]]>0)break;
		    }
		    if(j==sz)
			   visited[ans[alen-1]]++;
		    else
		  {
			  alen=0;
			  memset(visited,0,sizeof(visited));
		  }
		}
	  }
      
	  printf("Case #%d: [",cases);
	  if(alen>0)
		  printf("%c",ans[0]);
	  for(i=1;i<alen;i++)
		  printf(", %c",ans[i]);
      printf("]\n");

	}
	return 0;
}
