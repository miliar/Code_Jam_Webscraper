#pragma comment(linker,"/STACK:16777216")
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <locale>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long Ull;

#define VI vector <int>
#define FOR(i, a, b) for(int (i) = (a); (i) < (b); ++(i))
#define RFOR(i, a, b) for(int (i) = (a)-1; (i) >= (b); --(i))
#define CLEAR(a) memset((a), , sizeof(a))
#define INF 1000000000
#define PB push_back
#define ALL(c) (c).begin(),  (c).end()
#define pi 2*acos(0.0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define MOD 1000000007
#define EPS 1e-7
#define INF 2000000000


long long T,TT,n,W,L,r,h,w,H;
vector<pair<long long,long long> > R;
vector<pair<long long,pair<long long,long long> > > res1;
vector<pair<long long,pair<long long,long long> > > res2;
pair<long long,pair<long long,long long> > P;

int main()
{
	freopen("inputB.txt","r",stdin);
	freopen("outputB.txt","w",stdout);

	cin >> TT;
	FOR(T,0,TT)
	{
res1.clear();
res2.clear();
		R.clear();
		cin >> n >> W >> L;
		FOR(i,0,n)
		{
			cin >> r;
			R.PB(MP(r,i));
		}
		sort(ALL(R));
		reverse(ALL(R));
		
			/*
			...........
			.         .
			.         .
			...........
			*/
			 h = 0;
			 H = R[0].first;
			 w = R[0].first;
			P.second.first = 0;
			P.second.second = 0;
			P.first = R[0].second;
			res1.PB(P);
			long long i = 1;
			while (i<n)
			{
				while (w + R[i].first <= W)
				{
					if (!h)
						H = max(H,h+R[i].first);
					else
						H = max(H,h+2*R[i].first);
					P.second.first = w + R[i].first;
					P.second.second = h + (!h?0:R[i].first);
					P.first = R[i].second;
					res1.PB(P);
					w += R[i].first * 2;
					++i;
					if (i>=n)
						break;
				}
				
					if (i>=n)
						break;
				w = R[i].first * (-1);
				h = H;
			}



		
		
			/*
			...
			. .
			. .
			. .
			...
			*/
			 h = 0;
			 H = R[0].first;
			 w = R[0].first;
			P.second.first = 0;
			P.second.second = 0;
			P.first = R[0].second;
			res2.PB(P);

			 i = 1;
			while (i<n)
			{
				while (w + R[i].first <= L)
				{
					if (!h)
						H = max(H,h+R[i].first);
					else
						H = max(H,h+2*R[i].first);
					P.second.second = w + R[i].first;
					P.second.first = h + (!h?0:R[i].first);
					P.first = R[i].second;
					res2.PB(P);
					w += R[i].first * 2;
					++i;
					if (i>=n)
						break;
				}
				
					if (i>=n)
						break;
				w = R[i].first * (-1);
				h = H;
			}

		
		cout << "Case #" << T+1 << ":";
		if (res1[n-1].second.second < L)
		{
			//res1
			sort(ALL(res1));
			FOR(i,0,n)
				cout << " " << res1[i].second.first << " " << res1[i].second.second;
			cout << endl;
		}
		else
			if (res1[n-1].second.first < W)
		{
			//res2
			sort(ALL(res2));
			FOR(i,0,n)
				cout << " " << res2[i].second.first << " " << res2[i].second.second;
			cout << endl;
		}else
			cout <<"++++++++++++++++++++++++++++++++++++++++++++++++++++\n";
		
		//R.clear();

	}
	return 0;
}