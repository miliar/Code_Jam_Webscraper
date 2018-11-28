#include<iostream>

int data,ans,N,k;
int A[100];
bool H[100];

int rank(int x) {
    for (int i=1; i<=k; i++) if (A[i]==x) return i;
    return 0;
}
bool check() {
    for (int i=k; i==k; i--) {
        int j=A[i];
        while (j!=1) {
            int k=rank(j);
            if (k==1) return 1;
            if (!k || !H[k]) return 0;
            j=k;
        }
    }
    for (int i=1; i<=k; i++) printf("%d ",A[i]); printf("\n");
    
    return 1;
}

void dfs(int x) {
    if (x==N) {
        H[x]=1;
        A[++k]=x;
        H[x]=0;
        ans+=check();
        k--;
    } else {
        dfs(x+1);
        A[++k]=x;
        H[x]=1;
        dfs(x+1);
        H[x]=0;
        k--;
    }
}

int main() {
    freopen("cs.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&data);
    for (int T=1; T<=data; T++) {
        printf("Case #%d: ",T);
        scanf("%d",&N);
        memset(H,0,sizeof(H));
        ans=k=0;
        dfs(2);
        printf("%d\n",ans%100003);
    }
    return 0;
}
