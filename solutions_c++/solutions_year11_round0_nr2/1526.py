#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <iterator>

#define FOR(i,s,n) for((i)=(s);(i)<(int)(n);(i)++)
#define FORD(i,s,n) for((i)=(s);(i)>=(int)(n);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

using namespace std;

int run(int ncase){
    int i, j, k;
    int C, D, N;
    vector<string> comb;
    vector<string> opp;
    vector<int> opplist[2];
    string list;
    string ans;
    int skip;
    int pos;

    cin >> C;
    comb.resize(C);
    FOR(i, 0, C){
        cin >> comb[i];
        //cout << "C: " << comb[i] << endl;
    }

    cin >> D;
    opp.resize(D);
    opplist[0].resize(D);
    opplist[1].resize(D);
    FOR(i, 0, D){
        cin >> opp[i];
        opplist[0][i] = 0;
        opplist[1][i] = 0;
        //cout << "D: " << opp[i] << endl;
    }

    cin >> N;
    cin >> list;
    //cout << list << endl;

    string::iterator it;
    char pre = 0;
    foreach(list, it){
        char cmp;
        char cmp1, cmp2;
        char c = *it;

        skip = 0;

        FOR(i, 0, C){
            cmp1 = comb[i][0];
            cmp2 = comb[i][1];
            if(((c == cmp1) && (pre == cmp2)) ||
               ((c == cmp2) && (pre == cmp1)) ){
                skip = 1;
                pos = i;
                break;
            }
        }

        if(!skip){
            FOR(i, 0, D){


                FOR(j, 0, 2){
                    cmp = opp[i][j];
                    if(c != cmp) continue;

                    opplist[j][i]++;
                    if(opplist[!j][i] > 0)
                        skip = 1;
                }
            }
            if(skip){
                skip = 0;
                ans.clear();
                pre = 0;
                FOR(i, 0, D){
                    opplist[0][i] = 0;
                    opplist[1][i] = 0;
                }
                continue;
            }
        }


        if(skip){
            FOR(i, 0, D){
                FOR(j, 0, 2){
                    cmp  = opp[i][j];
                    if(pre != cmp) continue;
                    if(opplist[j][i] > 0)
                        opplist[j][i]--;
                }
            }
            ans[ans.size()-1] = comb[pos][2];
            pre = comb[pos][2];
            continue;
        }

        
        ans += c;
        pre = c;
    }

    

    cout << "Case #" << ncase << ": ";
    cout << "[";
    foreach(ans, itr){
        cout << *itr;
        if(*(itr+1))
            cout << ", ";
    }
    cout << "]" << endl;
    //cout << endl;
    return 0;
}

int main() {
    int i, test_set;
    cin >> test_set;
    //cin.ignore();
    FOR(i, 0, test_set) run(i+1);
    return 0;
}
