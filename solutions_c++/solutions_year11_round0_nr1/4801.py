#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;

#include <windows.h>

#define REP(i,b,n) for(int i=b; i<n; i++)
#define rep(i,n)      REP(i, 0, n)

#if 0
cd "C:\Users\AAA\Documents\My Dropbox\Dev\src\cplus"
g++ gcj-abot-trust.cpp && (./a.exe 2> out.txt) < gcj-abot-trust.data

g++ gcj-abot-trust.cpp && ./a.exe  < gcj-abot-trust.data
(a.exe 2> stderr.txt) > stdout.txt
#endif

//template<typename T0, typename T1, typename T2> void pp_pair(T0<pair<T1, T2> > &a)
void pp_vpsi(const vector< pair<string, int> >& a)
{
    int n = a.size();
    rep(i,n)
        cout << "[" << i << "]<" << a[i].first << ", " << a[i].second << "> ";
    cout << endl;
}

void puts(const string mes)
{
    cout << mes << endl;
}

class Bots {
public:

inline int get_closure_next_pos(int now_pos, int aim_pos){
    if(now_pos == aim_pos){
        return now_pos;
    }

    if(now_pos < aim_pos){
        return (now_pos + 1);
    }else{
        return (now_pos - 1);
    }
}

int solve(const vector< pair<string, int> >& h){
    // 現在地
    int pos_o = 1;
    int pos_b = 1;
    // 個々のロボットが次に目指すべき目標
    int aim_o = 1;
    int aim_b = 1;
    //既に自分が押すべきボタンを全て押したか
    bool finished_o = false;
    bool finished_b = false;

    int cmd_idx_o = 0;
    int cmd_idx_b = 0;

    int time = 0;
    bool o_has_priority = (h[0].first == "O" ? true : false);
    
    // 初期目標の設定
    while(1){
        if(cmd_idx_o >= h.size()){
            finished_o = true;
            break;
        }
        if(h[cmd_idx_o].first == "O"){
            aim_o = h[cmd_idx_o].second;
            break;
        }
        cmd_idx_o++;
    }

    while(1){
        if(cmd_idx_b >= h.size()){
            finished_b = true;
            break;
        }
        if(h[cmd_idx_b].first == "B"){
            aim_b = h[cmd_idx_b].second;
            break;
        }
        cmd_idx_b++;
    }

//    LOOP_OUT:;
    while(1){
    LOOP_OUT :

        if(finished_o && finished_b){
            puts("--- Clear !");
            break;
        }

        time++;

        cout << "Turn " << time << endl;
        cout << "O: now " << pos_o << ", aim " << aim_o << endl;
        cout << "B: now " << pos_b << ", aim " << aim_b << endl;
        if(o_has_priority){
            cout << "o has priority." << endl;
        }else{
            cout << "b has priority." << endl;
        }
        
        bool o_pushed_this_turn = false;

        //もしも、まだ仕事が残っており、目標地点に到達していたら、次の目標を見つける
        if(o_has_priority && !finished_o && pos_o == aim_o){
            puts("o pushed button.");
            o_pushed_this_turn = true;
            while(1){
                cmd_idx_o++;
                if(cmd_idx_o >= h.size()){
                    finished_o = true;

                    o_has_priority = false;
                    cout << "o passed priority." << endl;

                    cout << "o fnished." << endl;
                    break;
                }

                if(h[cmd_idx_o].first == "O"){
                    aim_o = h[cmd_idx_o].second;
                    
                    // 優先権の譲渡
                    if(cmd_idx_o > cmd_idx_b){
                        o_has_priority = false;
                        cout << "o passed priority." << endl;
                    }
                    break;
                    // continue LOOP_OUT;
                    // goto LOOP_OUT;
                }
            }
        }else{
            if(!finished_o){
                pos_o = get_closure_next_pos(pos_o, aim_o);                
            }
        }

        // Bも同様に
        //もしも、まだ仕事が残っており、目標地点に到達していたら、次の目標を見つける
        if(!o_pushed_this_turn && !o_has_priority && !finished_b && pos_b == aim_b){
            puts("b pushed button.");
            while(1){
                cmd_idx_b++;
                if(cmd_idx_b >= h.size()){
                    finished_b = true;

                    o_has_priority = true;
                    cout << "b passed priority." << endl;

                    cout << "b fnished." << endl;
                    break;
                }

                if(h[cmd_idx_b].first == "B"){
                    aim_b = h[cmd_idx_b].second;

                    // 優先権の譲渡
                    if(cmd_idx_b > cmd_idx_o){
                        o_has_priority = true;
                        cout << "b passed priority." << endl;
                    }
                    break;
                    // goto LOOP_OUT;
                }
            }
        }else{
            if(!finished_b){
                pos_b = get_closure_next_pos(pos_b, aim_b);                
            }
        }

        //        if(!finished_o && pos_o == aim_o){
        //            // Can push the button and pushed.
        //        }

        // pos_o = get_closure_next_pos(pos_o, aim_o);
        // pos_b = get_closure_next_pos(pos_b, aim_b);

        cout << endl;

//        pp_vpsi(h);
//        Sleep(300);
    }

    return time;
    
    // cout << h[1].first;    
}

};





int main(){
    int n;
    int line = 1;

    int num_case_t;
    cin >> num_case_t;
    
    while(cin >> n){
        vector<pair<string, int> > h(n);

        rep(i, n){
            string r;
            int p;
            cin >> r >> p;
            h[i] = make_pair(r, p);
        }

        int sencods = Bots().solve(h);
        cerr << "Case #" << line << ": " << sencods << endl;
        line++;
    }

    return 0;
}


#if 0
#define pb push_back
#define mp make_pair

typedef complex<double> P;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;

template<typename T> void pp(T &a, int n)
{
    rep(i,n)
        cout << a[i] << " " ;
    cout << endl;
}
#endif

#if 0
//typedef std::vector<std::pair<std::string, int> > Vpsi;

//int solve(vector<void> & h){
//int solve(const vector<pair>& h){
//int solve(const vector<pair<string, int> >* h){
//int solve(Vpsi& h){
//    cout << h->pop_back().first;
//    cout << h->pop_back().first;
//    cout << h->operator[](1).first;


bool issame(vi &a,vi &b){
    rep(i,a.size())if( a[i] != b[i])return false;
    return true;
}

class RouteIntersection {
public:
    string isValid(int N, vector <int> coords, string moves) {
        map<int,int> M;
        rep(i,coords.size()){
            int index = M.size();
            if (M.find(coords[i]) == M.end())M[coords[i]]=index;
        }
        vector<vi> res;
        vi now;
        rep(i,coords.size()){
            now.pb(0);
        }

        res.pb(now);
        rep(i,coords.size()){
            int cur = M[coords[i]];
            if (moves[i] == '+')now[cur]++;
            else now[cur]--;
            res.pb(now);
        }

        rep(i,res.size()){
            //pp(res[i],res[i].size());
        }
        rep(i,res.size()){
            REP(j,i+1,res.size()){
                if (issame(res[i],res[j]))return "NOT VALID";
            }
        }

        return "VALID";
    }
};


int main(){

    int n;
    while(cin >> n){
        vector< pair<int, string> > h(n);

        for(int i = 0; i<n;i++){
            string s;cin >> s;
            int p,m;cin >> p >> m;
            int sum = 0;
            for(int j = 0;j<5;j++){
                int a;cin >>a;
                sum += a;
            }
            sum += (100 * p-50 *m);  
            h[i] = make_pair(sum, s);
        }

        sort(h.rbegin(), h.rend());
        cout << h[0].second <<endl;
    }

    return 0;
}
#endif

