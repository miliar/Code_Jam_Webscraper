#include <stdio.h>
#include <string.h>
char table[]={"welcome to code jam"},temp[509];
int count;
void fun(int x,int y)
{
	if(table[x]==0)
	{
		count++;
		return;
	}
	for(;temp[y]!=0;y++)
	{
		if(table[x]==temp[y])
		fun(x+1,y+1);
	}
}
int main()
{
	freopen("C-small-attempt3.in.txt","r",stdin);
	freopen("C-small-attempt3.out.txt","w",stdout);
	int Case,n;
	scanf("%d",&n);
	getchar();
	for(Case=1;Case<=n;Case++)
	{
		gets(temp);
		//printf("%s",temp);
		count=0;
		fun(0,0);
		printf("Case #%d: %04d\n",Case,count);
	}
	return 0;
}
