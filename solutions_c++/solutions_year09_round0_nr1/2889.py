#include <iostream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <algorithm>  
#include <sstream>  
#include <ctype.h>  
#include <string.h>  
#include <math.h>  
#include <stack>  
#include <set>  
#include <map>  
#define sz(a) int((a).size())   
#define pb push_back   
#define mp make_pair 
#define fo(i,n) for(i=0;i<n;i++)  
#define all(x) x.begin(),x.end()  
#define present(c,x) ((c).find(x) != (c).end())   
using namespace std;  
typedef long long ll;  
struct key{long x; bool operator <(const key &b) const { return x < b.x;}};  

int l, m, n, i, j, ans, len, k, u;
string words[10000], s;
bool c[100][100];

int main(void){
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    scanf("%d %d %d\n", &l, &m, &n);
    
    fo(i, m) cin >> words[i];
    
    fo(i, n){
          ans = 0;
          cin >> s;
          memset(c, 0, sizeof(c));
          len = s.length(); 
          k = j = 0;
          while(j < len){
                  if (isalpha(s[j])){
                     c[k][s[j] - 'a'] = 1;
                     k++;
                     j++;
                     continue;
                     }
                  for(u = j + 1; s[u] != ')' ;u++) c[k][s[u] - 'a'] = 1;
                  j = u + 1;
                  k++;
                  }
          fo(j, m){
                 bool ok = true;
                 fo(u, l)if (!c[u][words[j][u] - 'a']) {ok= false; break;}
                 if (ok) ans ++;
                 }
          printf("Case #%d: %d\n", i+1, ans);
          }
    }
