#include <iostream>
#include <vector>
using namespace std;

bool graph[110][110], seen[110];
int matchL[110], matchR[110], n;
bool match(int u) {
   for(int v = 0; v < n; v++ ) if(graph[u][v]) {
      if(seen[v]) continue;
      seen[v] = true;
      if(matchR[v] < 0 || match(matchR[v] )) {
         matchL[u] = v;
         matchR[v] = u;
         return true;
      }
   }
   return false;
}
int main() {
    int cases;
    cin >> cases;
    vector<vector<int> > stocks;
    for(int cs=0; cs<cases; cs++) {
        int stockn, year; 
        cin >> stockn >> year;
        stocks.resize(stockn);

        for(int i=0; i<stockn; i++) {
            stocks[i].resize(year);
            for(int j=0; j<year; j++) cin >> stocks[i][j];
        }


        for(int i=0; i<stockn; i++) {
            for(int j=0; j<stockn; j++) {
                graph[i][j] = 1;
                for(int k=0; k<year; k++) if (stocks[i][k] >= stocks[j][k]) graph[i][j] = 0;
            }
        }

        n = stocks.size();
        memset(matchL,-1, sizeof(matchL));
        memset(matchR,-1, sizeof(matchR));
        int cnt = 0;
        for(int i = 0; i < n; i++)
        {
            memset(seen, 0, sizeof(seen));
            if(match(i)) cnt++;
        }
        cout << "Case #" << (cs+1) << ": "<< stocks.size() - cnt << endl;
    }
}
