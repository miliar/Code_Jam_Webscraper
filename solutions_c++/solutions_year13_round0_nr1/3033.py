#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <stack>
#include <climits>
#include <deque>
#include <bitset>
#include <cassert>
#include <ctime>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
const int dy[]={-1,0,1,0},dx[]={0,1,0,-1};
// adjust problem by problem
const double EPS=1e-8;
const double PI=acos(-1.0);
#define REP(i,n) for(int i=0;i<(int)n;++i)
#ifdef __GNUC__
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
int popcount(int n){return __builtin_popcount(n);}
int popcount(ll n){return __builtin_popcountll(n);}
#endif
#ifndef __GNUC__
template<class T> int popcount(T val){
  val = val - ((val >> 1) & 0x55555555);
  val = (val & 0x33333333) + ((val >> 2) & 0x33333333);
  val = (val + (val >> 4)) & 0x0f0f0f0f;
  val += val >> 8;
  val += val >> 16;
  return (int)(val & 0x0000003f);
}
#endif
template<class T>int SIZE(T a){return a.size();}
template<class T>string IntToString(T num){string res;stringstream ss;ss<<num;return ss.str();}
template<class T>T StringToInt(string str){T res=0;for(int i=0;i<SIZE(str);i++)res=(res*10+str[i]-'0');return res;}
template<class T>T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template<class T>T lcm(T a,T b){return a/gcd(a,b)*b;}
template<class T> void PrintSeq(T &a,int sz){for(int i=0;i<sz;i++){cout<<a[i];if(sz==i+1)cout<<endl;else cout<<' ';}}
ll getTen(int a){return (a<=0)?1:(getTen(a-1)*10);}
bool EQ(double a,double b){return abs(a-b)<EPS;}
void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}
vector<string> split(string str,char del){
  vector<string> res;
  for(int i=0,s=0;i<SIZE(str);i++){
    if(str[i]==del){if(i-s!=0)res.push_back(str.substr(s,i-s));s=i+1;}
    else if(i==SIZE(str)-1){res.push_back(str.substr(s));}
  }
  return res;
}

char field[4][4];
void solve(){
  for(int i=0;i<4;i++){
    int a=0;
    int b=0;
    bool isT=false;
    for(int j=0;j<4;j++){
      if(field[i][j]=='O')a++;
      if(field[i][j]=='X')b++;
      if(field[i][j]=='T')isT=true;
    }
    if(a+isT==4){
      cout<<"O won"<<endl;
      return;
    }
    if(b+isT==4){
      cout<<"X won"<<endl;
      return;
    }
  }
  for(int j=0;j<4;j++){
    int a=0;
    int b=0;
    bool isT=false;
    for(int i=0;i<4;i++){
      if(field[i][j]=='O')a++;
      if(field[i][j]=='X')b++;
      if(field[i][j]=='T')isT=true;
    }
    if(a+isT==4){
      cout<<"O won"<<endl;
      return;
    }
    if(b+isT==4){
      cout<<"X won"<<endl;
      return;
    }
  }
  {
    int a=0;
    int b=0;
    bool isT=false;
    for(int i=0;i<4;i++){
      if(field[i][i]=='O')a++;
      if(field[i][i]=='X')b++;
      if(field[i][i]=='T')isT=true;
    }
    if(a+isT==4){
      cout<<"O won"<<endl;
      return;
    }
    if(b+isT==4){
      cout<<"X won"<<endl;
      return;
    }
  }
  {
    int a=0;
    int b=0;
    bool isT=false;
    for(int i=0;i<4;i++){
      if(field[i][3-i]=='O')a++;
      if(field[i][3-i]=='X')b++;
      if(field[i][3-i]=='T')isT=true;
    }
    if(a+isT==4){
      cout<<"O won"<<endl;
      return;
    }
    if(b+isT==4){
      cout<<"X won"<<endl;
      return;
    }
  }
  int cnt=0;
  for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
      if(field[i][j]!='.')cnt++;
  if(cnt==16)cout<<"Draw"<<endl;
  else cout<<"Game has not completed"<<endl;
}
int main(){
  int T;
  cin>>T;
  int t=0;
  while(T--){
    cout<<"Case #"<<++t<<": ";
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
        cin>>field[i][j];
    solve();
  }
  
  return 0;
}
