#include <cstdio>
#include <cstring>

#define Nmax 128
#define Lmax 128
#define Qmax 1024

int T,N,Q;
int i,j,t,best;

char S[Nmax][Lmax], s[Lmax];
int A[Qmax][Nmax];

inline int min(int a,int b) { return a<b?a:b; }

void dinamica()
{
 int m=0x3f3f3f3f;
 memset(A[i],0x3f3f3f3f,sizeof(A[i]));
 
 for (j=1; j<=N; ++j)
     m = min( m, A[i-1][j] );
 for (j=1; j<=N; ++j)
     if (strcmp(s,S[j]) == 0) continue;
        else A[i][j] = min( A[i-1][j], m+1 );          
}

int main()
{
 freopen("a.in","r",stdin);
 freopen("a.out","w",stdout);
 scanf("%d\n",&T);

 for (t=1; t<=T; ++t)
       {        
        //citeste numele motoarelor de cautare
        scanf("%d\n",&N);
        for (i=1;i<=N;++i)
             fgets( S[i], 200, stdin);
             
        //citeste queryurile     
        scanf("%d\n",&Q);
        for (i=1; i<=Q; ++i)
            {
             fgets( s, 200, stdin);
             dinamica();
            }
        for (j=1,best=0x3f3f3f3f; j<=N; ++j)
            best = min(best, A[Q][j]);
        //afisare
        printf("Case #%d: %d\n",t,best);
       }

 fclose(stdout);
 return 0;      
}
