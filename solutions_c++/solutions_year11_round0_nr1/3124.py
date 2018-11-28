#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const string color[] = { "Orange", "Blue" };

int T, N, P, pos[2], idx[2];
char R;
vector<int> robot[2];
vector<int> order;

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        robot[0].clear(); 
        robot[1].clear();
        order.clear();
        
        cin >> N;
        for (int i = 1; i <= N; ++i) {
            cin >> R >> P;
            if (R == 'O') {
               robot[0].push_back(P);
               order.push_back(0);
            }
            else {
                 robot[1].push_back(P);
                 order.push_back(1);
            }
        }
    
        int cnt = 0;
        pos[0] = pos[1] = 1;
        idx[0] = idx[1] = 0;
        
        int sec = 0;
        
        while (cnt < N) {
              int cur = order[cnt++];
              
              int curpos = pos[cur];
              int tarpos = robot[cur][idx[cur]++];
              
              bool still = (idx[1 - cur] < robot[1 - cur].size());
              
              int other_curpos;
              int other_tarpos;
              
              if (still) {
                  other_curpos = pos[1 - cur];
                  other_tarpos = robot[1 - cur][idx[1 - cur]];
              }
    
              while (curpos != tarpos) {
                    ++sec;
                    
                    if (curpos < tarpos) ++curpos;
                    else --curpos;
                    
                    //cout << endl;
                    //cout << "Step " << sec << endl;
                    //cout << "Robot " << color[cur] << " moves to button " << curpos << endl;
                    
                    if (still) {
                       if (other_curpos < other_tarpos) ++other_curpos;
                       else if (other_curpos > other_tarpos) --other_curpos;
                       //cout << "Robot " << color[1 - cur] << " moves to button " << other_curpos << endl;
                    }
                    
              }
              
              ++sec;
              pos[cur] = tarpos;
              //cout << endl;
              //cout << "Step " << sec << endl;
              //cout << "Robot " << color[cur] << " pushes button " << tarpos << endl;
              if (still) {
                 if (other_curpos < other_tarpos) ++other_curpos;
                 else if (other_curpos > other_tarpos) --other_curpos;
                 //cout << "Robot " << color[1 - cur] << " moves to button " << other_curpos << endl;
                 pos[1 - cur] = other_curpos;
              }              
              
              //system("pause");
        }
        
        cout << "Case #" << t << ": " << sec << endl;
    }    
    
    return 0;
}
