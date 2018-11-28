//Piotr Pakosz
//g++ 4.3.3

#include<cstdio>

int main()
{
	
	int t;
	scanf("%i",&t);
	for (int i = 1; i <= t; ++i)
	{
		int a,b;
		scanf("%i%i",&a,&b);
		//printf("%i %i",((1<<(a))-1)&b,((1<<(a))-1));
		if ( (((1<<(a))-1)&b) == ((1<<(a))-1))
			printf("Case #%i: ON\n",i);
		else printf("Case #%i: OFF\n",i);
	}
	return 0;
}