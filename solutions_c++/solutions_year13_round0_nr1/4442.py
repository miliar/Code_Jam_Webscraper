//Tic-Tac-Toe-Tomek.cpp
//SmartCoder
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minei(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxei(x)  max_element(x.begin(),x.end())-(x).begin()

#define uns(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acusum(x)  accumulate(x.begin(),x.end(),0)
#define acumul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>()); 
#define bits(x)     __builtin_popcount( x )
#define oo INT_MAX
#define inf 1000000000

const double pi=acos(-1.0);
const double eps=1e-11;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
vector<string> mat;

bool chkWin(char c){
  int ct=0,T=0;
  for(int i=0;i<4;++i){
    ct=0;
    T=0;
    for(int j=0;j<4;++j){
      if(mat[i][j]==c) ct++;
      if(mat[i][j]=='T') T=1;
    }
    if(ct==4) return true;
    if(ct==3&&T==1) return true;
  }

  for(int i=0;i<4;++i){
    ct=0;
    T=0;
    for(int j=0;j<4;++j){
      if(mat[j][i]==c) ct++;
      if(mat[j][i]=='T') T=1;
    }
    if(ct==4) return true;
    if(ct==3&&T==1) return true;
  }
  ct=0,T=0;
  for(int i=0;i<4;++i){
    if(mat[i][i]==c) ct++;
    if(mat[i][i]=='T') T=1;
    if(ct==4) return true;
    if(ct==3&&T==1) return true;
  }
  ct=0,T=0;
  for(int i=0;i<4;++i){
    if(mat[i][4-i-1]==c) ct++;
    if(mat[i][4-i-1]=='T') T++;
    if(ct==4) return true;
    if(ct==3&&T==1) return true;
  }

  return false;
}
bool dots(){
  int d=0;
  for(int i=0;i<4;++i){
    for(int j=0;j<4;++j){
      d+=(mat[i][j]=='.');
    }
  }
  return d==0;
}
int main(){
  freopen("in.txt" , "rt" , stdin);
  freopen("out.out" , "wt" , stdout);
  int n;
  scanf("%d",&n);
  for(int tc=1;tc<=n;++tc){
    mat.clear();
    mat.resize(4);
    for(int i=0;i<4;++i){
      cin>>mat[i];
    }
    bool XX=chkWin('X');
    bool OO=chkWin('O');
    if(!XX&&!OO&&dots()) printf("Case #%d: Draw\n",tc);
    else if(XX) printf("Case #%d: X won\n",tc);
    else if(OO) printf("Case #%d: O won\n",tc);
    else printf("Case #%d: Game has not completed\n",tc);

  }
  return 0;
}
