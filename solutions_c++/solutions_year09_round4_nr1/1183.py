#include<iostream>
#include<queue>
using namespace std;
typedef struct node{
	int s;
	int step;
	node(){}
	node(int ss,int sp):s(ss),step(sp){}
}node;


char c[50][50];

char flag[100000000];

int l[50];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int ca,cas;
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		int i,j;
		int n;
		scanf("%d",&n);
		int s=0;
		for(i=0;i<n;i++)
		{
			scanf("%s",c[i]);
			for(j=n-1;j&&c[i][j]=='0';j--);
			s = s*10 + j+1;
		}
		memset(flag,0,sizeof(flag));
		queue<node> que;
		flag[s] = 1;
		que.push( node(s,0) );
		node t;
		while(!que.empty())
		{
			t = que.front();
			que.pop();
			for(i=n;i>=1;i--)
			{
				l[i] = t.s%10;
				t.s /= 10;
			}
			for(i=1;i<=n;i++)
				if(l[i]>i)
					break;
			if(i>n)
				break;
			t.step++;
			for(i=1;i<n;i++)
			{
				swap(l[i],l[i+1]);
				t.s = 0;
				for(j=1;j<=n;j++)
					t.s = t.s*10+l[j];
				if(flag[t.s]==0)
				{
					flag[t.s] = 1;
					que.push( node(t.s,t.step));
				}
				swap(l[i],l[i+1]);
			}
		}
		printf("Case #%d: %d\n",ca,t.step);
	}
}