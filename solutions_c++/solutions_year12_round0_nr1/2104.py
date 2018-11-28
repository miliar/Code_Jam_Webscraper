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

int main() {
  // 1
  int i, j;
  char c;
  char sg[128];
  char se[128];
  char mp[256]={};
  mp['y']='a';
  mp['e']='o';
  mp['q']='z';
  FILE *f=fopen("A-ref.in", "r");
  for (i=0; i<3; i++) {
    fgets(sg, sizeof sg, f);
    fgets(se, sizeof se, f);
    for (j=0; sg[j]; j++) {
      assert(mp[sg[j]]=='\0' || mp[sg[j]]==se[j]);
      mp[sg[j]]=se[j];
    }
  }
  fclose(f);
  for (c='a'; true; c++)
    if (find(mp+'a', mp+'z'+1, c)==mp+'z'+1)
      break;
  mp['z']=c;
  // 1
  int t, T;
  scanf("%d\n", &T);
  for (t=1; t<=T; t++) {
    gets(sg);
    for (i=0; sg[i]; i++)
      sg[i]=mp[sg[i]];
    PRINT("Case #%d: %s\n", t, sg);
  }
  return 0;
}
