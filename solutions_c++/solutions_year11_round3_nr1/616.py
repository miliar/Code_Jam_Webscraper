#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <string>
#include <set>
#include <stack>
#include <deque>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <cctype>
#include <algorithm>
using namespace std;
///////////////////////////////////macro///////////////////////////////////
// file
#define fri freopen("input.txt","r",stdin)
#define fro freopen("output.txt","w",stdout)
// for
#define fn(i,n) for(int i=0;i<(n);i++)
#define fnd(i,n) for(int i=(n)-1;i>=0;i--)
#define fiab(i,a,b) for(int i=(a);i<(b);i++)
#define fiba(i,b,a) for (int i=(b)-1;i>=(a);i--)
#define ff(i,j,n,m) fn(i,n)fn(j,m)
#define fev(i,mas) for (size_t i=0;i<mas.size();i++)
// container
#define all(x) x.begin(),x.end()
#define sz(x) x.size()
// typedefs
typedef long long ll;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pi> vpi;
typedef pair<double,double> pd;
typedef vector<double> vd;
typedef vector<pd> vpd;
typedef vector<string> vs;
typedef set<int> si;
// i/o
struct tout{template<class T> tout operator()(const T &x){cout<<x;return *this;}}out;
struct tin{template<class T> tin operator()(T &x){cin>>x;return *this;}}in;
template<class T> inline tout operator, (tout, const T &x){cout<<x;return tout();}
template<class T> inline tin operator, (tin, T &x){cin>>x;return tin();}
inline int ni(){int x;scanf("%d",&x);return x;}
inline double nd(){double x;scanf("%lf",&x);return x;}
// other
#define bit(i) (1<<(i))
#define bitl(i) (1LL<<(i))
#define mp make_pair
#define pb push_back
#define vc vector
/////////////////////////////////////////////////////////////////////////////
int main(){
	fri;
	fro;
	int test;
	in,test;
	fn(t,test){
		out,"Case #",t+1,":\n";
		int n,m;
		in,n,m;
		vs mas(n);
		fn(i,n)
			in,mas[i];
		bool bad=false;
		fn(i,n){
			if (bad)
				break;
		fn(j,m){
			if (mas[i][j]!='#')
				continue;
			if (i+1<n && j+1<m && mas[i][j]=='#' && mas[i][j+1]=='#' && mas[i+1][j]=='#' && mas[i+1][j+1]=='#'){
				mas[i][j]=mas[i+1][j+1]='/';
				mas[i+1][j]=mas[i][j+1]='\\';
			}else{
				out,"Impossible";
				bad=true;
				break;
			}
		}
		}
		if (!bad)
			fn(i,n)
				out,mas[i],"\n";
		out,"\n";
	}
	return 0;
}