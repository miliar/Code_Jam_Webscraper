#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define LL long long
#define gcd __gcd
using namespace std;

int main()
{
	int cases;
	LL N,Pd,Pg,G,D;
	
	scanf("%d",&cases);
	
	for(int iD=1;iD<=cases;iD++)
	{
		scanf("%lld %lld %lld",&N,&Pd,&Pg);
		bool ok;

		LL g1=gcd(100ll,Pd);
		LL g2=gcd(100ll,Pg);
		LL Dx=100/g1;
		LL Gx=100/g2;

		if(Dx>N) ok=false;
		else
		{
			// first multiple of Gx >=Dx
			LL G=(Gx*Dx)/gcd(Gx,Dx);
			LL W1=(Pd*Dx)/100;
			LL W2=(Pg*G)/100;
			G=G-(Dx-W1);	// max winnable games
			ok=(G>=W2);
		}

		if(Pg==0 && Pd!=0) ok=false;
		printf("Case #%d: %s\n",iD,ok?"Possible":"Broken");
	}

	return 0;
}

