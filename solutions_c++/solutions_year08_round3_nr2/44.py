#include<stdio.h>
#include<string.h>

int len;
int a[41];
char c[50];

__int64 f[41][2*3*5*7];

class Node
{
public:
	int a[5];
};

int p[]={0,3,5,7,1};

int encode(Node a)
{
	int i,s=0;
	for(i=1;i<=4;i++)
	{
		s=(s+a.a[i])*p[i];		
	}
	return s;
}

int pp[]={0,2,3,5,7};
Node decode(int num)
{
	int i;
	Node t;

	for(i=4;i>=1;i--)
	{
		t.a[i]=num%pp[i];
		num/=pp[i];
	}
	return t;
}

int ppp[]={0,2,3,5,7};
Node count(int x,int y)
{
	int i,j;
	Node t;
	for(i=1;i<=4;i++)
	{
		t.a[i]=0;
		for(j=x;j<=y;j++)
		{
			t.a[i]=(t.a[i]*10+a[j])%ppp[i];
		}
	}
	return t;
}


Node add(Node t,Node tt)
{
	int i;
	Node ttt;
	for(i=1;i<=4;i++)
	{
		ttt.a[i]=(t.a[i]+tt.a[i])%ppp[i];
	}
	return ttt;
}

Node minus(Node t,Node tt)
{
	int i;
	Node ttt;
	for(i=1;i<=4;i++)
	{
		ttt.a[i]=(t.a[i]-tt.a[i]+ppp[i])%ppp[i];
	}
	return ttt;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int T1,T,i,j,k;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%s",&c[1]);
		len=strlen(&c[1]);
		for(i=1;i<=len;i++)
		{
			a[i]=c[i]-'0';
		}

		memset(f,0,sizeof(f));
		Node t;
		for(i=1;i<=len;i++)
		{
			t=count(1,i);
			f[i][encode(t)]=1;
		}

		for(i=1;i<=len-1;i++)
		{
			for(j=0;j<=2*3*5*7-1;j++)
			{
				for(k=i+1;k<=len;k++)
				{
					Node t=decode(j);
					Node tt=count(i+1,k);

					Node t1=add(t,tt);
					int num=encode(t1);
					f[k][num]+=f[i][j];

					Node t2=minus(t,tt);
					num=encode(t2);
					f[k][num]+=f[i][j];
				}
			}
		}

		int s[41];
		for(i=1;i<=len;i++)
		{
			s[i]=0;
			for(j=0;j<=2*3*5*7-1;j++)
			{
				s[i]+=f[i][j];
			}
		}

		__int64 ans=0;
		for(j=0;j<=2*3*5*7-1;j++)
		{
			Node t=decode(j);
			if(f[len][j]!=0 && (t.a[1]==0 || t.a[2]==0 || t.a[3]==0 || t.a[4]==0))
			{
				ans+=f[len][j];
			}
		}

		printf("Case #%d: %I64d\n",T1,ans);
	}
	return 0;
}