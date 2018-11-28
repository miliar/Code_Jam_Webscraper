#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <set>
using namespace std;

int main() {
    int T;
    cin>>T;
    for(int i = 1; i <= T; ++i) {
        int N,M;        
        cin>>N>>M;
        vector<string> E(N);
        for(int a = 0; a < N; ++a) cin>>E[a];
        vector<string> R(M);
        for(int a = 0; a < M; ++a) cin>>R[a];

        set<string> dirs;
        dirs.insert("/");

        for(int a = 0; a < E.size(); ++a) {
        	string cum = "";
            for(int b = 0; b < E[a].size(); ++b) {
                cum += E[a][b];
                if(E[a][b] == '/') {
                    dirs.insert(cum);
                }
            }
            cum += "/";
            dirs.insert(cum);
        }

        int sz = dirs.size();

        //for(set<string>::iterator it = dirs.begin(); it != dirs.end(); ++it) cout<<*it<<endl;

        //cout<<"Size: "<<sz<<endl;

        for(int a = 0; a < R.size(); ++a) {
        	string cum = "";
            for(int b = 0; b < R[a].size(); ++b) {
                cum += R[a][b];
                if(R[a][b] == '/') {
                    dirs.insert(cum);
                }
            }
            cum += "/";
            dirs.insert(cum);
        }

        //for(set<string>::iterator it = dirs.begin(); it != dirs.end(); ++it) cout<<*it<<endl;

        printf("Case #%d: %d\n",i,dirs.size() - sz);
    }
    return 0;
}
