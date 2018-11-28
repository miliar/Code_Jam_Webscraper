#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>

#define FOR(i,k,n)  for (int i=(k); i<(int)(n); ++i)
#define REP(i,n)    FOR(i,0,n)
#define FORIT(i,c)	for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define sz          size()
#define pb          push_back
#define mp          make_pair
#define ALL(X)      (X).begin(),(X).end()

using namespace std;

typedef long long ll;
typedef vector<int> vi;

void output(int cas,string str){
  cout<<"Case #"<<cas<<": "<<str<<endl;
  return;
}

bool won(vector<string> v,char c){
  int x[10]={0,0,0,0,0,1,2,3,0,0};
  int y[10]={0,1,2,3,0,0,0,0,0,3};
  int xx[10]={1,1,1,1,0,0,0,0,1,1};
  int yy[10]={0,0,0,0,1,1,1,1,1,-1};
  REP(i,10){
    bool flag=true;
    REP(j,4){
      if(v[x[i]+xx[i]*j][y[i]+yy[i]*j]!=c && v[x[i]+xx[i]*j][y[i]+yy[i]*j]!='T') flag=false;
    }
    if(flag)return true;
  }
  return false;
}
	 

int main(void)
{
  int n;
  cin>>n;
  FOR(cas,1,n+1){
    vector<string> v;
    string str;
    REP(i,4){
      cin>>str;
      v.pb(str);
    }
    if(won(v,'X'))output(cas,"X won");
    else if(won(v,'O'))output(cas,"O won");
    else{
      bool flag=false;
      REP(i,4)REP(j,4)if(v[i][j]=='.')flag=true;
      if(flag)output(cas,"Game has not completed");
      else output(cas,"Draw");
    }
  }
  return 0;
}
