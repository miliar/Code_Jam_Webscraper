#include <iostream>
#include <vector>
using namespace std;

int Ax[] = {0, -1, 1, 0};
int Ay[] = {-1, 0, 0, 1};

int n, m;
char lletra;
vector<vector<int> > v;
vector<vector<int> > g;
vector<vector<char> > sol;

void lol(int i, int j) {
   if (sol[i][j] != ' ')
      return;
   sol[i][j] = lletra;
   lol(i+Ay[g[i][j]], j+Ax[g[i][j]]);
   for (int k=0; k<4; ++k)
      if (i+Ay[k] >= 0 and i+Ay[k] < n and j+Ax[k] >= 0 and j+Ax[k] < m and Ay[k] + Ay[g[i+Ay[k]][j+Ax[k]]] == 0 and   Ax[k] + Ax[g[i+Ay[k]][j+Ax[k]]] == 0) {
         sol[i][j] = lletra;
         lol(i+Ay[k], j+Ax[k]);
      }
}

int main() {
   int t;
   cin >> t;
   for (int tt=1; tt<=t; ++tt) {
      cout << "Case #" << tt << ":" << endl;
      cin >> n >> m;
      lletra = 'a';
      v = vector<vector<int> >(n, vector<int>(m));
      g = vector<vector<int> >(n, vector<int>(m, -1));
      sol = vector<vector<char> >(n, vector<char>(m, ' '));
      for (int i=0; i<n; ++i)
         for (int j=0; j<m; ++j)
            cin >> v[i][j];
      for (int i=0; i<n; ++i)
         for (int j=0; j<m; ++j) {
            int minim = -1;
            int dir = -1;
            for (int k=0; k<4; ++k)
               if (i+Ay[k] >= 0 and i+Ay[k] < n and j+Ax[k] >= 0 and j+Ax[k] < m and (minim == -1 or v[i+Ay[k]][j+Ax[k]] < minim)) {
                  minim = v[i+Ay[k]][j+Ax[k]];
                  dir = k;
               }
            if (minim < v[i][j])
               g[i][j] = dir;
         }
      for (int i=0; i<n; ++i)
         for (int j=0; j<m; ++j)
            if (sol[i][j] == ' ') {
               lol(i, j);
               ++lletra;
            }
      for (int i=0; i<n; ++i) {
         cout << sol[i][0];
         for (int j=1; j<m; ++j)
            cout << ' ' << sol[i][j];
         cout << endl;
      }
   }
}