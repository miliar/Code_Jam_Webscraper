#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<int>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

int main() {

int T; cin>>T;

for (int t=0;t<T;t++) {
    int R,C,D;
    cin>>R>>C>>D;
    vector<string> a;
    for (int i=0;i<R;i++) {string s; cin>>s; a.PB(s);}
    int ret=-1;
    for (int i=0;i+2<R;i++) for (int j=0;j+2<C;j++) for (int k=2;i+k<R&&j+k<C;k++) {
        double dx=0;
        double dy=0;
        for (int ii=0;ii<=k;ii++) for (int jj=0;jj<=k;jj++) {
            if (ii==0&&jj==0) continue;
            if (ii==0&&jj==k) continue;
            if (ii==k&&jj==k) continue;
            if (ii==k&&jj==0) continue;
            double x=(k+1)/2.0-ii-0.5;
            double y=(k+1)/2.0-jj-0.5;
            dx+=x*(D+(a[i+ii][j+jj]-'0'));
            dy+=y*(D+(a[i+ii][j+jj]-'0'));
        }
     //   cout<<i<<" "<<j<<" "<<k<<" -- "<<dx<<" "<<dy<<endl;
        if (abs(dx)<1e-9&&abs(dy)<1e-9&&k+1>=ret) ret=k+1;
    }
    if (ret==-1) cout<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;
    else cout<<"Case #"<<t+1<<": "<<ret<<endl;
}
    
}
