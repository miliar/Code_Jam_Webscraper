#include<stdio.h>
#include<string.h>


char x[5005],y[5005];
int len1,len2;

int Call( int i, int j)
{
	int res;
	if (i == len2)
		return 1;
	if ( j == len1)
		return 0;
	res = 0;
	if ( y[i] == x[j] )
		res += Call(i+1,j+1);
	res += Call(i, j+1);
	return res % 10000;
}

int main()
{
	int nCase,test,res;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.txt","w",stdout);
	scanf("%d\n",&nCase);
	strcpy(y,"welcome to code jam");
	len2 = strlen(y);
	for ( test = 1; test <= nCase; test ++)
	{
		gets(x);
		len1 = strlen(x);
		res = Call(0,0);
		printf("Case #%d: %04d\n",test,res%10000);
	}
	return 0;
}