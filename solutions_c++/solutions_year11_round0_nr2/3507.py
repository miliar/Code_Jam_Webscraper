#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <utility>

using namespace std;
//using namespace __gnu_cxx;

typedef long long ll;
typedef double db;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef istringstream is;
typedef ostringstream os;

#define INF (1<<30)
#define INFLL (1LL<<61LL)
#define EPS (1e-9)
#define PB push_back
#define FI first
#define SE second
#define ALL(v) (v).begin(),(v).end()
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);--(i))
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();++(i))
#define FORE(i,a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define PRINT(v) for(int (i)=0;(i)<(int)(v).size();(i)++) cerr<<v[i]<<" "; cerr<<endl;

int ile[1000];

void run(int cnum){
    int C,D,N;
    cin >> C;
    string s;
    vs cvec;
    REP(i,C){
        cin >> s;
        cvec.PB(s);
    }

    cin >> D;
    vs opvec;
    REP(i,D){
        cin >> s;
        opvec.PB(s);
    }

    cin >> N >> s;
    FUP(i,'A','Z')
        ile[i] = 0;
    vector<char> res;
    REP(i,N){
        res.PB(s[i]);
        ile[s[i]]++;
        int siz = res.size();
        if(siz == 1) continue;
        char pop = res[siz-2];
        char ost = res[siz-1];

        char change = '-';
        REP(j,C){
            if((cvec[j][0] == pop && cvec[j][1] == ost) || (cvec[j][0] == ost && cvec[j][1] == pop)){
                change = cvec[j][2];
                break;
            }
        }
        if(change != '-'){
            ile[res.back()]--;
            res.pop_back();
            ile[res.back()]--;
            res.pop_back();
            res.PB(change);
            ile[change]++;
        } else {
            bool czysc = false;
            REP(j,D){
                if((opvec[j][0] == ost && ile[opvec[j][1]]) || (opvec[j][1] == ost && ile[opvec[j][0]])){
                    czysc = true;
                    break;
                }
            }
            if(czysc){
                res.clear();
                FUP(k,'A','Z')
                    ile[k] = 0;
            }
        }
    }
    cout << "Case #" << cnum << ": [";
    if(res.size())
        cout << res[0];
    FUP(j,1,(int)res.size()-1)
        cout << ", " << res[j];
    cout << "]\n";
}

int main(){
    ios::sync_with_stdio(0);
    int C;
    cin >> C;
    REP(i,C) run(i+1);
    return 0;
}

