
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define REP(i,u) for(__typeof(u) i=0;i<(u);i++)
#define REPS(i,n) for(int(i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(__typeof(a) i=(a);i<=(b);i++)
#define FORD(i,a,b) for(__typeof(a) i=(a);i>=(b);i--)
#define FORE(it,c) for(__typeof(c.begin()) it=(c).begin();it!=(c).end();it++)
#define SQR(a) ((a)*(a))
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define mset(a,u) memset(a,u,sizeof(a))
#define sz(a) ((int)a.size())
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
#define PI 3.141592653589793238462
#define MAX 10000

using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;



string sDt;
int N;
vector<int> ind[MAX];  
int kde[MAX];

void parse(string s)
{
  int stack=0;
  REP(i,sz(s))
    if(s[i]=='(')
    {
      ind[stack].pb(i);
      stack++;
    }
    else if(s[i]==')')
    {
      stack--;
      ind[stack].pb(i);
    }
    
}

struct dt{
  double val;
  string name;
  int has;
  struct dt *child[2];
  dt()
  {
  };
};

string name,f;
int M;
vector<string> fea;

bool ma(string s)
{
  REP(i,sz(fea))
    if(fea[i]==s) return true;
  return false;
}

dt poi[MAX];
int poiind=0;
dt* parse2(int level)
{
  dt *ret = &poi[poiind++];
  ret->has=0;
  int poc=0;
  for(int i=ind[level][kde[level]]+1;;i++)
  {
    if(sDt[i]=='(')
    {
      ret->has=1;
      break;
    }
    if(sDt[i]==')')
      break;
    poc++;
  }
  string s=sDt.substr(ind[level][kde[level]]+1,poc);
  kde[level]+=2;
  istringstream ins;
  ins.str(s);
  ins >> ret->val >> ret->name;
 // cout<<ret->val<<".."<<ret->name<<"____"<<endl;  
  if(!ret->has) return ret;
  ret->child[0]=parse2(level+1);
  ret->child[1]=parse2(level+1);  
  return ret;
}

void solve_case(int pp)
{
  poiind=0;
   cin>>N;getchar();
   sDt="";
   REP(i,MAX)
   {
     ind[i].clear();  
     kde[i]=0;
   }
   string s;
   REP(i,N)
   {
     getline(cin, s);
     sDt+=s;
     sDt+=" ";
   }
   parse(sDt);
   dt *TREE;
   TREE = parse2(0);
   cin>>N;
printf("Case #%d:\n",pp+1);
   REP(i,N)
   {
     cin>>name>>M;
     fea.clear();
     REP(j,M)
     {
       cin>>f;
       fea.pb(f);
     }
     dt *cur=TREE;
     double ret=1;
     while(cur->has)
     {
       ret*=cur->val;
    //   cout<<cur->val<<" "<<cur->name<<endl;
       if(ma(cur->name))
         cur=cur->child[0];
       else
         cur=cur->child[1];
     }
     ret*=cur->val;
     printf("%.7lf\n",ret);
   }
   




/*   REP(i,5)
   {
     cout<<"i : "<<sz(ind[i])<<endl;
     REP(j,sz(ind[i]))
       cout<<ind[i][j]<<", ";
     cout<<endl;
   }*/
//    cout<<sDt<<endl;
//    cout<<"----------------------"<<endl;
}


int cases;
int main( )
{
  scanf("%d",&cases);getchar();
  REP(ii,cases)
  {
    solve_case(ii);
  }         
  return 0;
}

