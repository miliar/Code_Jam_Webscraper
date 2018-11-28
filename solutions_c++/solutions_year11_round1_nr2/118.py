#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const double PI = acos(-1.0);

#define SZ size()
#define PB push_back
#define SORT(a) sort((a).begin(), (a).end())
#define REV(a) reverse((a).begin(), (a).end())
#define UNQ(a) (a).resize(unique((a).begin(), (a).end()) - (a).begin())
#define SUM(a) accumulate((a).begin(), (a).end(), 0)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(__typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define SQR(x) ((x) * (x))
#define EUCL(x1, y1, x2, y2) (((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2)))
#define MANH(x1, y1, x2, y2) (abs((x1) - (x2)) + abs((y1) - (y2)))
#define CROSS(x1, y1, x2, y2) ((x1) * (y2) - (y1) * (x2))
#define CROSS2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((y2) - (y0)) - ((y1) - (y0)) * ((x2) - (x0)))
#define DOT(x1, y1, x2, y2) ((x1) * (x2) + (y1) * (y2))
#define DOT2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((x2) - (x0)) + ((y1) - (y0)) * ((y2) - (y0)))
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }


string D[10005], L;
int N, M;

bool is[300], is2[10005][300];

string get(int ind)
{
    string res = "";
    FOR(i, 0, D[ind].SZ){
        res += (is[D[ind][i]] ? D[ind][i] : '_');
    }
    return res;
}

string solve()
{
    memset(is2, 0, sizeof(is2));
    for(char c = 'a'; c <= 'z'; c++){
        FOR(i, 0, N){
            is2[i][c] = 0;
            FOR(j, 0, D[i].SZ){
                if(D[i][j] == c){
                    is2[i][c] = 1;
                }
            }
        }
    }


    queue< pair< pair< vector<int>, int >, int > > Q;
    vector<int> v[11];
    FOR(i, 0, N){
        v[D[i].SZ].PB(i);
    }
    FOR(k, 1, 11){
        if(v[k].SZ > 0){
            Q.push(make_pair(make_pair(v[k], -1), 0));
        }
    }

    int best = -1, resInd;

    memset(is, 0, sizeof(is));
    //FOR(i, 0, 300) is[i] = 0;

    while(!Q.empty()){

        vector<int> S = Q.front().first.first;
        int ind = Q.front().first.second;
        int pts = Q.front().second;

        Q.pop();

        /*FOR(i, 0, S.SZ){
            cout << D[S[i]] << " ";
        }
        cout << pts << " " << L.substr(0, ind + 1) << endl;*/

        //if(S.SZ == 0) cout << endl << "!" << endl;

        if(S.SZ == 1){
            if(best < pts){
                best = pts;
                resInd = S[0];
            }
            else if(best == pts){
                resInd = min(resInd, S[0]);
            }
            continue;
        }

        ind++;

        bool ok = 0;

        FOR(i, 0, S.SZ){
            ok |= is2[S[i]][L[ind]];
            /*FOR(j, 0, D[S[i]].SZ){
                if(D[S[i]][j] == L[ind]){
                    ok = 1;
                }
            }*/
        }

        if(!ok){
            Q.push(make_pair(make_pair(S, ind), pts));
            continue;
        }

        //memset(is, 0, sizeof(is));
        //FOR(i, 0, ind + 1){
            is[L[ind]] = 1;
        //}

        vector< vector<int> > newS;
        map<string, int> whichS;
        int cnt = 0;

        FOR(i, 0, S.SZ){
            string tmp = get(S[i]);
            if(whichS.find(tmp) == whichS.end()){
                whichS[tmp] = cnt++;
                newS.PB(vector<int>());
            }
            newS[whichS[tmp]].PB(S[i]);
        }

        FOR(i, 0, newS.SZ){
            //string s = get(newS[i][0]);
            bool found = is2[newS[i][0]][L[ind]];
            /*FOR(j, 0, s.SZ){
                if(s[j] == L[ind]){
                    found = 1;
                    break;
                }
            }*/
            Q.push(make_pair(make_pair(newS[i], ind), pts + (int)(!found)));
        }

    }

    return D[resInd];
}

int main()
{
    freopen("B.large.in", "r", stdin);
    freopen("B.large.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    for(int testInd = 1; testInd <= testCnt; testInd++){
        cin >> N >> M;
        FOR(i, 0, N){
            cin >> D[i];
            //cout << D[i] << endl;
        }
        cout << "Case #" << testInd << ":";
        FOR(i, 0, M){
            cin >> L;
            //cout << " " << L << ": " << endl;
            //string k = solve();
            //cout << k << endl;
            cout << " " << solve();
        }
        cout << endl;
    }
}










