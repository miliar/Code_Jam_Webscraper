#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;

int main() {
    
    vector< vector<string> > V;
    vector<string> S;
    int T,M,N;
    ifstream in("in.in");
    ofstream out("out.txt");
    in >> T;
    int n ,k;
    int f1;
    string cur,c;
    for(int i = 0; i < T; i++) {
        in >> N >> M;
        n = 0;
        for(int j = 0; j < N; j++) {
            in >> cur;
            f1 = 1; 
            c.clear();
            for(int k = 0; k < cur.size(); k++) {
                if (cur[k] == '/') {
                   f1 = 1;
                   if(c.size()) S.push_back(c);
                   c.clear();
                }
                else f1 = 0;
                if (!f1) c+=cur[k];
            } 
            S.push_back(c);
            V.push_back(S);
            S.clear();
        }

        for(int j = 0; j < M; j++) {
            in >> cur;
            f1 = 1; 
            c.clear();
            for(int k = 0; k < cur.size(); k++) {
                if (cur[k] == '/') {
                   f1 = 1;
                   if(c.size()) 
                        S.push_back(c);
                   c.clear();
                }
                else f1 = 0;
                if (!f1) c+=cur[k];
            } 
            S.push_back(c);
            k = 0;
            for(int j = 0; j < V.size(); j++) {
                for(int m = 0; m < (S.size() <? V[j].size()); m++) {
                    if (V[j][m] != S[m]) {
                        k >?= (m);
                        break;
                    }
                    if (m == S.size() - 1) {
                        k = S.size();
                        break;
                    }
                    if (m == V[j].size()-1) {
                        k >?= V[j].size();
                        break;
                    }
                }
            }     

            if (S.size() - k) V.push_back(S);
            n += S.size() - k;
            S.clear();
        }
        out<<"Case #"<<i+1<<": "<<n<<endl;
        V.clear();
    }
}
