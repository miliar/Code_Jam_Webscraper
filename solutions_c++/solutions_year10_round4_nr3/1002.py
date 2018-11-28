#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>


using namespace std;

#define INF 2147483647
#define EL cout<<endl
#define TI freopen("test.inp","rt",stdin)


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

struct info {int x,y,t; };

#define MAX 200
char a[MAX+9][MAX+9],b[MAX+9][MAX+9],c[MAX+9][MAX+9];
int N,T,x1,x2,y1,y2,R,S;

void xuly(int t)
{
     scanf("%d",&N);
     memset(a,0,sizeof(a));
     R=S=0;
     FOR(i,1,N) 
     {
                scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
                FOR(p,y1,y2) FOR(q,x1,x2) a[p][q]=1;
                R=max(R,y2);S=max(S,x2);
     }
     
      
     int dem=0;
     while(1)
     {
         dem++;    
         memset(b,0,sizeof(b));
         memset(c,0,sizeof(c));    
         
//         FOR(i,1,R) {FOR(j,1,S) cout<<(int)a[i][j];EL;}EL;
         FOR(i,1,R) FOR(j,1,S) 
         {
             if (a[i][j] && a[i+1][j-1] && a[i+1][j]==0) b[i+1][j]=1;
             if (a[i][j] && a[i-1][j]+a[i][j-1]==0) c[i][j]=1;
         }
         R++;S++;         
         int cnt=0;
         
         FOR(i,1,R) FOR(j,1,S)
         {
             if (b[i][j] || a[i][j]) a[i][j]=1;
             if (c[i][j]) a[i][j]=0;
         }
         FOR(i,1,R) FOR(j,1,S) cnt+=a[i][j];

         if (cnt==0) 
         {
                     cout<<"Case #"<<t<<": "<<dem;
                     if (t<T) cout<<endl;
                     break;
         }
         
     }
}

#include <conio.h>
int main()
{
    TI;
    freopen("test.out","wt",stdout);
    cin>>T;
    FOR(t,1,T) xuly(t);
//    getch();
    return 0;
}
 
