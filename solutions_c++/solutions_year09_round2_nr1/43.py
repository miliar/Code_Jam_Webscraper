//DEDICATED TO EMMA WATSON, THE BRITISH *SUNSHINE*
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
//#include <fstream>

#define eps 10e-10
#define INF 1000000000
#define PI 3.141592653589793238462
#define EU 2.71828182845904523536
#define sz(a) (int)a.size()
#define pb(a) push_back(a)
#define mset(a,hodnota) memset(a,hodnota,sizeof(a))
#define wh(a) a.begin(),a.end()
#define REP(i,n) for(__typeof(n) i=0;i<(n);++i)
#define REPS(i,n) for(int(i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b) for(__typeof(a) i=(a);i>=(b);--i)
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define SQR(a) ((a)*(a))
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
typedef long long ll;
typedef long double ld;
using namespace std;

struct node
{
  node * ch[2];
  double v;
  string n;
  node()
  {
    ch[0]=ch[1]=NULL;  
    n="";
  }
};

int L;
string T;

void myParse(node * cur,int x,int y)
{//<x,y)
//   cout<<"PARSE : "<<x<<" "<<y<<" : "<<T.substr(x,y-x)<<endl;
  while(T[x]!='(')x++;
  while(T[y-1]!=')')y--;

  if (T.substr(x+1,y-x-1).find("(")==string::npos)
  {//leaf
//     cout<<"leaf"<<endl;
    stringstream ss(T.substr(x+1,y-x));
    ss>>cur->v;      
  }else
  {//inner node
    int next_space=x;while(T[next_space]!=' ')next_space++;
    stringstream ss(T.substr(x+1,next_space-x));
    ss>>cur->v;
    int next_space2=next_space+1;while(T[next_space2]!=' ')next_space2++;
    stringstream ss2(T.substr(next_space,next_space2-next_space));
    ss2>>cur->n;
    //now children are in (next_space2,y)
    int lev=0,passed=0,first_end=-1;
    FOR(i,next_space2,y)
    {
      if (T[i]=='(')lev++,passed=1;
      if (T[i]==')') lev--;
      if (passed && lev==0 && T[i]==')')
      {
        first_end=i;
        break;
      }
    }
    cur->ch[0]=new node();
    cur->ch[1]=new node();
    myParse(cur->ch[0],next_space2,first_end+1);
    myParse(cur->ch[1],first_end+1,y-1);  
  }
}

void debug(node * p,string pad)
{
  cout<<pad<<"node : "<<p->v;
  if (p->ch[0]!=NULL)
  {
    cout<<" "<<p->n<<endl;
    cout<<pad<<"Child 1"<<endl;
    debug(p->ch[0],pad+"  ");

    cout<<pad<<"Child 2"<<endl;
    debug(p->ch[1],pad+"  ");
  }else
    cout<<pad<<" leaf"<<endl;
}
void solve_case()
{
  putchar(10);
  cin>>L;getchar();
  T="";
  REP(i,L)
  {
    string s;
    getline(cin,s);
    T+=s;  
  }
//   cout<<T<<endl;
  node * root=new node();
  myParse(root,0,sz(T));
//   debug(root,"");
  int A;
  cin>>A;
  REP(ii,A)
  {
    string name;
    set<string> feat;
    cin>>name;
    int K;
    cin>>K;
    REP(i,K)
    {
      string buf;
      cin>>buf;
      feat.insert(buf);
    }
    double p=1;
    node * cur=root;
//     cout<<"PATH : ";
    while(1)
    {
//       cout<<cur->n<<" ";
      p*=cur->v;
      if (cur->n=="")
        break;
      cur=cur->ch[feat.find(cur->n)==feat.end()];    
    }
//     cout<<endl;
    printf("%.9lf\n",p);
  }
}


int cases;
int main( )
{
  scanf("%d",&cases);getchar();
  REP(ii,cases)
  {
    printf("Case #%d: ",ii+1);
    solve_case();
  }         
  return 0;
}
