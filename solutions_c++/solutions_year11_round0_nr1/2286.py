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

#include <cout.hpp>

int T;

int main() {
    cin >> T;
    rep(i, T){
        // => "------------------------------"
        int n;
        cin >> n;

        vector<char> r(n);
        vector<int> p(n);
        rep(j, n){
            cin >> r[j] >> p[j];
            p[j]--;
        }
        
        // => r | p
        
        int lentask=len(p);
        int cur=0;
        int turn=0;
        
        int orange_pos = 0, blue_pos = 0;
        while(cur != lentask){
            // => turn | "たーん"
            if(r[cur]=='O'){
                //オレンジさんはボタンまで移動してボタン押す
                // blueさんは次の自分担当ターンの位置まで移動
                int orange_used_turn = abs(p[cur]-orange_pos) + 1;
                // => orange_used_turn
                
                int next_blue_pos=-1;
                REP(i, cur+1, lentask){
                    if(r[i] == 'B'){
                        next_blue_pos = p[i];
                        break;
                    }
                }
                
                if(next_blue_pos != -1 && blue_pos != next_blue_pos){
                    // => "blueさんがうらで移動" | next_blue_pos | blue_pos | orange_used_turn
                    rep(t, orange_used_turn){
                        if(blue_pos < next_blue_pos){
                            blue_pos++;
                        }else if(blue_pos > next_blue_pos){
                            blue_pos--;
                        }
                    }
                }

                // orangeは目標にいるていで
                orange_pos = p[cur];
                turn += orange_used_turn;
                cur++;
                // => "現在ターン" | turn | cur | orange_pos | blue_pos
            }else{
                //blueさんはボタンまで移動してボタン押す
                // orangeさんは次の自分担当ターンの位置まで移動
                int blue_used_turn = abs(p[cur]-blue_pos) + 1;
                // => blue_used_turn
                
                int next_orange_pos=-1;
                REP(i, cur+1, lentask){
                    if(r[i] == 'O'){
                        next_orange_pos = p[i];
                        break;
                    }
                }
                
                if(next_orange_pos != -1 && orange_pos != next_orange_pos){
                    // => "orangeさんがうらで移動" | next_orange_pos | orange_pos | blue_used_turn
                    rep(t, blue_used_turn){
                        if(orange_pos < next_orange_pos){
                            orange_pos++;
                        }else if(orange_pos > next_orange_pos){
                            orange_pos--;
                        }
                    }
                }

                // blueは目標にいるていで
                blue_pos = p[cur];
                turn += blue_used_turn;
                cur++;
                // => "現在ターン" | turn | cur | orange_pos | blue_pos
            }
        }
        
        printf("Case #%d: %d\n", i+1, turn);
    }
    
    return 0;
}
