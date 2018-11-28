#include <iostream>
#include <map>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

int H,W;

int tab[105][105];

bool in(int x, int y){
     return (x >= 0 && x < H && y >= 0 && y < W);
}

pair<int,int> go(int x, int y){
              vector<pair<int,int> > v;
              if (in(x-1,y)) v.push_back(make_pair(tab[x-1][y],0));
              if (in(x,y-1)) v.push_back(make_pair(tab[x][y-1],1));
              if (in(x,y+1)) v.push_back(make_pair(tab[x][y+1],2));
              if (in(x+1,y)) v.push_back(make_pair(tab[x+1][y],3));
              //for (int i=0; i< v.size(); i++) cout << "v de " << i << " = " << v[i].first << " " << v[i].second << endl;
              sort(v.begin(),v.end());
              if (v.size() == 0 || v[0].first >= tab[x][y]) return make_pair(x,y);
              else {
                   //cout << "(x,y) = " << x << " " << y << endl;
                   //cout << "second = " << v[0].second << endl;
                   if (v[0].second == 0) return go(x-1,y);
                   if (v[0].second == 1) return go(x,y-1);
                   if (v[0].second == 2) return go(x,y+1);
                   if (v[0].second == 3) return go(x+1,y);
              }
    
}

int main(){
    int nc; cin >> nc;
    for (int q = 1; q <= nc; q++){
        cin >> H >> W;
        memset(tab,0,sizeof(tab));
        for (int i = 0; i < H ;i++) for (int j = 0; j < W; j++) cin >> tab[i][j];
        pair<int,int> res[H][W];
        for (int i = 0; i < H ;i++) for (int j = 0; j < W; j++) res[i][j] = go(i,j);
        char alpha[H][W];
        map<pair<int,int>,int> M;
        int num = 0;
        /*for (int i = 0; i < H ;i++) for (int j = 0; j < W; j++){
            cout << res[i][j].first << " " << res[i][j].second << " " << i << " " << j << endl;
        }*/
        for (int i = 0; i < H ;i++) for (int j = 0; j < W; j++){
            if (M.find(res[i][j]) == M.end()){
               alpha[i][j] = 'a'+num;
               M[res[i][j]] = num;
               num++;
            }
            else alpha[i][j] = 'a' + M[res[i][j]];
        }
        cout << "Case #" << q << ":" << endl;
        for (int i= 0; i < H ;i++){
            for (int j = 0; j < W; j++){
                if (j !=0) cout << " ";
                cout << alpha[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
