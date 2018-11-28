#include <stdafx.h>
#include <stdio.h>
#include <string>

using namespace std;

const long maxn=55;

struct elem
{
	long x;
	long y;
};

char a[maxn][maxn];
elem list[maxn*maxn];
long n,m,q,k,test,t,choice,cht;
bool fail;

void solve(long x,long y,char c)
{
	if ((x>n)||(y>m))
	{
		fail=true;
		return;
	}

	if (a[x][y]!='#')
	{
		fail=true;
		return;
	}

	a[x][y]=c;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%ld",&t);
	for (test=1;test<=t;test++)
	{
		scanf("%ld%ld\n",&n,&m);
		cht=0;
		for (q=1;q<=n;q++)
		{
			for (k=1;k<=m;k++)
			{
				scanf("%c",&a[q][k]);
				if (a[q][k]=='#')
				{
					cht++;
					list[cht].x=q;
					list[cht].y=k;
				}
			}
			scanf("\n");
		}


		char ch1='/';
		string s1="\\";
		char ch2=s1[0];
		fail=false;
		for (choice=1;choice<=cht;choice++)
			if (a[list[choice].x][list[choice].y]=='#')
			{
				solve(list[choice].x,list[choice].y,ch1);
				solve(list[choice].x,list[choice].y+1,ch2);
				solve(list[choice].x+1,list[choice].y,ch2);
				solve(list[choice].x+1,list[choice].y+1,ch1);
				if (fail==true)
					break;
			}

		printf("Case #%ld:\n",test);
		if (fail==true)
			printf("Impossible\n");
		else
			for (q=1;q<=n;q++)
			{
				for (k=1;k<=m;k++)
					printf("%c",a[q][k]);
				printf("\n");
			}
	}

}