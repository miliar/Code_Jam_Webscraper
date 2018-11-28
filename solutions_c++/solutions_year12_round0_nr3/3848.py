#include <iostream>
#include <cmath>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define INPUT "B-small-attempt0.in"
#define OUTPUT "B-small-attempt0.out"
#define MAXN 10000000
using namespace std;
FILE *in,*out;
int A,B,N;
int use[MAXN+5];
int cevir(int a,int bas)
{
	a*=10;
	return a%bas + a/bas;
}
void solve()
{
	in =  fopen(INPUT,"r");
	out = fopen(OUTPUT,"w");
	fscanf(in,"%d",&N);
	int a,bas,i,j,k,uses=1,s=0;
	FOR(i,1,N)
	{
		fscanf(in,"%d %d",&A,&B);
		s = 0;
		FOR(j,A,B)
		{
			a = k = j;
			bas = 1;
			while(a)
			{
				a/=10;
				bas*=10;
			}
			a = j;
			while(a)
			{
				a/=10;
				k = cevir(k,bas);
				if(use[k] < uses && k > j && k<=B)
				{
					s++;
					use[k] = uses;
				}
			}
			uses++;
		}
		fprintf(out,"Case #%d: %d\n",i,s);
	}
}
int main()
{
	solve();
	return 0;
}


