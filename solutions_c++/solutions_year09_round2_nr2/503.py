#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")

using namespace std;

int main(){
  freopen("B.out","wt", stdout);
  freopen("B.in","r", stdin);
  int tests;
  scanf("%d", &tests);
  int ret;
  FOR (test, tests){
    string val;
    cin >> val;
    int digs[10], vv[val.sz];
    SET(digs, 0);
    FOR (i, val.sz){
      vv[i] = val[i] - '0';
      digs[vv[i]]++;
    }
      
    int idx = val.sz - 1, mm = 0;
    while (idx > -1){
      if (vv[idx] < mm) // we can change this part
        break;
        
      mm >?= vv[idx];
      idx--;
    }
    
    cout << "Case #" << (test + 1) << ": ";
    if (idx == -1){
      digs[0]++;
      idx = 1;
      while (!digs[idx])
        idx++;
        
      cout << idx;
      digs[idx]--;
    }
    else{
      FOR (i, idx){
        cout << val[i];
        digs[vv[i]]--;
      }
      int fg = 100;
      ffor (i, idx, val.sz)
        if (vv[i] > vv[idx] && vv[i] < fg)
          fg = vv[i];
          
      cout << fg;
      digs[fg]--;
    }
    
      FOR (i, 10)
        while (digs[i]){
          cout << i;
          digs[i]--;
        }      

    cout << endl;
  }

  return 0;
}
