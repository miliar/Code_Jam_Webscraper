#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <complex>

using namespace std;

typedef complex<double> CDD;
const int MaxN=1000;
int T,N,M,A[MaxN][MaxN];
double Sum[MaxN][MaxN];
CDD SumD[MaxN][MaxN];
CDD D(int x,int y) {return A[x][y]*1.0*CDD(x,y);}
CDD Plot(int x1,int y1,int x2,int y2) {
    return (SumD[x2][y2]-SumD[x2][y1-1]-SumD[x1-1][y2]+SumD[x1-1][y1-1]-D(x1,y1)-D(x1,y2)-D(x2,y1)-D(x2,y2))
    /(Sum[x2][y2]-Sum[x2][y1-1]-Sum[x1-1][y2]+Sum[x1-1][y1-1]-A[x1][y1]-A[x1][y2]-A[x2][y1]-A[x2][y2]);
}
const double dd=1e-8;
bool operator ==(CDD A,CDD B) {
     return abs(A.real()-B.real())<dd && abs(A.imag()-B.imag())<dd;
}
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>T;
    for (int cnt=1;cnt<=T;++cnt) {
        scanf("%d%d%*d",&N,&M);
        for (int i=1;i<=N;++i)
            for (int j=1;j<=M;++j) {
                char ch;
                scanf(" %c",&ch);
                A[i][j]=ch-'0'+1;
            }
        for (int i=1;i<=N;++i)
            for (int j=1;j<=M;++j) {
                Sum[i][j]=Sum[i-1][j]+Sum[i][j-1]-Sum[i-1][j-1]+A[i][j];
                SumD[i][j]=SumD[i-1][j]+SumD[i][j-1]-SumD[i-1][j-1]+D(i,j);
            }
        bool flag=false;
        int ans;
        for (int k=min(N,M);k>=3;--k) {
            for (int i=1;i+k-1<=N;++i) {
                for (int j=1;j+k-1<=M;++j) 
                    if (Plot(i,j,i+k-1,j+k-1)==CDD((i+i+k-1)/2.0,(j+j+k-1)/2.0)) {flag=true;ans=k;break;}
                if (flag) break;
            }
            if (flag) break;
        }
        printf("Case #%d: ",cnt);
        if (!flag) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<"\n";
    }
    return 0;
}
