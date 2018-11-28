#include <iostream>
#define fi "A.INP"
#define fo "A.OUT"
const long maxn=100;
using namespace std;
long t,T,n;
int a[maxn][maxn];
double wp[maxn],owp[maxn],oowp[maxn];

double calc(long u,long v)
{
    long i,j,st,sm;
    st=0; sm=0;
    for (j=1; j<=n; j++){
        if (j==v) continue;
        if (a[u][j]!=2) sm++;
        if (a[u][j]==1) st++;
    }
    return (double(st)/sm);
}

void solve(){
    double st,sm;
    for (int i=1; i<=n; i++){
        st=0; sm=0;
        for (int j=1; j<=n; j++){
            if (a[i][j]!=2) (sm++);
            if (a[i][j]==1) (st++);
        }
        wp[i]=double(st)/sm;
    }

    for (int i=1; i<=n; i++){
        st=0; sm=0;
        for (int j=1; j<=n; j++){
            if (a[i][j] != 2) {sm++;} else continue;
            st=st+calc(j,i);
        }
        owp[i]=double(st)/sm;
    }

    for (int i=1; i<=n; i++){
        st=0; sm=0;
        for (int j=1; j<=n; j++){
           if (a[i][j] != 2) {sm++;} else continue;
            st=st+owp[j];
        }
        oowp[i]=double(st)/sm;
    }
    cout << "Case #" << t+1 << ":" << endl;
    for (int i=1; i<=n; i++)
    {
        //cout << double(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]) << endl;
        printf("%f\n",double(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]));
    }
}

int main()
{
   freopen(fi,"r",stdin);
   freopen(fo,"w",stdout);
   cin >> T; char s;
   for (t=0; t<T; t++){
        cin >> n;
        for (int i=1; i<=n; i++){
            for (int j=1; j<=n; j++){
                cin >> s;
                if (s=='.') {a[i][j]=2;} else
                if (s=='1') {a[i][j]=1;} else
                if (s=='0') {a[i][j]=0;}
            }
        }
        solve();
   }
}
