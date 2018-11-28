#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

class T
{
public:
  T() { }
  //side of the start
  //side=0 -> left
  //side=1 -> right
  T(int _from, int _to, bool _side)
  { from=_from; to=_to; side=_side; }
  int from, to;
  bool side;
};

class CMP
{
public:
  bool operator () (const T &a, const T &b)
  { return a.from < b.from; }
};

vector<T> v;
int t;

int parse(string str)
{
  int res=0;
  int p=0;
  while(str[p]!=':')
    { res*=10; res+=str[p]-'0'; p++; }
  p++;
  res*=60;
  while(p<str.length())
    { res*=10; res+=str[p]-'0'; p++; }
  return res;
}

int main()
{
  int tt;
  scanf("%d",&tt);
  char tmps[100];
  for(int ttt=1;ttt<=tt;ttt++) {
    v.clear();
    scanf("%d",&t);
    int na,nb;
    scanf("%d%d",&na,&nb);
    for(int i=0;i<na;i++) {
      scanf("%s",tmps);
      int st=parse(tmps);
      scanf("%s",tmps);
      int fin=parse(tmps);
      v.push_back(T(st,fin,0));
    }
    for(int i=0;i<nb;i++) {
      scanf("%s",tmps);
      int st=parse(tmps);
      scanf("%s",tmps);
      int fin=parse(tmps);
      v.push_back(T(st,fin,1));      
    }
    sort(v.begin(),v.end(),CMP());
    
    vector<int> side[2];

    int res[2];
    res[0]=res[1]=0;
    for(int i=0;i<v.size();i++) {
      int s=v[i].side;
      if(side[s].empty()) {
	res[s]++;
	side[!s].push_back(v[i].to+t);
	continue; 
      }
      int p=0;
      for(int j=0;j<side[s].size();j++)
	if(side[s][j] < side[s][p])
	  p=j;
      
      if(side[s][p] <= v[i].from)
	side[s].erase(side[s].begin()+p);
      else
	res[s]++;

      side[!s].push_back(v[i].to+t);
    }
    printf("Case #%d: %d %d\n", ttt, res[0],res[1]);
  }
  return 0;
}
