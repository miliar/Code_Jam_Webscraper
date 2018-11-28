#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <fstream>
#include <sstream>
#include <utility>

using namespace std;

int N,NQ;

//Directions:
//              1
//            8   2
//          7      3
//           6   4
//             5  

int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};

struct S {
      pair<int,int> first;
      pair<int,string> second;
      bool operator()(const S &x, const S &y) const {
           if (x.second.second.size() < y.second.second.size()) return false;
           if (x.second.second.size() > y.second.second.size()) return true;
           return (x.second.second > y.second.second);
      }
};

map<int,string> puedo[20][20];
int target;

bool in(int x,int y){
     if (x>=0 && y>=0 && x<N && y<N) return true;
     return false;
}

//devuelve cierto si a < b
bool menor(string& a, string& b){
     if (a.size() < b.size()) return true;
     if (a.size() > b.size()) return false;
     return a < b;
}

int main(){
    int nc; cin >> nc;
    for (int cas = 1; cas <= nc; cas++){
        cerr << "cas = " << cas << endl;
        cout << "Case #" << cas << ":" << endl;
        cin >> N >> NQ;
        char tab[N][N];
        for (int i=0;i<20;i++) for (int j=0;j<20;j++) puedo[i][j].clear();
        for (int i=0; i< N;i++) for (int j=0;j<N;j++) cin >> tab[i][j];
        // (posicion, target+string)
        priority_queue<S,vector<S>, S > Q;
        for (int i=0;i<N;i++) for (int j=0;j<N;j++){
            if (tab[i][j] >='0' && tab[i][j] <='9'){
               string unchar = ""; 
               unchar += tab[i][j];
               puedo[i][j][tab[i][j]-'0'] = unchar;
               S s;
               s.first = make_pair(i,j);
               s.second = make_pair((int)(tab[i][j]-'0'), unchar);
               Q.push(s); 
            }
        }
        while (!Q.empty()){
              pair<int,int> pos = Q.top().first;
              pair<int,string> state = Q.top().second;
              //cerr << "cojo el " << state.second << " " << state.first << " de las casillas ";
              //cerr << pos.first << " " << pos.second << endl;
              Q.pop();
              for (int mov1 = 0; mov1 < 4; mov1++){
                  if (!in(pos.first+dx[mov1],pos.second+dy[mov1])) continue;
                  for (int mov2 = 0; mov2 < 4; mov2++){
                      if (!in(pos.first+dx[mov1]+dx[mov2],pos.second+dy[mov1]+dy[mov2])) continue;
                      //cout << "mov1 = " << mov1 << " mov2 = " << mov2 << endl;
                      pair<int,string> new_state = state;
                      if (tab[pos.first+dx[mov1]][pos.second+dy[mov1]] == '+'){
                           //cout << "Caso +" << endl;
                         new_state.first+=(int)(tab[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]]-'0');
                         new_state.second+=(char)'+';
                         new_state.second+= (char)tab[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]];
                         if (abs(new_state.first) > 500) continue;
                         if (puedo[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]].find(new_state.first) == puedo[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]].end()
                         or menor(new_state.second,puedo[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]][new_state.first])){
                            puedo[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]][new_state.first] = new_state.second;
                            S s;
                            s.first = make_pair(pos.first+dx[mov1]+dx[mov2],pos.second+dy[mov1]+dy[mov2]);
                            s.second = new_state;
                            Q.push(s);
                            //cout << "echo el "
                            //<< new_state.second << " " << new_state.first << " en las casillas " << pos.first+dx[mov1]+dx[mov2]
                            //<< " " << pos.second+dy[mov1]+dy[mov2] << endl;
                         }
                      }
                      else if (tab[pos.first+dx[mov1]][pos.second+dy[mov1]] == '-'){
                           //cout << "Caso -" << endl;
                         new_state.first-=(int)(tab[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]]-'0');
                         new_state.second+=(char)'-';
                         new_state.second+= (char)tab[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]];
                         if (abs(new_state.first) > 500) continue;
                         if (puedo[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]].find(new_state.first) == puedo[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]].end()
                         or menor(new_state.second,puedo[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]][new_state.first])){
                            puedo[pos.first+dx[mov1]+dx[mov2]][pos.second+dy[mov1]+dy[mov2]][new_state.first] = new_state.second;
                            S s;
                            s.first = make_pair(pos.first+dx[mov1]+dx[mov2],pos.second+dy[mov1]+dy[mov2]);
                            s.second = new_state;
                            Q.push(s);
                            //cout << "echo el "
                            //<< new_state.second << " " << new_state.first << " en las casillas " << pos.first+dx[mov1]+dx[mov2]
                            //<< " " << pos.second+dy[mov1]+dy[mov2] << endl;
                         }
                      }
                      else cout << "JORRLRLRLRLL!!" << endl;
                  }
              }
        }
        //
        for (int Query=0;Query<NQ;Query++){
            cin >> target;
            string res = "";
            for (int i=0;i<N;i++) for (int j=0;j<N;j++){
                if (puedo[i][j].find(target) != puedo[i][j].end()){
                   if (res == "" or menor(puedo[i][j][target],res)){
                      res = puedo[i][j][target];
                   }
                }
            }
            cout << res << endl;
        }
    }
    return 0;
}
