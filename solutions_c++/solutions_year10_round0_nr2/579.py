//Grzegorz Prusak: problem "Fair Warning" (GCJ 2010)
#include <cstdio>
#include <cstring>
#include <algorithm>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

struct BN
{
	BN(){}
	BN(const BN &a, const BN &b){ *this=a; *this-=b; }
	
	void clear(){ REP(i,SIZE) mem[i] = 0; }

	void scan()
	{
		char buffer[100]; scanf(" %s",buffer); int l = strlen(buffer), c = l;
		clear(); REP(i,l){ c--; mem[c/DIG] = 10*mem[c/DIG]+buffer[i]-'0'; }
	}
	
	void print()
	{
		int i = SIZE-1; while(i && !mem[i]) i--;
		printf("%d",mem[i]); while(i--) printf("%0*d",DIG,mem[i]);
	}

	operator bool(){ REP(i,SIZE) if(mem[i]) return 1; return 0; }

	bool operator<(const BN &b) const { FORD(i,SIZE-1,0) if(mem[i]!=b.mem[i]) return mem[i]<b.mem[i]; return 0; }

	BN & operator-=(const BN &b)
	{ int r=0; REP(i,SIZE){ r = BASE+mem[i]-b.mem[i]-r; mem[i] = r%BASE; r = r<BASE; } return *this; }

	BN twice() const { BN a; int r=0; REP(i,SIZE){ r += 2*mem[i]; a.mem[i] = r%BASE; r/=BASE; } return a; }

	BN & operator%=(const BN &b)
	{ if(*this<b) return *this; *this %= b.twice(); if(!(*this<b)) *this -= b; return *this; }

	enum { SIZE = 6, BASE = 1000000000, DIG = 9 };
	int mem[SIZE];
};

void gcd(BN &a, BN &b){ while(b){ a %= b; std::swap(a,b); } }

int main()
{
	int c; scanf("%d",&c); REP(x,c)
	{
		int n; scanf("%d",&n); BN A[n]; REP(i,n) A[i].scan(); std::sort(A,A+n);
		BN T(A[1],A[0]); REP(i,n-1){ BN b(A[i+1],A[i]); gcd(T,b); }
		BN y(T); A[0]%=T;
		if(A[0]) 
		y-=A[0]; 
		else y-=T; 
		printf("Case #%d: ",x+1); y.print(); puts("");
	}

	return 0;
}

