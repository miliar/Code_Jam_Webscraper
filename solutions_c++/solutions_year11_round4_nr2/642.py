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
	for (int tt=0;tt<test;tt++){
		out,"Case #",(tt+1),": ";
		int n,m,d;
		in,n,m,d;
		vector<string> s(n);
		fn(i,n)
			in,s[i];
		vvi mas(n,vi(m));
		ff(i,j,n,m)
			mas[i][j]=d+s[i][j]-'0';
		int maxx=-1;
		for (int top=0;top<n;top++){
			for (int bot=top+2;bot<n;bot++){
				for (int left=0;left<m;left++){
					for (int right=left+bot-top;right<=left+bot-top && right<m;right++){
						int mx=0;
						int my=0;
						for (int i=top;i<=bot;i++){
							for (int j=left;j<=right;j++){
								if ((i==top || i==bot) && (j==left || j==right))
									continue;
								mx+=mas[i][j]*(2*j-(left+right));
								my+=mas[i][j]*(2*i-(top+bot));
							}
						}
						if (mx==0 && my==0)
							maxx=max(maxx,bot-top+1);
					}
				}	
			}
		}
		if (maxx==-1)
			out,"IMPOSSIBLE";
		else
			out,maxx;
		out,"\n";
	}
	return 0;
}