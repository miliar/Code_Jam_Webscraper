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
ll arr[10];
int main()
{
//	ios_base:: sync_with_stdio(false);
	int tt=GI;
	ll n, A, B, C, D, x0, y0 ,M;
	forz(t,tt)
	{
		fill(arr,arr+10,0);
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n, &A,&B,&C, &D, &x0, &y0 , &M);
		ll X = x0, Y = y0;
		int p = X%3*3 + Y%3;		
		arr[p]++;
		forz(i,n) {
			if(i==0) continue;
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			p = X%3*3 + Y%3;
			arr[p]++;
		}
		ll cnt = 0;
		forz(i,9)
		{
//			cout << arrx[i] <<" " << arry[i] << endl;
			forz(j,9) forz(k,9) {
				if(i > j || j > k) continue;
				if((i/3+j/3+k/3)%3 == 0 && (i%3+j%3+k%3)%3 == 0 ) {				
					ll x = arr[i], y = arr[j], z = arr[k];
					if(i==j && j == k) cnt += x*(x-1)*(x-2)/6;
					else if(i==j) cnt += x*(x-1)/2 * z;
					else if(j==k) cnt += y*(y-1)/2* x; 
					else cnt += x*y*z;
				}
			}
		}
		printf("Case #%d: %lld\n",t+1,cnt);
	}
	return 0;
}

