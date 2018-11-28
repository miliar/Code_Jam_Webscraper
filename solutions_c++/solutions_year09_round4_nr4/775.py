#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

//double PI =  3.14159265358979323846;
#define dd long double
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >
#define VD vector<dd >

dd vzd(dd x1,dd y1,dd x2,dd y2) {
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

void solve() {
    
    int n; cin>>n;
    VD x(n,0);
    VD y(n,0);
    VD r(n,0);
    for (int i=0;i<n;i++) cin>>x[i]>>y[i]>>r[i];
    if (n==1) { cout<<r[0]<<endl; return ;}
    if (n==2) { if (r[1]>r[0]) cout<<r[1]<<endl; else cout<<r[0]<<endl; return; }
    if (n==3) {
        VD p;
        p.PB(max(vzd(x[0],y[0],x[1],y[1])+r[0]+r[1],r[2]));
        p.PB(max(vzd(x[2],y[2],x[1],y[1])+r[2]+r[1],r[0]));
        
        p.PB(max(vzd(x[2],y[2],x[0],y[0])+r[2]+r[0],r[1]));
        sort(p.begin(),p.end());
        cout<<p[0]/2<<endl;
    }



    
    
}

int main() {
  int cases;
  cin>>cases;
  for (int t=0;t<cases;t++) {
    cout<<"Case #"<<t+1<<": ";
    solve();
  }
}
