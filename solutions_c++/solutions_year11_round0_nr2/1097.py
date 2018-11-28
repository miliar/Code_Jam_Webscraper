#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

int _,C,D,n;
char a,b,c;
map<pair<char,char>, char> mut;
int op[256],opp;
int ile[256];
vector<char> lst;
pair<char,char> bp;

int main() {
   scanf("%d",&_);
   REP(test,_) {
      mut.clear();
      REP(i,256) op[i]=0;
      lst.clear();
      opp=0; REP(j,26) ile[j]=0;
      scanf("%d",&C);
      REP(i,C) scanf(" %c%c%c",&a,&b,&c), mut[make_pair(a,b)] = mut[make_pair(b,a)] = c;
      scanf("%d",&D);
      REP(i,D) scanf(" %c%c",&a,&b), op[a-'A'] |= 1<<(b-'A'), op[b-'A'] |= 1<<(a-'A');
      scanf("%d",&n);
      REP(i,n) {
	 scanf(" %c",&a);
	 lst.push_back(a);
	 if (lst.size() >= 2 && mut.find(bp = make_pair(lst.back(), lst[lst.size()-2])) != mut.end()) {
	    lst.pop_back();
	    if (--ile[lst.back()-'A']==0) opp &= ~(1<<(lst.back()-'A'));
	    lst.pop_back(), lst.push_back(mut[bp]), opp |= 1<<(mut[bp]-'A'), ile[mut[bp]-'A']++;
	 }
	 else if (opp & op[a-'A']) { lst.clear(), opp = 0; REP(j,26) ile[j]=0; }
	 else opp |= 1<<(a-'A'), ile[a-'A']++;
      }
      printf("Case #%d: [",test+1);
      REP(i,lst.size())
	 if (i!=lst.size()-1) printf("%c, ",lst[i]);
	 else printf("%c",lst[i]);
      printf("]\n");
   }
}
