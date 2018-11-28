#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>


using namespace std;

#define INF 2147483647
#define EL cout<<endl
#define TI freopen("test.inp","rt",stdin)
#define TO freopen("test.out","wt",stdout)


#define FOR(i,a,b) for(int i=a;i<=b;i++) 
#define FORD(i,a,b) for(int i=a;i>=b;i--) 
#define REP(i,n) for(int i=0;i<n;i++)

int INP;
#define BUFSIZE (1<<10)
char BUF[BUFSIZE+1], *inp=BUF;
#define GETCHAR(INP) {				\
	if(!*inp) {					\
		fread(BUF,1,BUFSIZE,stdin);	\
		inp=BUF;				\
	}						\
	INP=*inp++;					\
}
#define DIG(a) (((a)>='0')&&((a)<='9'))
#define GN(j) {					\
	GETCHAR(INP); while(!DIG(INP)) GETCHAR(INP);\
	j=INP-'0'; GETCHAR(INP);				\
	while(DIG(INP)){j=10*j+(INP-'0');GETCHAR(INP);}	\
}

int N,K,T;

void xuly()
{
     cin>>T;
     FOR(i,1,T)
     {
         cin>>N>>K;
         K%=(1<<N);
         if (K+1==(1<<N)) 
            cout<<"Case #"<<i<<": ON";
         else 
            cout<<"Case #"<<i<<": OFF";
         if (i<T) cout<<endl;
     }
}

#include <conio.h>
int main()
{
    TI;
    TO;
    xuly();
    getch();
    return 0;
}
