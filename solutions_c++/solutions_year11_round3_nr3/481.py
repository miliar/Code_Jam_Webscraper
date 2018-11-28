#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int ss[101];
int p, n, l, h, bingo;

bool calc(int x)
{
	int i, j;
	for(i=1;i<=n;i++)
	if(!(x%ss[i]==0 || ss[i]%x==0))return false;
	return true;
}

void work()
{
	int i,j,k;
	scanf("%d%d%d",&n,&l,&h);
	bingo=-1;
	for(i=1;i<=n;i++)
	  scanf("%d",&ss[i]);
	for(i=l;i<=h;i++)
		if(calc(i))
		{
			bingo=i;
			break;
		}
	printf("Case #%d: ",p);
	if(bingo==-1)
		printf("NO\n");
	else
		printf("%d\n",bingo);
}

int main()
{
	int T;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for(p=1;p<=T;p++)
		work();
	return 0;
}
