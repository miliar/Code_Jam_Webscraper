#include <cstdio>
int N,D,G;

int gcd(int x,int y)
{
	return x?gcd(y%x,x):y;
}

inline void Readin()
{
	scanf("%d%d%d",&N,&D,&G);
}

inline void Solve()
{
	if (G==100 && D!=100)
		puts("Broken");
	else if (G==0 && D!=0)
		puts("Broken");
	else{
		int g= 100/gcd(100,D);
		if (N<g) puts("Broken");
		else puts("Possible");
	}
}

int main()
{
	//freopen("i.txt","r",stdin);
	int Test,Case=0;
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
