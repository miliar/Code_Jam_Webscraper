#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <string.h>
using namespace std;

#define rep(i,a) for((i)=0;(int)(i)<(a);(i)++)
#define rrep(i,a,b) for((i)=(a);(i)>=(b);(i)--)
#define maX(a,b) ((a)>(b)?(a):(b))
#define miN(a,b) ((a)<(b)?(a):(b))
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pis pair<int,string>
#define psi pair<string,int>
#define pss pair<string,string>
#define ll long long
#define ull unsigned long long
#define fi first
#define se second
#define re return
#define sz(x) ((int)(x).size())
#define vi vector<int>
#define vs vector<string>
#define vpii vector< pii >
#define S(x) scanf("%d",&x)

template<class T> T abs(T x){return x>0?x:-x;}
inline int toInt(string s) {int v;istringstream sin(s);sin>>v;return v;}
inline ll toll(string s) {ll v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> inline T sqr(T x) {return x*x;}
template<class T> inline T gcd(T a,T b) {if (a<0) a=-a;if (b<0) b=-b;return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {return a*(b/gcd(a,b));}

void solve()
{
    int i,j,x,o;
    string s[4];
    rep(i,4)    cin>>s[i];
    bool draw=true;
    rep(i,4){
        x=o=0;
        x=(s[i][0]=='X')+(s[i][1]=='X')+(s[i][2]=='X')+(s[i][3]=='X');
        o=(s[i][0]=='O')+(s[i][1]=='O')+(s[i][2]=='O')+(s[i][3]=='O');
        x+=(s[i][0]=='T')+(s[i][1]=='T')+(s[i][2]=='T')+(s[i][3]=='T');
        o+=(s[i][0]=='T')+(s[i][1]=='T')+(s[i][2]=='T')+(s[i][3]=='T');
        
        if(x==4){    cout<<"X won\n";return;}
        else if(o==4){        cout<<"O won\n";return;}

        x=(s[0][i]=='X')+(s[1][i]=='X')+(s[2][i]=='X')+(s[3][i]=='X');
        o=(s[0][i]=='O')+(s[1][i]=='O')+(s[2][i]=='O')+(s[3][i]=='O');
        x+=(s[0][i]=='T')+(s[1][i]=='T')+(s[2][i]=='T')+(s[3][i]=='T');
        o+=(s[0][i]=='T')+(s[1][i]=='T')+(s[2][i]=='T')+(s[3][i]=='T');
        if(x==4){    cout<<"X won\n";return;}
        else if(o==4){        cout<<"O won\n";return;}

        rep(j,4)if(s[i][j]=='.') draw=false;
    }
    x=o=0;
    rep(i,4){
        x+=((s[i][i]=='X')||(s[i][i]=='T'));
        o+=((s[i][i]=='O')||(s[i][i]=='T'));
    }
 
    if(x==4){           cout<<"X won\n";return;}
    else if(o==4){      cout<<"O won\n";return;}


    x=o=0;
    rep(i,4){
        x+=((s[i][3-i]=='X')||(s[i][3-i]=='T'));
        o+=((s[i][3-i]=='O')||(s[i][3-i]=='T'));
    }

     
    if(x==4){    cout<<"X won\n";return;}
    else if(o==4){        cout<<"O won\n";return;}
    
    if(draw)    cout<<"Draw\n";
    else    cout<<"Game has not completed\n";
}
int main()
{
		int totTC,testcase;
		cin>>totTC;
		for(testcase=1;testcase<=totTC;testcase++){
			printf("Case #%d: ",testcase);
			solve();
		}
        return 0;
}

