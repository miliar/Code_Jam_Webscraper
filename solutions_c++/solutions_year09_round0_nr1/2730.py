#include <stdio.h>
#include <stdlib.h>
char temp[5002][17];
int l,d,n;
bool fun(char *a,char *b)
{
	int j=0;
	for(int i=0;a[i]!=0;i++)
	{
		if(b[j]=='(')
		{
			for(;b[j]!=0;j++)
			{
				if(a[i]==b[j])break;
				if(b[j]==')')goto haha;
			}
			while(b[j]!=')')j++;
			j++;
		}
		else if(a[i]==b[j])j++;
		else goto haha;
		
	}
	return true;
	haha:return false;
}
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	int Case=1,i,j;
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)scanf("%s",temp[i]);
	while(n--)
	{
		char t[1000];
		int sum=0;
		scanf("%s",t);
		for(i=0;i<d;i++)
		if(fun(temp[i],t))sum++;
		printf("Case #%d: %d\n",Case++,sum);
	}
	return 0;
}
