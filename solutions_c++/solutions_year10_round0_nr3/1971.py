#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>
#include <cctype>
#include <vector>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int,int> PI;
#define dbg(x) cerr << #x << " -> " << (x) << "\t";
#define dbge(x) cerr << #x << " -> " << (x) << "\n";
const int mn=2048;
LL R,N,G[mn] , Sum[mn],Size;
LL nxt[mn][32] , blockSum[mn][32];

int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		cin >> R >> Size >> N;	
		for ( int i=1;i<=N;i++ )
		{
			cin >> G[i];
			G[i+N] = G[i];
		}
		Sum[0] = 0;
		for ( int i=1;i<=2*N;i++ )
			Sum[i] = Sum[i-1] + G[i];

		for ( int ptr1 = 1 ; ptr1 <= N ; ptr1 ++ )
		{
			int lo,hi,mid;
			lo=ptr1 , hi = ptr1 + N-1;
			while ( lo < hi )
			{
				mid = (lo+hi+1)/2;
				if ( Sum[mid] - Sum[ptr1-1] <= Size )
					lo = mid;
				else
					hi = mid-1;
			}
			// ptr2 inclusive , ptr1 inclusive
			nxt[ptr1][0] = (lo+1 <= N ? lo+1 : lo - N + 1);
			blockSum[ptr1][0] = Sum[lo] - Sum[ptr1-1] ;
		}
		for ( int step=1;(1<<step)<=R;step ++ )
		{
			for ( int i=1;i<=N;i++ )
				nxt[i][step] = nxt[nxt[i][step-1]][step-1] , blockSum[i][step] = blockSum[i][step-1] + blockSum[nxt[i][step-1]][step-1];
		}
		LL ans = 0;
		int pres = 1;
		for ( int i=30;i>=0;i-- ) if (( R >> i )&1 )
		{
			ans += blockSum[pres][i];
			pres = nxt[pres][i];
		}
		cout <<"Case #" << kase <<": " << ans << endl;
	}
	return 0;
}
