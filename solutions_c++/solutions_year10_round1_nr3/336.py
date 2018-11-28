#include <stdio.h>

int A1,A2,B1,B2;

void swap(int &a,int &b)
{
	int t;
	t=a;a=b;b=t;
}

int count(int a,int b)
{
	if (a>b) swap(a,b);
	int cnt=0;
	while (a>0&&b/a==1)
	{
		cnt++;
		int t= a;
		a = b%a;
		b=t;
	}
	return cnt;
}

int main()
{
	freopen("d:\\C-small-attempt0.in","r",stdin);
	freopen("d:\\output.txt","w",stdout);
	int T;
	int t;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
		int a,b;
		int pos=0;
		for(a=A1;a<=A2;a++)
			for(b=B1;b<=B2;b++)
			{
				int cnt=count(a,b);
				if (cnt%2==0)
				pos++;
			}
		printf("Case #%d: %d\n",t,pos);
	}
	return 0;
}