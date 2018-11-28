#include<iostream>
using namespace std;

int num[10],n;

void toDec ( int v )
{
	memset(num,0,sizeof(num));
	while ( v)
	{
		num[v%10]++;
		v/=10;
	}
}
bool check ( int v )
{
	int i,buf[10];
	for (  i=0 ; i<10 ; i++ )
		buf[i]=num[i];
	while ( v )
	{
		buf[v%10]--;
		if ( buf[v%10]<0 && v%10 )
			return false;
		v/=10;
	}
	for ( i=1 ; i<10 ; i++ )
		if(  buf[i] )
			return false;
	return true;
}

int main ()
{
	int cas,a,k;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cas);
	for ( k=1 ; k<=cas; k++ )
	{
		int i;
		scanf("%d",&a);
		toDec(a);
		for ( i=a+1 ; ; i++ )
		{
			if ( check(i)  )
			{
				
				break;
			}

		}
		printf("Case #%d: %d\n",k,i);

	}

}