#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

const int maxLen=10001;
map <string,int> Map;
set <string> Set;
char s[maxLen];
int testcases,n,S,Q;

void init() {
  Set.clear();
  scanf("%d\n",&S);
  for (int i=0;i<S;i++) {
    gets(s);
    //    cout<<s<<endl;
    string t=s;
    Set.insert(t);
  }
}

void solve() {
  scanf("%d\n",&Q);
  Map.clear();
  int tot=S,ans=0;
  for (int i=0;i<Q;i++) {
    gets(s);
    string t=s;
    if (Set.find(t)==Set.end()) continue;
    //    cout<<t<<" OK "<<Map[t]<<endl;
    if (Map[t]!=1) {
      tot--;
      //      cout<<i<<" " << t<<' '<<tot<<endl;
      if (tot==0) {
	Map.clear();
	ans++;
	tot=S-1;
	//	continue;
      }
      Map[t]=1;
    }
  }
  printf("Case #%d: %d\n",++testcases,ans);
}

int main() {
  testcases=0;
  scanf("%d",&n);
  while (n--) {
    init();
    solve();
  }
}
