#include <stdio.h>

long long N;
int PD, PG;

template<class T> inline T Abs(T t) {return t>0? t: -t;}
template<class T> inline T Gcd(T a,T b)
{if(a<0)return Gcd(-a,b);if(b<0)return Gcd(a,-b);return (b==0)?a:Gcd(b,a%b);}
template<class T> inline T Euclide(T a,T b,T &x,T &y)
  {if(a<0){T d=Euclide(-a,b,x,y);x=-x;return d;}
   if(b<0){T d=Euclide(a,-b,x,y);y=-y;return d;}
   if(b==0){x=1;y=0;return a;}else{T d=Euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}

bool Solve()
{
	if(PD > 0 && PG == 0)
		return false;
	if(PD == 0 && PG == 0)
		return true;
	if(PD < 100 && PG == 100)
		return false;
	if(PD == 100 && PG == 100)
		return true;
	for(long long i = 1; i <= N; i++){
		if(i*PD%100 == 0){
			if(PD == PG) return true;
			// test
			long long D = i;
			long long DWin = i*PD/100;
			long long GWin, G;
			long long a = -100, b = PG, c = (100*DWin-PG*D);
			long long nGcd = Gcd(-a,b);
			if(Abs(c)%nGcd) continue;
			Euclide(a,b,GWin,G);
			GWin = GWin*c/nGcd;
			G = G*c/nGcd;
			if(GWin < 0){
				long long k = (-GWin+b-1)/b;
				GWin += k*b;
				G -= k*a;
			}
			if(G < 0){
				a = -a;
				b = -b;
				long long k = (-G+a-1)/a;
				GWin -= k*b;
				G += k*a;
			}
			if(GWin >= 0 && GWin <= G)
				return true;
		}
	}
	return false;
}

int main()
{
	int nCase = 0;
	scanf("%d", &nCase);
	for(int i = 1; i <= nCase; i++){
		scanf("%lld %d %d", &N, &PD, &PG);
		if(Solve())
			printf("Case #%d: Possible\n", i);
		else
			printf("Case #%d: Broken\n", i);
	}
	return 0;
}

