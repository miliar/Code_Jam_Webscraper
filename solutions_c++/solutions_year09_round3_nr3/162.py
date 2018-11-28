//Bribe the Prisoners
//

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



int main()
{
//	ios_base:: sync_with_stdio(false);
	int t = GI;
	int tt = 0;
	while(tt<t)
	{
		int p =GI,q=GI;
		vi arr(q),L(q),R(q);
		forz(i,q) cin >>arr[i];
		forz(i,q) L[i] = i==0?arr[i]-1:arr[i]-arr[i-1]-1;
		forz(i,q) R[i] = i+1==q?p-arr[i]:L[i+1];

		vvi ans(q,vi(q));
		for(int l = 1; l <= q; l++)
		{
			for(int s = 0; s+l<=q; s++)
			{
				int e = s+l-1;
				int now = arr[e]-arr[s]+L[s]+R[e];
				int ret = oo;
				for(int i = s; i <= e; i++)
				{
					int val = 0;
					if(s!=i)
						val = ans[s][i-1];
					if(e!=i)		
						val += ans[i+1][e];
					cmin(ret,val);
				}
				ret += now;
		//			dbg(s), dbg(e), dbge(ret);
				ans[s][e] = ret;
			}
		}
		cout << "Case #"<<++tt << ": "<<ans[0][q-1] << endl;
	}
	return 0;
}

