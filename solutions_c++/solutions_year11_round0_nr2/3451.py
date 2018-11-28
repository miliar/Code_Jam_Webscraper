#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef pair<char, char> PCC;

int main(){
    int T;
    cin >> T;
    for(int tc=1; tc <= T; tc++){
            int C;
            cin >> C;
            map<char, map<char, char> > t;
            for(int i=0;i<C;i++){
                    char a, b, c;
                    cin >> a >> b >> c;
                    t[a][b] = t[b][a] = c;
            }
            
            set<PCC> op;
            int D;
            cin >> D;
            for(int i=0;i<D;i++){
                    char a, b;
                    cin >> a >> b;
                    op.insert(PCC(a,b));
                    op.insert(PCC(b,a));
            }
            
            int N;
            string s;
            cin >> N >> s;
            vector<char> l;
            for(int i=0;i<N;i++){
                    l.push_back(s[i]);
                    bool comb = false;
                    while(l.size() > 1 && t.count(l[l.size()-1]) && t[l[l.size()-1]].count(l[l.size()-2]) ){
                          l[l.size()-2] = t[l[l.size()-1]][l[l.size()-2]];
                          l.resize(l.size()-1);
                          comb = true;
                    }
                    
                    if(!comb) for(int j=0;j<int(l.size())-1;j++){
                         if(op.count(PCC(l[l.size()-1], l[j]))) l.resize(0);
                    }
            }
            
            cout << "Case #" << tc << ": [";
            if(l.size() > 0) cout << l[0];
            for(int i=1;i<l.size();i++) cout << ", " << l[i];
            cout << "]" << endl;
    }
}
