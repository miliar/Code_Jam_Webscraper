#include <iostream>
#include <vector>
#include <set>
#include <string>
using namespace std;

bool eq(set<char> F, string a, string b) {
    if(a.size() != b.size()) return false;
    for(int i = 0; i < (int)a.size(); ++i) {
        if(a[i] == 0) {
            if(F.count(b[i])) return false;    
        } else if(a[i] != b[i]) return false;
    }
    return true;
}

bool ok(char ch, const vector<string>& P) {
    for(int i = 0; i < (int)P.size(); ++i) {
        for(int j = 0; j < (int)P[i].size(); ++j) {
            if(P[i][j] == ch) return true;
        }
    }
    return false;
}

void printer(string a) {
    for(int i = 0; i < (int)a.size(); ++i) {
        if(a[i]==0) cout<<0;
        else cout<<a[i];
    }
}

vector<string> getnew(string cur, set<char> F, vector<string> P) {
    vector<string> R;
    for(int i = 0; i < (int)P.size(); ++i) {
        if(eq(F,cur,P[i])) {
            /*
            cout<<"Accepted: ";
            printer(cur);
            cout<<" "<<P[i]<<endl;
            cout<<"In set: {";
            for(set<char>::iterator it = F.begin(); it!=F.end(); ++it) {
                cout<<*it<<", ";
            }
            cout<<"}"<<endl;
            */
            R.push_back(P[i]);
        } else {
            /*
            cout<<"Failed: ";
            printer(cur);
            cout<<" "<<P[i]<<endl;
            cout<<"In set: {";
            for(set<char>::iterator it = F.begin(); it!=F.end(); ++it) {
                cout<<*it<<", ";
            }
            cout<<"}"<<endl;
            */
        }
    }
    return R;
}

int simulate(const vector<string>& V, string o, string c) {
    //cout<<"SIMULATING"<<endl;
    //cout<<"WORD: "<<c<<endl;
    vector<string> P;
    string cur;
    cur.resize(c.size());

    int fail = 0;
    int ind = 0;

    for(int i = 0; i < (int)V.size(); ++i) {
        if(V[i].size() == c.size()) P.push_back(V[i]);
    }

    set<char> F;

    while(true) {
        //printer(cur);
        /*
        cout<<"Remaining: {";
        for(int i = 0; i < (int)P.size(); ++i) {
            if(i != (int)P.size() - 1) {
                cout<<P[i]<<", ";
            } else cout<<P[i]<<"}"<<endl;
        }
        cout<<ind<<endl;
        printer(cur);
        */
        F.insert(o[ind]);
        if(!ok(o[ind],P)) {
            //cout<<"moro"<<endl;
            ++ind;
            continue;
        }

        string prev = cur;
        for(int i = 0; i < (int)cur.size(); ++i) {
            if(c[i] == o[ind]) cur[i] = c[i];
        }

        if(prev == cur) {
            ++fail;   
        }

        P = getnew(cur,F,P);
        /*
        vector<string> N;
        for(int i = 0; i < (int)P.size(); ++i) {
            if(eq(cur,P[i])) N.push_back(P[i]);
        }

        P = N;
        */

        bool br = true;

        for(int i = 0; i < (int)cur.size(); ++i) {
            if(cur[i] == 0) br = false;
        }

        ++ind;

        if(br) break;
        if(P.size() <= 1) break;
    }

    return fail;
}

int main() {
    int T;
    cin>>T;
    for(int i = 1; i <= T; ++i) {
        int N,M;
        cin>>N>>M;
        vector<string> V(N);
        for(int j = 0; j < N; ++j) cin>>V[j];
        vector<string> L(M);
        for(int j = 0; j < M; ++j) cin>>L[j];

        cout<<"Case #"<<i<<": ";
        for(int j = 0; j < M; ++j) {
            int best = -1;
            int bi = -1;
            for(int k = 0; k < N; ++k) {
                int val = simulate(V,L[j],V[k]);
                //cout<<V[k]<<" FAIL: "<<val<<endl;
                if(val > best) {
                    best = val;
                    bi = k;
                }
            }

            //cout<<"BESTFAIL: "<<best<<endl;

            string word = V[bi];

            if(j != M - 1) {
                cout<<word<<" ";
            } else {
                cout<<word<<endl;
            }
        }
    }
    return 0;
}
