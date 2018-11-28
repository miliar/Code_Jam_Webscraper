#include<iostream>
#include<algorithm>

using namespace std;

const int maxN=600;

int data,N,M,A[maxN][maxN],F[maxN][maxN],S[maxN],ans;
int first[maxN][3],next[maxN][maxN][3];
int V[maxN][maxN],H[maxN][maxN];

int sum(int x,int y,int l) {
    int p=x+l-1;
    int q=y+l-1;
    return H[p][q]+H[x-1][y-1]-H[p][y-1]-H[x-1][q]; 
}

int main() {
    freopen("cs.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d\n",&data);
    for (int T=1; T<=data; T++) {
        printf("Case #%d: ",T);
        scanf("%d%d\n",&M,&N);
        memset(S,0,sizeof(S));
        memset(V,0,sizeof(V));
        memset(H,0,sizeof(H));
        memset(F,0,sizeof(F));
        memset(A,0,sizeof(A));
        ans=0;
        for (int i=1; i<=M; i++) {
            for (int j=1; j<=N/4; j++) {
                char c; int x;
                scanf("%c",&c);
                if ( '0'<=c && c<='9' ) x=c-'0'; else x=c-'A'+10; 
                for (int k=j*4; k>(j-1)*4; k--) {
                    A[i][k]=x&1; x/=2;
                }
            }
            scanf("\n");
        }
        //for (int i=1; i<=M; i++) {
        //    for (int j=1; j<=N; j++) printf("%d",A[i][j]); printf("\n");
        //}
        memset(first,0,sizeof(first));
        for (int i=M; i>0; i--)
            for (int j=N; j>0; j--) {
                if (A[i][j]!=A[i][j+1] && A[i][j]!=A[i+1][j] && A[i][j]==A[i+1][j+1])
                    F[i][j]=min(F[i+1][j+1],min(F[i][j+1],F[i+1][j]))+1;
                else F[i][j]=1;
                ans=max(F[i][j],ans);
                next[i][j][0]=first[F[i][j]][0];
                next[i][j][1]=first[F[i][j]][1];
                first[F[i][j]][0]=i;
                first[F[i][j]][1]=j;
                //printf("%d",F[i][j]);
                //if (j==N) printf("\n");
            }
        for (int i=1; i<=M; i++)
            for (int j=1; j<=N; j++) {
                H[i][j]=i*j;
                V[i][j]=1;
            }
    for (int len=ans; len>0; len--)
        for (int i=ans; i>=len; i--) {
            int p=first[i][0],q=first[i][1];
            while (p+q>0) {
                if (sum(p,q,len)==len*len) {
                    S[len]++;
                    for (int l=p; l<p+len; l++)
                        for (int r=q; r<q+len; r++) V[l][r]=0;
                    for (int l=1; l<=M; l++)
                        for (int r=1; r<=N; r++) H[l][r]=H[l-1][r]+H[l][r-1]-H[l-1][r-1]+V[l][r];
                }
                int x=next[p][q][0];
                int y=next[p][q][1];
                p=x; q=y;
            }
        }
        int ss=0;
        for (int i=1; i<=ans; i++) ss+=(S[i]>0);
        printf("%d\n",ss);
        for (int i=ans; i>0; i--) if (S[i]) printf("%d %d\n",i,S[i]);
            
    }
    return 0;
}
