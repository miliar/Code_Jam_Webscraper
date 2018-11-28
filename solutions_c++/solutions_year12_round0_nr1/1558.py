//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl; 
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

char mapping[300];
string question,answer;
int main() {
  string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

  for(int i = 0; i < SZ(a); i++) {
    mapping[a[i]] = b[i];
  }
  mapping['q'] = 'z';
  mapping['z'] = 'q';

  // for(int i = 'a'; i <= 'z'; i++) {
  //   printf("%c -> ",i);
  //   if(mapping[i] == 0) {
  //     printf("missing\n");
  //   }
  //   else {
  //     printf("%c\n",mapping[i]);
  //   }
  // }
  int n;
  scanf("%d\n",&n);
  for(int i = 1; i <= n; i++) {
    getline(cin,question);
    answer = "";
    for(int j = 0; j < SZ(question); j++) {
      answer += mapping[question[j]];
    }
    cout << "Case #" << i << ": " << answer << endl;
  }
  
  
  return 0;
}
