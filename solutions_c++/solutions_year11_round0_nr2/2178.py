//0x
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
using namespace std;

#define CLR(a, n) memset((a), n, sizeof(a))
#define arlen(x) sizeof x / sizeof x[0]
#define len(a)  int((a).size())
#define all(x) (x).begin(), (x).end()
#define rall(c) (c).rbegin(), (c).rend()
#define has(s, val) (find(all(s), val)!=(s).end())
#define EXIST(s,e)  ((s).find(e)!=(s).end())
#define REMOVE(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define rep(i,n)  REP(i,0,n)
#define REP(i,a,b) for(int i=(a);i<(b);++i)
#define SORT(c) sort(all(c))
#define pb push_back
#define mp make_pair
const int INF=1<<29;
const double EPS=1e-9;
typedef std::vector<int> VI;
typedef std::vector<VI> VVI;
typedef std::vector<string> VS;
typedef long long ll;

// #include <cout.hpp>

int T, C, D, N;
map<pair<char, char>, char> combines;
map<pair<char, char>, bool> opposed;
string ans;

void combine(){
    int len = len(ans);
    char hit=combines[mp(ans[len-1], ans[len-2])];
    if(hit){
        ans = ans.substr(0, len-2)+hit;
        combine();
    }
}

int main() {
    cin >> T;
    rep(t, T){
        combines.clear(); opposed.clear();
        string tmp;
        cin >> C;
        rep(i, C){
            cin >> tmp;
            combines[mp(tmp[0], tmp[1])]=tmp[2];
            combines[mp(tmp[1], tmp[0])]=tmp[2];
        }
        cin >> D;
        rep(i, D){
            cin >> tmp;
            opposed[mp(tmp[0], tmp[1])]=true;
            opposed[mp(tmp[1], tmp[0])]=true;
        }

        // combines
        // opposed

        ans="";
        cin >> N;
        char c;
        string ans_pre;
        rep(i, N){
            cin >> c;
            // c
            if(ans == ""){
                ans = c;
            }else{
                ans += c;
                // ans
                ans_pre = ans;
                combine();
                // ans_pre | ans

                if(ans_pre == ans){
                    // ans
                    int len = len(ans);      
                    char las = ans[len-1];
                    int tarpos=-1;
                    //opposed check last --->
                    for(int l=len-2;l>=0;l--){
                        auto it = opposed.find(mp(ans[l], las));
                        if(it != opposed.end()){
                            // opposed
                            // "opposed!" | l
                            tarpos=l;
                            // break;
                        }
                    }
                    
                    
                    if(tarpos!=-1){
                        // ans.erase(tarpos);
                        ans = "";
                    }
                    // ans
                }
            }
        }

        // ans
        printf("Case #%d: [", t+1);
        rep(i, len(ans)){
            if(i>0){
                cout << ", ";
            }
            cout << ans[i];
        }
        puts("]");
    }
    return 0;
}
