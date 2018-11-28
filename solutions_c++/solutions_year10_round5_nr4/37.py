#include<cstdio>
#include<iostream>

using namespace std;

const int p=1000000007;

int T,I=0;
int Calc[71][10000][71];
int opt[77][77][100];
int A[200][200],N[200];

int calc(int n,int sum,int ma){
    if (sum<0) return 0;
    int &ret=Calc[n][sum][ma];
    if (ret!=-1) return ret;
    if (n==0) return ret=(sum==0);
    if (ma==0) return ret=0;
    return ret=(calc(n-1,sum-ma,ma-1)+calc(n,sum,ma-1))%p;
}

int len,b;
int now[100];

int dp(int k,int n,int delta){
    int &ret=opt[k][n][delta];
    if (ret!=-1) return ret;
    if (k==len) return ret=(n==0 && delta==0);
    ret=0;
    for (int i=0;i<b;++i){
        int nnow=now[k]-(delta+i*b);
        int ndelta=(-nnow)/b;
        nnow+=ndelta*b;
        while (nnow<0){
            ndelta++;
            nnow+=b;
        }
        for (int zero=0;zero<2;++zero)
            for (int nn=zero;nn<=n;++nn){
                if (zero) ret=(ret+dp(k+1,nn,ndelta)*(long long)calc(n-zero,i*b+nnow,b-1)%p*(long long)nn*(long long)A[n-1][nn-1]%p)%p;
                else ret=(ret+dp(k+1,nn,ndelta)*(long long)calc(n-zero,i*b+nnow,b-1)%p*(long long)A[n][nn]%p)%p;
            }
    }
//    printf("%d %d %d %d\n",k,n,delta,ret);
    return ret;
}

int i,j;
long long n;

int main(){
    cin >> T;
    for (i=0;i<=100;++i)
        for (j=0;j<=i;++j)
            if (i==j || j==0) A[i][j]=1;
            else A[i][j]=(A[i-1][j]+A[i-1][j-1])%p;
    N[0]=1;
    for (i=1;i<=100;++i)
        N[i]=N[i-1]*(long long)i%p;
    for (i=0;i<=100;++i)
        for (j=0;j<=i;++j)
            A[i][j]=A[i][j]*(long long)N[j]%p;
    memset(Calc,-1,sizeof Calc);
    while (T--){
        cin >> n >> b;
        for (i=0;n;++i){
            now[i]=n%b;
            n/=b;
        }
        len=i;
        memset(opt,-1,sizeof opt);
        int ans=0;
        for (i=1;i<=b;++i)
            ans+=dp(0,i,0);
        cout << "Case #" << ++I << ": " << ans << endl;
    }
}
