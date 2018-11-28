#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<vector>
#include<cstring>
using namespace std;
#define SIZE 120
int gn,gm;
int mat[SIZE][SIZE];
int link[SIZE];
int useif[SIZE];
int can(int t)
{
    int i;
    for(i = 1; i <= gm; i ++)
    {
          if(useif[i] == 0 && mat[t][i])
          {
                useif[i] = 1;
                if(link[i] == -1 || can(link[i]))
                {
                       link[i] = t;
                       return 1;
                }
          }
    }
    return 0;
}

int MaxMatch(void)
{
    int i , num;
    num = 0;
    memset(link , -1 , sizeof(link));
  
    for(i = 1 ; i <= gn ; i ++)
    {
          memset(useif , 0 , sizeof(useif));
          if(can(i))
                 num ++ ;
    }
    
    return num;
}
struct node{
	int num[50];
};
node p[120];
bool cmp(node l,node r)
{
	return l.num[0]<r.num[0];
}
int main(void)
{
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);

	int tn;
	scanf("%d",&tn);
	int cas=0;
	while(tn--)
	{
	int n,k;
	scanf("%d%d",&n,&k);
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<k;j++)
			scanf("%d",&p[i].num[j]);
	}
	sort(p,p+n,cmp);
	memset(mat,0,sizeof(mat));
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
		{
			int s;
			for(s=0;s<k;s++)
			{
				if(p[j].num[s]>p[i].num[s])
					;
				else
					break;
			}
			if(s==k)
				mat[i][j]=1;
		}
/*	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
			cout<<mat[i][j]<<" ";
		cout<<endl;
	}*/
	gn=n;
	gm=n;
//	cout<<gn<<","<<gm<<endl;
//	cout<<MaxMatch()<<endl;
	int ans=n-MaxMatch();
	printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
