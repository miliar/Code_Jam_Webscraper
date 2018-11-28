#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;
const int Maxn=51;
int T,N,K;
char a[Maxn][Maxn],b[Maxn][Maxn];
bool flagR,flagB;
void Init(){
     cin>>N>>K;
     for (int i=1;i<=N;++i)
     for (int j=1;j<=N;++j)
     cin>>a[i][j];
     for (int i=1;i<=N;i++)
     for (int j=1;j<=N;j++)
     b[j][N-i+1]=a[i][j];
     flagR=false;
     flagB=false;
}
void solve(){
     int i,j;
     for (i=N;i>=1;i--)
     for (j=1;j<=N;j++){
         int k=N;
         while (k>i && a[k][j]!='.') k--;
         if (i!=k){
            a[k][j]=a[i][j];
            a[i][j]='.';
         }
     }
     for (i=1;i<=N-K+1;i++)
     for (j=1;j<=N;j++)
     if (a[i][j]!='.'){
        bool flag=true;
        for (int k=i;k<i+K;k++)
        if (a[i][j]!=a[k][j]){
           flag=false;
           break;
        }
        if (flag){
           if (a[i][j]=='R') flagR=true;else
           flagB=true;
        }
     }
     
     for (i=1;i<=N;i++)
     for (j=1;j<=N-K+1;j++){
         
         if (a[i][j]!='.'){
            bool flag=true;
            for (int k=j;k<j+K;k++)
            if (a[i][j]!=a[i][k]){
               flag=false;
               break;
            }
            if (flag){
               if (a[i][j]=='R') flagR=true;else
               flagB=true;
            }
         }
     }
     for (i=1;i<=N-K+1;i++)
     for (j=1;j<=N-K+1;j++){
         if (a[i][j]!='.'){
            bool flag=true;
            for (int k=0;k<K;k++)
            if (a[i+k][j+k]!=a[i][j]){
               flag=false;
               break;
            }
            if (flag){
               if (a[i][j]=='R') flagR=true;else
               flagB=true;
            }
         }
     }
     
     for (i=N;i>=K;i--)
     for (j=1;j<=N-K+1;j++){
         if (a[i][j]!='.'){
            bool flag=true;
            for (int k=0;k<K;k++)
            if (a[i][j]!=a[i-k][j+k]){
               flag=false;
               break;
            }
            if (flag){
               if (a[i][j]=='R') flagR=true;else
               flagB=true;
            }
         }
     }
}
int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>T;
    for (int t=1;t<=T;t++){
        cout<<"Case #"<<t<<": ";
        Init();
        solve();
        for (int i=1;i<=N;i++)
        for (int j=1;j<=N;j++)
        a[i][j]=b[i][j];
        solve();
        if (flagR && flagB) cout<<"Both"<<endl;
        if ((! flagR) && (! flagB)) cout<<"Neither"<<endl;
        if ((flagR) && (!flagB)) cout<<"Red"<<endl;
        if ((flagB) && (!flagR)) cout<<"Blue"<<endl;
    }
    return 0;
}
