#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define PRUSH(stream, format, args...) do { fprintf(stream, format, ## args); fflush(stream); } while (0)
#define DEBUG(format, args...) do { PRUSH(stderr, format, ## args); } while (0)
#define PRINT(format, args...) do { PRUSH(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

#define FST first
#define SND second

const int MOD=10009;

char pl[108];
char bf[108];
int sm[108];
int ch[108][26];

int main() {
  int i, j, d, w, D, W, t, z, Z, b;
  scanf("%d", &Z);
  for (z=1; z<=Z; z++) {
    memset(ch, 0, sizeof ch);
    scanf("%s %d", pl, &D);
    scanf("%d", &W);
    for (i=0; i<W; i++) {
      scanf("%s", bf);
      for (j=0; bf[j]; j++)
        ch[i][bf[j]-'a']++;
    }
    vector<string> tm;
    for (i=0; pl[i]; i++);
    pl[i]='+';
    pl[i+1]='\0';
    for (i=j=0; pl[i]; i++)
      if (pl[i]=='+') {
        tm.push_back(string(pl+j, pl+i));
        j=i+1;
      }
    memset(sm, 0, sizeof sm);
    for (b=1; b<=D; b++)
      for (t=1; t<=SIZE(tm); t++) {
        map< vector<int>, int > mp[12];
        mp[0][vector<int>(SIZE(tm[t-1]))]=1;
        for (d=1; d<=b; d++)
          FOREACH(z, mp[d-1]) {
            const vector<int> &vr=z->FST;
            for (w=0; w<W; w++) {
              vector<int> vR(SIZE(tm[t-1]));
              for (j=0; j<SIZE(tm[t-1]); j++)
                vR[j]=vr[j]+ch[w][tm[t-1][j]-'a'];
              mp[d][vR]+=z->SND;
              mp[d][vR]%=MOD;
            }
          }
        FOREACH(z, mp[b]) {
          const vector<int> &vr=z->FST;
          int A=1;
          for (i=0; i<SIZE(tm[t-1]); i++) {
            A*=vr[i];
            A%=MOD;
          }
          A*=z->SND;
          A%=MOD;
          sm[b]+=A;
          sm[b]%=MOD;
        }
      }
    PRINT("Case #%d:", z);
    for (d=1; d<=D; d++)
      PRINT(" %d", sm[d]);
    PRINT("\n");
  }
  return 0;
}
