#include<stdio.h>
#include<algorithm>
using namespace std;

const int MAXN = 120;

struct node
{
	int c,pos;
}T[MAXN];

int n;
int abs(int x)
{
	if (x > 0) return x;
	return -x;
}

int main()
{
	char ch[5];
	int test;
	
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d",&test);
	for (int cas=1;cas<=test;cas++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%s%d",ch,&T[i].pos);
			if (ch[0] == 'O')
			{
				T[i].c = 0;
			}else
				T[i].c = 1;
		}
		int nowx = 1,nowy = 1;
		int ans = 0,tmp;
		for (int i=1;i<=n;i++)
		{
			if (T[i].c == 0)
			{
				tmp = abs(T[i].pos - nowx) + 1;
				
				int cho = -1;
				for (int j=i;j<=n;j++)
				if (T[j].c == 1)
				{
					cho = j;
					break;
				}
				if (cho != -1)
				{
					if (T[cho].pos > nowy)
						nowy = min(nowy+tmp,T[cho].pos);
					else
						nowy = max(nowy-tmp,T[cho].pos);
				}
				nowx = T[i].pos;
			}else
			{
				tmp = abs(T[i].pos - nowy) + 1;
				
				int cho = -1;
				for (int j=i;j<=n;j++)
				if (T[j].c == 0)
				{
					cho = j;
					break;
				}
				if (cho != -1) 
				{
					if (T[cho].pos > nowx)
						nowx = min(nowx+tmp,T[cho].pos);
					else
						nowx = max(nowx-tmp,T[cho].pos);
				}
				nowy = T[i].pos;
			}
			ans += tmp;
			//printf("tmp is %d\n",tmp);
		}
		printf("Case #%d: %d\n",cas,ans);
	}
}

