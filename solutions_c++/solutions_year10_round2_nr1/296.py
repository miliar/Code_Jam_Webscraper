#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <string>
#include <sstream>

using namespace std;

vector<string> split(string &s){
   vector<string> VS;
   for (int i=0;i<s.size();i++){ if (s[i] == '/') s[i] = ' '; }
   istringstream iss(s);
   string t;
   while (iss >> t) VS.push_back(t);
   return VS;
}

int main(){
    int Nc; cin >> Nc;
    for (int qq = 1; qq <= Nc; qq++){
        int res = 0;
        set<vector<string> > have;
        int M,N; cin >> N >> M;
        for (int i=0;i<N;i++){
            string s; cin >> s;
            vector<string> vs = split(s);
            vector<string> curr;
            for (int j=0;j<vs.size();j++){
                curr.push_back(vs[j]);
                have.insert(curr);
            }
        }
        for (int i=0;i<M;i++){
            string s; cin >> s;
            vector<string> vs = split(s);
            vector<string> curr;
            for (int j=0;j<vs.size();j++){
                curr.push_back(vs[j]);
                if (have.find(curr) == have.end()){
                   have.insert(curr);
                   res++;
                }
            }
        }
        cout << "Case #" << qq << ": " << res << endl;
    }
    return 0;
}
