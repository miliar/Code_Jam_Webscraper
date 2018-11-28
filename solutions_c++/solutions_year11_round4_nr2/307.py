#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
using namespace std;

long long a[555][555];
long long s[555][555];
long long wx[555][555], wy[555][555];

int main() {
    int T;
    cin>>T;
    for(int TT=1;TT<=T;TT++) {
        int n,m,dixie;
        cin>>n>>m>>dixie;
        for(int i=0;i<n;i++) for(int j=0;j<m;j++) {
            char x;
            cin>>x;
            a[i][j]=x-'0';
        }
        for(int i=0;i<=n;i++) for(int j=0;j<=m;j++) {
            if (i==0 || j==0) s[i][j]=0;
            else s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i-1][j-1];
            if (i==0 || j==0) wx[i][j]=0;
            else wx[i][j]=wx[i-1][j]+wx[i][j-1]-wx[i-1][j-1]+a[i-1][j-1]*(i-1);
            if (i==0 || j==0) wy[i][j]=0;
            else wy[i][j]=wy[i-1][j]+wy[i][j-1]-wy[i-1][j-1]+a[i-1][j-1]*(j-1);
        }

        int ans=0;
        for(int w=min(n,m);w>=3;w--) {
            for(int i=0;i+w<=n;i++) for(int j=0;j+w<=m;j++) {
                int iw=i+w-1, jw=j+w-1;
                long long ss=s[i+w][j+w]-s[i+w][j]-s[i][j+w]+s[i][j];
                ss=ss-a[i][j]-a[iw][j]-a[i][jw]-a[iw][jw];
                long long xs=wx[i+w][j+w]-wx[i+w][j]-wx[i][j+w]+wx[i][j];
                xs=xs-a[i][j]*i-a[iw][j]*iw-a[i][jw]*i-a[iw][jw]*iw;
                long long ys=wy[i+w][j+w]-wy[i+w][j]-wy[i][j+w]+wy[i][j];
                ys=ys-a[i][j]*j-a[iw][j]*j-a[i][jw]*jw-a[iw][jw]*jw;
                long long px=ss*(2*i+w-1);
                long long py=ss*(2*j+w-1);
                //cerr<<"w="<<w<<"  ss xs ys = "<<ss<<' '<<xs<<' '<<ys<<" @ ("<<i<<","<<j<<")"<<endl;
                if (px==2*xs && py==2*ys) {
                    //cerr<<"Found "<<w<<" @ ("<<i<<","<<j<<")"<<endl;
                    ans=w;
                    break;
                }
            }
            if (ans==w) break;
        }
        cout<<"Case #"<<TT<<": ";
        if (ans==0) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}
