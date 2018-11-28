#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

#define CLEAR(t) memset((t),0,sizeof(t))
#define FOR(i,a,b) for(__typeof(a)i=(a);i<=(b);++i)
#define FORD(i,a,b) for(__typeof(a)i=(a);i>=(b);--i)
#define REP(i,n) for(__typeof(n)i=0;i<(n);++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)

vector<string> split(const string& s, const string& delim=" ")
{ vector<string> res; string t; for(unsigned int i=0;i<s.length();i++) { if(delim.find(s[i])!=string::npos) { if(!t.empty()) { res.PB(t); t=""; } } else t+=s[i]; } if(!t.empty()) res.PB(t); return res; }
vector<int> splitint(const string& s, const string& delim=" ") { vector<string> vs=split(s); vector<int> res; for(unsigned int i=0;i<vs.size();i++) res.PB(atoi(vs[i].c_str())); return res; }

char s[1010];
vector<int> p;
int k,n;

int go()
{
  char t[1010];
  REP(i,n)t[i]=s[k*(i/k)+p[i%k]];
  int res=1;
  REP(i,n-1)if(t[i]!=t[i+1])res++;
  return res;
}

void _case(int casenum)
{
  scanf("%d %s ",&k,s);
  n=strlen(s);
  p.clear();REP(i,k)p.push_back(i);
  int now,res=n;
  do{ 
    now=go();
    if(now<res) res=now;
  } while (next_permutation(p.begin(),p.end()));
  printf("Case #%d: %d\n",casenum,res);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
