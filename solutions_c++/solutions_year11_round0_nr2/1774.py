#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
using namespace std;

map<pair<char,char>, char> comb;
map<char,char> ops;

void output(vector<char> el) {
    cout<<"[";
    if(!el.empty()) {
        for(int i=0; i<el.size()-1; ++i) cout<<el[i]<<", ";
        cout<<el.back()<<"]"<<endl;
    }else{
        cout<<"]"<<endl;
    }

}

int main() {
    int t,c,d,n;
    string s;
    cin>>t;
    for(int tc=1; tc<=t; ++tc) {
        comb.clear(); ops.clear();
        cin>>c;
        for(int i=0; i<c; ++i) {
            cin>>s;
            comb[make_pair(s[0],s[1])] = s[2];
            comb[make_pair(s[1],s[0])] = s[2];
        }

        cin>>d;
        for(int i=0; i<d; ++i) {
            cin>>s;
            ops[s[0]] = s[1];
            ops[s[1]] = s[0];
        }

        cin>>n;
        cin>>s;
        vector<char> el;
        for(int i=0; i<n; ++i) {
            if(el.empty()) {
                el.push_back(s[i]);
                continue;
            }

            if(comb.find(make_pair(el.back(),s[i])) != comb.end()) {
                char co = comb[make_pair(el.back(),s[i])];
                el.pop_back();
                el.push_back(co);
                continue;
            }

            if(ops.find(s[i]) != ops.end()) {
                char op = ops[s[i]];
                for(int i=0; i<el.size(); ++i) {
                    if(el[i] == op) {
                        el.clear();
                        goto NEXT;
                    }
                }
            }
            el.push_back(s[i]);
        NEXT:;
        }

        cout<<"Case #"<<tc<<": ";
        output(el);
    }
}
