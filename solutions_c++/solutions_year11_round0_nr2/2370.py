#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <utility>
using namespace std;

map<char,map<char,char> > combine;
map<char,set<char> > opposed;

void result(int t, vector<char> V) {
    cout<<"Case #"<<(t+1)<<": [";
    for(int i = 0; i < (int)V.size() - 1; ++i) {
        cout<<V[i]<<", ";
    }
    if(!V.empty()) cout<<V.back();
    cout<<"]"<<endl;
}

int main() {
	int T;
	cin>>T;
	for(int t = 0; t < T; ++t) {
		opposed.clear();
		combine.clear();

        int C;
        cin>>C;
        string s;
        for(int c = 0; c < C; ++c) {
            cin>>s;
            combine[s[0]][s[1]] = s[2];
            combine[s[1]][s[0]] = s[2];
        }

        int D;
        cin>>D;
        for(int d = 0; d < D; ++d) {
            cin>>s;
            opposed[s[0]].insert(s[1]);
            opposed[s[1]].insert(s[0]);
        }


        int N;
        cin>>N;
        string S;
        cin>>S;

        vector<char> V;
        set<char> cur;

        for(int s = 0; s < (int)S.size(); ++s) {
            if(V.size() == 0) {
                V.push_back(S[s]);
                cur.insert(S[s]);
            } else {
                if(combine[S[s]].count(V.back())) {
                    V.back() = combine[S[s]][V.back()];
                    cur.clear();
                    for(int i = 0; i < (int)V.size(); ++i) {
                        cur.insert(V[i]);
                    }
                    continue;
                }

                bool no = false;
                set<char>::iterator it;
                for(it = opposed[S[s]].begin(); it != opposed[S[s]].end(); ++it) {
                    if(cur.count(*it)) {
                        cur.clear();
                        V.clear();
                        no = true;
                        break;
                    }
                }
                 
                if(!no) {
                	V.push_back(S[s]);
                    cur.insert(S[s]);
                }
            }
        }
        result(t,V);
    }
    return 0;
}
