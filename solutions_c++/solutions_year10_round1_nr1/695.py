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

int T,N,K;
char a[100][100],b[100][100],c[100][100];
void xuly(int t)
{
     scanf("%d%d\n",&N,&K);
     FOR(i,1,N) 
     {
                FOR(j,1,N) scanf("%c",&a[i][j]);
                scanf("\n");
     }
//     FOR(i,1,N) {FOR(j,1,N) cout<<a[i][j];EL;}  EL;

     FOR(i,1,N)     FOR(j,1,N) 
       b[j][N-i+1]=a[i][j];//quay

//     FOR(i,1,N) {FOR(j,1,N) cout<<b[i][j];EL;}  EL;

     FOR(i,1,N) FOR(j,1,N) c[i][j]='.';

     FOR(j,1,N) //roi
     {
         int p=N;       
         FORD(i,N,1)
         if (b[i][j]!='.')
         {
             c[p][j]=b[i][j];         
             p--;    
         }
     }
     
//     FOR(i,1,N) {FOR(j,1,N) cout<<c[i][j];EL;}  EL;

     int cR=0,cB=0;
     FOR(i,1,N)
     FOR(j,1,N)
     if (c[i][j]!='.')
     {
         int ok=1;             
         if (j+K-1<=N)
         {
         FOR(k,1,K) 
            if (c[i][j]!=c[i][j+k-1]) ok=0;
         } else ok=0;
         
         int ok1=1;
         if (i+K-1<=N)
         {
         FOR(k,1,K) 
            if (c[i][j]!=c[i+k-1][j]) ok1=0;
         }
         else ok1=0;
         
         int ok2=1;
         if (i+K-1<=N && j+K-1<=N)
         {
         FOR(k,1,K)
            if (c[i][j]!=c[i+k-1][j+k-1]) ok2=0;
         }
         else ok2=0;
         
         int ok3=1;
         if (i+K-1<=N && j-K+1>=1) 
         {
            FOR(k,1,K)
            if (c[i][j]!=c[i+k-1][j-k+1]) ok3=0;
         }
         else ok3=0;
         
         if (ok1 || ok2 || ok3 || ok) if (c[i][j]=='R') cR=1; else cB=1;
     }
     
     if (cR==1 && cB==1) 
        cout<<"Case #"<<t<<": Both";
     else if (cR==0 && cB==0) cout<<"Case #"<<t<<": Neither";
     else if (cR==1 && cB==0) cout<<"Case #"<<t<<": Red";
     else if (cR==0 && cB==1) cout<<"Case #"<<t<<": Blue";
     
     if (t<T) cout<<endl;
}

#include <conio.h>
int main()
{
    TI;TO;
    cin>>T; 
    FOR(t,1,T) xuly(t);
//    getch();
    return 0;
}
