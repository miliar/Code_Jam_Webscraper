#include <cstdio>
#include <sstream>
#include <iostream>
#include <string>
using namespace std;

const int maxn=5050;

string dict[maxn];
bool g[32][26];
int l, d, n;

int main() {
 freopen("a-large.in", "r", stdin);
 freopen("a-large.out", "w", stdout);
 cin>>l>>d>>n;
 for (int i=0; i<d; ++i)
  cin>>dict[i];
 for (int tc=1; tc<=n; ++tc) {
  string s; cin>>s;
  memset(g, 0, sizeof(g));

  int k=0;
  for (int i=0; i<s.size(); ++i)
   if (s[i]=='(') {
    int j=i+1;
    for (; s[j]!=')'; ++j)
     g[k][s[j]-'a']=true;
    i=j;
    k++;
   } else g[k++][s[i]-'a']=true;

  int res=0;
  for (int i=0; i<d; ++i) {
   int ok=1;
   for (int j=0; j<l; ++j)
    ok&=g[j][dict[i][j]-'a'];
   res+=ok;
  }
  printf("Case #%d: %d\n", tc, res);
 }

 return 0;
}
