#include <iostream>
#include <set>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std ;

int t,a,b;
int pots[10];

int digitos( int n )
{
	return (int)(log10(n*1.0)+1);
}

int calcula(int n)
{
	int dig=digitos(n);
	int resp=0;
	set<int> usd;
	int act,ini,num,base,obt;
	    
	    //printf("%d\n",n);
	    
	for(int j=0; j<=dig; j++)
	{
		act=n;
		ini=num=base=0;
		base++;
		while( ini<j && act!=0)
		{
			//printf("%d %d %d\n",ini,j,act);
			num+=base*(act%10);
			base*=10;
			act/=10;
			ini++;
		}
		ini++;
		obt=act+num*pots[dig-ini+1];
		if (obt>n && obt<= b) 
		{
			//printf("%d ",obt);
			if(usd.count(obt)==0)
				usd.insert(obt),resp++;
		}
	}
	//printf("\n");
	return resp;
}

int main()
{
	pots[0]=1;
	
	for( int i=1; i<=9;i++) pots[i]=10*pots[i-1];
	
	scanf("%d",&t);
	
	for( int i=1; i<=t; i++)
	{
		int resp=0;
		scanf("%d%d",&a,&b);
		for( int ii=a; ii<=b; ii++)
				resp+=calcula(ii);
			
		printf("Case #%d: %d\n",i,resp);
	}

	return 0;
}
