#include <vector>
#include <list>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>  
using namespace std;


#define oo (int)1e8
#define v(x) vector<x>
#define pb push_back
#define sz size()
#define forz(i,n) for(int i = 0; i < (n); i++)
#define foro(i,o) for(int i = 0; i < (o).size(); i++)
#define fore(i,o) for(typeof((o).begin()) i = (o).begin(); i != (o).end(); i++)
#define all(a) (a).begin(),(a).end()
#define clr(a,v) memset((a),(v),sizeof(a))
#define isto(c,x) ((c).find(x) != (c).end()) 
#define ist(c,x) (find(ALL(c),x) != (c).end()) 
#define GI ({int t; scanf("%d",&t);t;})

#define dbg(x) (cerr << #x << ": " << x<<'\t')
#define dbge(x) (dbg(x),cerr << endl)
#define iamhere (cout<< "I am here!!\n")

typedef pair<int,int> ii; 
typedef stringstream ss;
typedef long long ll;
typedef long double ld;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef priority_queue<ii,vector<ii>,greater<ii> > p_q;

template <class T>
inline void cmax(T &a, T b) { a = max(a,b); } 
template <class T>
inline void cmin(T &a, T b) { a = min(a,b); } 
int isand[10005], ischan[10005], isset[10005];
int n;
int dp[2][10005];
int doit(int des, int ind)
{
	if(ind >= (n-1)/2)  {
//dbg(des), dbg(ind); dbge(isset[ind]);	
	if(isset[ind] == des) {return 0 ;}
	else return oo;
	}
	int& ret = dp[des][ind];
	if(ret != -1) return ret;
	ret = oo;
		if((isand[ind]==1)^des) {
				ret <?= min(doit(des, ind*2+1), doit(des,ind*2+2));
		}
		else
		{
			ret <?= doit(des, ind*2+1)+doit(des,ind*2+2);			
		}
		if(ischan[ind])
		{
			isand[ind] = !isand[ind];
		if((isand[ind]==1)^des) {
				ret <?= 1+min(doit(des, ind*2+1), doit(des,ind*2+2));
		}
		else
		{
			ret <?= 1+doit(des, ind*2+1)+doit(des,ind*2+2);			
		}			
			isand[ind] = !isand[ind];				
		}

//dbg(des), dbg(ind); dbge(ret);
	return ret;
}

int main()
{
//	ios_base:: sync_with_stdio(false);
	int tt = GI;
	
	forz(t,tt)
	{
		memset(dp,-1,sizeof(dp));
		int n = GI, des= GI;
		::n = n;
		forz(i,(n-1)/2) isand[i] = GI, ischan[i] = GI, isand[i] = isand[i]==1, ischan[i] = ischan[i]==1;
		forz(i,(n+1)/2) isset[i+(n-1)/2] = GI;

		int ans = doit(des, 0);		
		if(ans >= oo) printf("Case #%d: IMPOSSIBLE\n",t+1);
		else printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}

