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

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int L, D, N;
  cin >> L >> D >> N;
  string word[D];
  FOR (i, D)
    cin >> word[i];
   
  string pat; 
  bool ok[D], cont[26];
  int ret, idx;
  FOR (i, N){
    cin >> pat;
    FOR (j, D)
      ok[j] = true;
    idx = 0;
    FOR (j, L){
      SET(cont, 0);
      if (pat[idx] == '('){
        idx++;
        while (pat[idx] != ')'){
          cont[pat[idx] - 'a'] = true;
          idx++;
        }
      }
      else
        cont[pat[idx] - 'a'] = true;
        
      idx++;
      
      FOR (k, D)
        ok[k] &= cont[word[k][j] - 'a'];
    }
    
    ret = 0;
    FOR (j, D)
      ret += ok[j];
      
    cout << "Case #" << (i + 1) << ": " << ret << endl;
  }
  return 0;
}
