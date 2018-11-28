#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
int base[26][26];
int opp[26][26];

int main(){
  int tt; cin >> tt;
  for(int caso = 1; caso <= tt; caso++){
    int c, d, n; 
    memset(base, -1, sizeof base);
    memset(opp, -1, sizeof opp);

    cin >> c;
    while(c--){
      char x, y, z; cin >> x >> y >> z;
      x -= 'A';
      y -= 'A';
      z -= 'A';
      base[x][y] = base[y][x] = z;
    }
    
    cin >> d;
    while(d--){
      char x, y; cin >> x >> y;
      x -= 'A';
      y -= 'A';
      opp[x][y] = opp[y][x] = 1;
    }

    cin >> n;
    char s[101];
    char t[101];
    scanf("%s", s);
    for(int i = 0; i < n; i++) s[i] -= 'A';
    int sz = 0;

    for(int i = 0; i < n; i++){
      t[sz++] = s[i];
      while(sz >= 2 && base[t[sz - 1]][t[sz - 2]] != -1){
          t[sz - 2] = base[t[sz - 1]][t[sz - 2]];
          sz--;
      }
      for(int i = 0; i + 1 < sz; i++)
          if(opp[t[i]][t[sz - 1]] != -1)
              sz = 0;
    }
    printf("Case #%d: ", caso);
    cout << "[";
    for(int i = 0; i < sz; i++){
      if(i) cout << ", ";
      cout << char('A' + t[i]);
    }
    cout << "]" << endl;
  }
}
