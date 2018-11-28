#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define x first
#define y second
#define c first

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
            cout << "Case #" << t << ": ";
            int R;
            cin >> R;
            vector<vector<bool> > T(101,vector<bool>(101,0));
            int tot = 0;
            for(int k=0;k<R;k++){
                    int x1,x2,y1,y2;
                    cin >> x1 >> y1 >> x2 >> y2;
                    for(int i=min(x2,x1);i<=max(x1,x2);i++) for(int j=min(y2,y1);j<=max(y1,y2);j++) if(!T[i][j]){ tot++; T[i][j] = 1; }
            }
            
            int sol = 0;
            vector<vector<bool> > T2;
            while(tot > 0){
                      T2 = T;
                      for(int i=1;i<=100;i++){ for(int j=1;j<=100;j++){
                              if(T[i][j] == 1 && !T[i-1][j] && !T[i][j-1]){ tot--; T2[i][j] = 0; }
                              else if(T[i][j] == 0 && T[i-1][j] && T[i][j-1]){ tot++; T2[i][j] = 1; }
                      } }
                      T = T2;
                      sol++;
            }
            cout << sol << endl;
    }
}



