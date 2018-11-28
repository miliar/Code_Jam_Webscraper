#include <iostream>
#include <cstdio>
#include <string>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")

using namespace std;

int par[10000];

int getRoot(int v){
  if (par[v] == v)
    return v;
    
  return par[v] = getRoot(par[v]);
}

void join(int v, int w){
  par[getRoot(v)] = getRoot(w);
}

int main(){
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests, H, W, n, g[100][100], r, c, f;
  cin >> tests;
  FOR (test, tests){
    cin >> H >> W;
    n = H * W;
    FOR (i, H)
      FOR (j, W){
        cin >> g[i][j];
        par[i * W + j] = i * W + j;
      }
      
    FOR (i, H)
      FOR (j, W){
        r = -1;
        f = g[i][j];
        
        // north
        if (i > 0 && g[i - 1][j] < f){
          r = i - 1;
          c = j;
          f = g[i - 1][j];
        }
        
        // west
        if (j > 0 && g[i][j - 1] < f){
          r = i;
          c = j - 1;
          f = g[i][j - 1];
        }

        // east
        if (j < W - 1 && g[i][j + 1] < f){
          r = i;
          c = j + 1;
          f = g[i][j + 1];
        }


        // south
        if (i < H - 1 && g[i + 1][j] < f){
          r = i + 1;
          c = j;
          f = g[i + 1][j];
        }
        
        if (r != -1)
          join(i * W + j, r * W + c);
      }
      
    char ret[W][H], mapped[W * H], ch = 'a';
    SET(mapped, 0);
    FOR (i, H)
      FOR (j, W)
        if (!mapped[getRoot(i * W + j)])
          mapped[getRoot(i * W + j)] = ch++;
          
    cout << "Case #" << (test + 1) << ":" << endl;
    FOR (i, H){
      FOR (j, W){
        cout << mapped[getRoot(i * W + j)];
        if (j < W - 1)
          cout << " ";
      }
      cout << endl;    
    }
    
  }
  return 0;
}
