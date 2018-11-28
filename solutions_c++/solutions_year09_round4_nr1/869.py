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
#define VS vector<string>


bool isPos(VS a) {
    sort(a.begin(),a.end());
    for (int i=0;i<a.size();i++) for (int j=0;j<a.size()-1-i;j++) if (a[i][j]=='1') {  return false; }
    return true;
}

int num(VS a) {
    if (a.size()==1) return 0;
    VS b=a;
    for (int i=0;i<b.size();i++) { b[i]=a[i].substr(0,a[0].size()-1);}
    for (int i=0;i<a.size();i++) {
        bool ok=true;
        for (int j=0;j<a[0].size()-1;j++) if (a[i][j]=='1') ok=false;
        if (ok) {
            VS c;
            for (int k=0;k<a.size();k++) if (k!=i) c.PB(b[k]);
            if (isPos(c)) { return i+num(c);} 
        }

    }

}

void solve() {
    int r;
    cin>>r;
    VS a;
    for (int i=0;i<r;i++) {
        string s;
        cin>>s;
        reverse(s.begin(),s.end());
        a.PB(s);
    }
    cout<<num(a)<<endl;
    
    
}

int main() {
  int cases;
  cin>>cases;
  for (int t=0;t<cases;t++) {
    cout<<"Case #"<<t+1<<": ";
    solve();
  }
}
