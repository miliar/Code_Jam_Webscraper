#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <ctime>
#include <complex>
using namespace std;
typedef long long lld;
typedef unsigned long long llu;
const int intmax=0x3f3f3f3f;//NOTES:intmax
const lld lldmax=0x3f3f3f3f3f3f3f3fll;//NOTES:lldmax
double eps=1e-8;//NOTES:eps
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
template<class T> inline T sqr(T x){return x*x;}//NOTES:sqr
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit(
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(
template<class T> inline T checkmod(T n,T m) {return (n%m+m)%m;}//NOTES:checkMod(
template<class T> inline T gcd(T a,T b)//NOTES:gcd(
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T euclid(T a,T b,T &x,T &y)//NOTES:euclide(
{if(a<0){T d=euclid(-a,b,x,y);x=-x;return d;}
if(b<0){T d=euclid(a,-b,x,y);y=-y;return d;}
if(b==0){x=1;y=0;return a;}else{T d=euclid(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
template<class T> inline int dblcmp(T a,const T b){a-=b; return a>eps?1:(a<-eps?-1:0);}//NOTES:doublecmp
template<class T> inline int sgn(T a){return a>eps?1:(a<-eps?-1:0);}
#define mem(a, val) memset(a, val, sizeof(a))//memset(
#define shl(i)      ((lld)1 << (i))
#define MP make_pair
#define PB push_back

char a[5][5];

bool judge(char ch){
	for (int i=0; i<4; ++i){
		bool flag = true;
		for (int j=0; j<4; ++j) flag = flag && (a[i][j] == ch || a[i][j] == 'T');
		if (flag) return true;
	}
	for (int i=0; i<4; ++i){
		bool flag = true;
		for (int j=0; j<4; ++j) flag = flag && (a[j][i] == ch || a[j][i] == 'T');
		if (flag) return true;
	}
	bool flag = true;
	for (int j=0; j<4; ++j) flag = flag && (a[j][j] == ch || a[j][j] == 'T');
	if (flag) return true;
	flag = true;
	for (int j=0; j<4; ++j) flag = flag && (a[3-j][j] == ch || a[3-j][j] == 'T');
	return flag;
}

bool filled(){
	for (int i=0; i<4; ++i){
		for (int j=0; j<4; ++j){
			if (a[i][j] == '.') return false;
		}
	}
	return true;
}

int main(){
	int cases;
	//freopen("data.in", "r", stdin);
	//freopen("data.out", "w", stdout);
	cin >> cases;
	for (int I=1; I<=cases; ++I){
		for (int i=0; i<4; ++i){
			scanf("%s", a[i]);
		}
		printf("Case #%d: ", I);
		if (judge('X')){
			puts("X won");
		}else if (judge('O')){
			puts("O won");
		}else if (filled()){
			puts("Draw");
		}else {
			puts("Game has not completed");
		}
	}
	return 0;
}
