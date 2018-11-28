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

char s[50];
vector<pair<int,int> > v;
int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};

long long area(vector<pair<int,int> >& v)
{
  long long res=0;
  long long ux,uy,vx,vy;
  int n=v.size();
  REP(i,n)
  {
    ux=v[i].first; uy=v[i].second;
    vx=v[(i+1)%n].first; vy=v[(i+1)%n].second;
    res+=ux*vy-vx*uy;
  }
  if(res<=0) res=-res;
  return res/2;
}

void print(vector<pair<int,int> >& v)
{ REP(i,v.size())printf("(%d,%d) ",v[i].first,v[i].second); printf("\n"); }

void _case(int casenum)
{
  int L,t;
  int x=0,y=0,xx=0,yy=0,dir=0;
  v.clear();
  v.PB(MP(xx,yy));
  scanf("%d ",&L);
  REP(i,L)
  {
    scanf("%s %d ",s,&t);
    int len=strlen(s);
    REP(j,t)REP(k,len)
    {
      if(s[k]=='F') { x+=dx[dir]; y+=dy[dir]; }
      else
      {
        if(s[k]=='L') { dir=(dir+3)%4; }
        if(s[k]=='R') { dir=(dir+1)%4; }
        if((xx!=x)||(yy!=y)) { xx=x; yy=y; v.PB(MP(xx,yy)); }
      }
    }
  }
  if(v.back()==v.front()) v.pop_back();
  long long a=area(v);

  vector<pair<int,int> > v1,v2,v3,v4;
  v1.clear();v2.clear();v3.clear();v4.clear();

//print(v);
  sort(v.begin(),v.end());
//print(v);
  int min=5000,max=-5000;
  REP(i,v.size())
  {
    if(v[i].second<min)
    {
      min=v[i].second;
      if(v1.empty()) v1.PB(v[i]); else { v1.PB(MP(v[i].first,v1.back().second)); v1.PB(v[i]); }
    }
    if((i+1==v.size())||(v[i+1].first>v[i].first))
      if(v[i].second>max)
      {
        max=v[i].second;
        if(v2.empty()) v2.PB(v[i]); else { v2.PB(MP(v[i].first,v2.back().second)); v2.PB(v[i]); }
      }
  }
  reverse(v.begin(),v.end());
  min=5000;max=-5000;
  REP(i,v.size())
  {
    if(v[i].second>max)
    {
      max=v[i].second;
      if(v3.empty()) v3.PB(v[i]); else { v3.PB(MP(v[i].first,v3.back().second)); v3.PB(v[i]); }
    }
    if((i+1==v.size())||(v[i+1].first<v[i].first))
      if(v[i].second<min)
      {
        min=v[i].second;
        if(v4.empty()) v4.PB(v[i]); else { v4.PB(MP(v[i].first,v4.back().second)); v4.PB(v[i]); }
      }
  }

//print(v1); print(v2); print(v3); print(v4);

  vector<pair<int,int> > w;
  w.clear();
  reverse(v4.begin(),v4.end());
  reverse(v2.begin(),v2.end());
  REP(i,v1.size()) w.PB(v1[i]);
  REP(i,v4.size()) w.PB(v4[i]);
  REP(i,v3.size()) w.PB(v3[i]);
  REP(i,v2.size()) w.PB(v2[i]);
  long long b=area(w);

  printf("Case #%d: %lld\n",casenum,b-a);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
