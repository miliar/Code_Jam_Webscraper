#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <queue>
using namespace std;

int n,l,h;

void solve() {
    cin>>n>>l>>h;
    vector<int> dogs(n);
    for(int i=0;i<n;i++) cin>>dogs[i];  //i dogs?
    int ret=-1;
    for(int i=l;i<=h;i++) {
        bool ok=true;
        for(int j=0;j<n;j++) if(!((i%dogs[j]==0)||(dogs[j]%i==0))) {ok=false; break;}
        if(ok) {
            cout<<i<<endl;
            return;
        }
    }
    cout<<"NO"<<endl;
}

int main() {
    int cases;
    cin>>cases;
    for(int cnum=1;cnum<=cases;cnum++) {
        cout<<"Case #"<<cnum<<": ";
        solve();
    }
}
