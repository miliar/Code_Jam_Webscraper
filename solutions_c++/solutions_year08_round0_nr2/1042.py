#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;

int turn,n,m;
typedef struct
{
	int s,e;
	int f;
}road;
road r[1000];

int cmp(road A,road B)
{
	if(A.s==B.s)
	{
		return A.e<B.e;
	}
	return A.s<B.s;
}

int queue[1000];

int main()
{
	int test,i,j,k,T=1;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(;test>0;test--)
	{
		scanf("%d",&turn);
		scanf("%d%d",&n,&m);
		m+=n;
		for(i=0;i<n;i++)
		{
			scanf("%d:%d",&j,&k);
			r[i].s=j*60+k;
			scanf("%d:%d",&j,&k);
			r[i].e=j*60+k;
			r[i].f=0;
		}
		for(i=n;i<m;i++)
		{
			scanf("%d:%d",&j,&k);
			r[i].s=j*60+k;
			scanf("%d:%d",&j,&k);
			r[i].e=j*60+k;
			r[i].f=1;
		}
		sort(r,r+m,cmp);
		int top=0,s[2];
		s[0]=s[1]=0;
		for(i=0;i<m;i++)
		{
			for(j=0;j<top;j++)
			{
				if(r[i].f!=r[queue[j]].f && r[queue[j]].e+turn<=r[i].s)
				{
					queue[j]=i;
					break;
				}
			}
			if(j==top)
			{
				s[r[i].f]++;
				queue[top++]=i;
			}
		}
		printf("Case #%d: %d %d\n",T++,s[0],s[1]);
	}
}
