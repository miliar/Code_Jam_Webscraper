#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
using namespace std;

int n;
string s;
map < pair<char,char> , char > com;
set < pair<char,char> > del;
vector <char> Q;

void solve(){
    Q.clear();
    int i,j;
    for (i=0;i<n;i++){
        #define sz Q.size()
        Q.push_back(s[i]);
        if (sz>=2){
            if (com.count(make_pair(Q[sz-1],Q[sz-2]))){
                char rep=com[make_pair(Q[sz-1],Q[sz-2])];
                Q.pop_back();
                Q.pop_back();
                Q.push_back(rep);
            }
        }
        for (j=0;j<sz-1;j++)
          if (del.count(make_pair(Q[j],Q[sz-1]))){
              Q.clear();
              break;
          }
    }
}

void output(){
    for (int i=0;i<sz;i++){
        if (i==0) cout << Q[i];
             else cout << ", " << Q[i];
    }
    cout << "]" << endl;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Tc;
    cin >> Tc;
    for (int T=1;T<=Tc;T++){
        cout << "Case #" << T << ": [";
        com.clear();
        del.clear();
        int c,d;
        cin >> c;
        for (int i=0;i<c;i++){
            char x,y,z;
            cin >> x >> y >> z;
            com[make_pair(x,y)]=z;
            com[make_pair(y,x)]=z;
        }
        cin >> d;
        for (int i=0;i<d;i++){
            char x,y;
            cin >> x >> y;
            del.insert(make_pair(x,y));
            del.insert(make_pair(y,x));
        }
        cin >> n;
        cin >> s;
        solve();
        output();
    }
}
