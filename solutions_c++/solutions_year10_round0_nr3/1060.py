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

int R,K,N,G[2002],next[1001],dd[1001],q[1001],M,vt[1001],dung,T;
long long rs,sum,s[1001];

void xuly()
{
     cin>>T;
     FOR(t,1,T)
     {
         
         cin>>R>>K>>N;
         sum=0;dung=-1;
         FOR(i,1,N) 
         {
                    cin>>G[i];
                    G[i+N]=G[i];
                    sum+=G[i];

         }
         FOR(i,1,N) if (K<G[i]) { dung = i-1;  break;}

//         FOR(i,1,N) cout<<G[i]<<" ";EL;
//         cout<<K<<endl;
                  
         if (sum<=K) {cout<<"Case #"<<t<<": "<<(sum+0LL)*R<<endl; continue;}

         if (dung>=0) 
         {
                     rs=0;
                     FOR(i,1,min(dung,R))  rs+=G[i];
                     cout<<"Case #"<<t<<": "<<rs<<endl;
                     continue;
         }
          
         FOR(i,1,N)
         {
             int j=i-1;
             sum=0;
             while(sum<=K) {j++;sum+=G[j];}
             s[i]=sum-G[j];
    
             next[i]=j;         if (j>N) next[i]-=N;
         }
         
         FOR(i,1,N) dd[i]=0;
         int i=1,start;
         M=0;
         while(dd[i]==0)
         {
             dd[i]=1;
             q[++M]=i; 
             vt[i]=M;
             i=next[i];   
         }
         start=vt[i]; //vi tri bat dau cua cycle
         
//         FOR(i,1,M) cout<<q[i]<<" ";EL;         
//         cout<<start<<endl;
         
         rs=0;
         if (R<start) 
         {
              FOR(i,1,R) rs+=s[q[i]];
              cout<<"Case #"<<t<<": "<<rs<<endl;
              continue;
         }
         else
         {
              FORD(i,start-1,1) rs+=s[q[i]];
              R=R-start+1;
              sum=0;
              FOR(i,start,M) sum+=s[q[i]];
              rs+=((int)R/(M-start+1))*sum;
              R%=M-start+1;
              FOR(i,start,start+R-1) rs+=s[q[i]];
              
              cout<<"Case #"<<t<<": "<<rs<<endl;
              continue;
         }

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
