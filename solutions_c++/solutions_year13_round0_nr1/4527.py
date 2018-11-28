
// AUTHOR: AMAN JAIN
#include <iostream>
#include <sstream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <deque>
#include <bitset>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>

using namespace std;

#define VI vector < int >
#define VVI(A,N,M) vector< VI > A( N, VI (M) )
#define LL long long
#define LLU unsigned long long
#define SI ({int x;scanf("%d",&x);x;})
#define SC ({char x;scanf("%c",&x);x;})
#define PI acos(-1)
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size()) 
#define SORT(c) sort(ALL(c)) 
#define FIT(it,v) for (typeof(v.begin()) it = v.begin(); it != v.end(); it++)
#define FITD(it,v) for (typeof(v.rbegin()) it = v.rbegin(); it != v.rend(); it++)
#define FOR(i,start,end) for(int i=start;i<end;i++)
#define IATOV(a) ({vector<int> v(a,a+sizeof(a)/sizeof(int));v;})
#define CATOV(a) ({vector<char> v(a,a+sizeof(a)/sizeof(char));v;})
#define sieve(a) ({int b=ceil(sqrt(a));VI d(a,0);VI e;int f=2;e.pb(2);e.pb(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.pb(c);}}e;})
#define INF 1000000007
#define EPS 1e-9
#define mt(x, y, z) mp(mp(x,y),z)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
template <class T> string str(T Number){

	string Result;          // string which will contain the result

	ostringstream convert;   // stream used for the conversion

	convert << Number;      // insert the textual representation of 'Number' in the characters in the stream

	Result = convert.str();
	return Result;
}
  int StringToNumber ( const string &Text )
  {
     istringstream ss(Text);
     int result;
     return ss >> result ? result : 0;
  }
template<class T> inline vector<pair<T,int> > FACTORISE(T n){vector<pair<T,int> >R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline T TOTIENT(T n) {vector<pair<T,int> > R=FACTORISE(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}
double rnd(float d) //for rounding values
{
	          return floor(d + 0.49);
}
int check_rows(vector<string>&a,int& f){
FOR(i,0,sz(a)){
int x=0,o=0;
FOR(j,0,sz(a[i])){
if(a[i][j]=='X')x++;
if(a[i][j]=='O')o++;
if(a[i][j]=='T'){x++;o++;}
if(a[i][j]=='.')f=1;
}
if(x==4)return 0;
if(o==4)return 1;
}
return 2;
}
int check_cols(vector<string>&a,int& f){
FOR(i,0,sz(a)){
int x=0,o=0;
FOR(j,0,sz(a[i])){
if(a[j][i]=='X')x++;
if(a[j][i]=='O')o++;
if(a[j][i]=='T'){x++;o++;}
if(a[j][i]=='.')f=1;
}
if(x==4)return 0;
if(o==4)return 1;
}
return 2;
}
int check_dig(vector<string>& a,int&f){
int x=0,o=0;
FOR(i,0,4){
if(a[i][i]=='X')x++;
if(a[i][i]=='O')o++;
if(a[i][i]=='T'){x++;o++;}
if(a[i][i]=='.')f=1;
}
if(x==4)return 0;
if(o==4)return 1;
x=0;o=0;
FOR(i,0,4){
if(a[i][4-i-1]=='X')x++;
if(a[i][4-i-1]=='O')o++;
if(a[i][4-i-1]=='T'){x++;o++;}
if(a[i][4-i-1]=='.')f=1;
}
if(x==4)return 0;
if(o==4)return 1;
return 2;
}
int main(){
int T;
cin>>T;
getchar();
FOR(i,1,T+1){
vector<string> a(4);
FOR(j,0,4)cin>>a[j];
int f=0;
int t;
t=check_rows(a,f);
if(t==0){printf("Case #%d: X won\n",i);getchar();continue;}
if(t==1){printf("Case #%d: O won\n",i);getchar();continue;}
t=check_cols(a,f);
if(t==0){printf("Case #%d: X won\n",i);getchar();continue;}
if(t==1){printf("Case #%d: O won\n",i);getchar();continue;}
t=check_dig(a,f);
if(t==0){printf("Case #%d: X won\n",i);getchar();continue;}
if(t==1){printf("Case #%d: O won\n",i);getchar();continue;}
if(f==1){printf("Case #%d: Game has not completed\n",i);}
else printf("Case #%d: Draw\n",i);
getchar();
}
	return 0;
}
