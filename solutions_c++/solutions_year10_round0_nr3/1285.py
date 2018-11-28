#define DEBUG 1

using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <fstream>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep(i, a, b, x) for(int i(a), _b(b); i <= _b; i += x )
#define rep(i, n) _rep( i, 0, n - 1, 1 )
#define rrep(i, a, b) for(int i(a),_b(b); i >= (_b); --i)
#define xrep( i, a, b ) _rep(i, a, b, 1)
#define foreach(type, v, it) for(type::iterator it = v.begin(); it!=v.end(); ++it)

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

#define dbg(x) if(DEBUG) cerr << __LINE__ << ": " << #x << " -> " << (x) << "\t";
#define dbge(x) if(DEBUG) cerr << __LINE__ << ": "<<#x << " -> " << (x) << endl;


typedef vector <int> vi;

// She
// May be the reason I survive
// The why and wherefore I'm alive
// The one I'll care for through the rough in ready years

//...


LL cost[1005];
bool ok[1005][1005];
LL G[1005];
int main()
{
	LL ans = 0;
	int t, n, r, k;
	//ifstream in("f:\\bin.txt");
	freopen("f:\\data\\C-small-attempt1.in.txt","r",stdin);
	freopen("f:\\data\\cout1.txt","w",stdout);
	//ofstream out("f:bout.txt");

	//streambuf *inbuf = std::cin.rdbuf(in.rdbuf());

	scanf("%d",&t);
	
	
	xrep(ca,1,t)
	{
		scanf("%d %d %d",&r, &k, &n);

		rep(i,n) scanf("%I64d", &G[i]);
		ms(ok,0);
		ms(cost,0);
		LL sum = 0, cum = 0;
		
		int i = 0, last = -1;
		int times = 0;

		while (times<r)
		{
			if (i == last || sum + G[i] > (LL)k)
			{
		
				if (last<0) break;
				//if (ok[last][i]) break;
				//ok[last][i] = true;				
				cum += sum;
				times++;
				//cost[++times] = cum;
				sum = 0;
				last = i;
			} 
			
			if (last == -1) last = 0;	
			
			sum += G[i];
			i = (i + 1) % n;
		}
	/*	if (r <= times) ans = cost[r];
		else
		{
			ans = (r/times)*cost[times]+ cost[r%times];
		}*/
		ans = cum;
		cout<<"Case #"<<ca<<": "<<ans<<endl;
	}
	
	
	return 0;
}
