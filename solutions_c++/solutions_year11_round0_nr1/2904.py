/*
** In the name of God **
*/
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
#include <stdio.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define EPS 1e-8
#define MOD 1000000007
#define INF 100000000
#define SQR(a) ((a)*(a))
#define pb push_back
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define ORANGE true
#define BLUE false
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tnum,n;
	vector<pair<char,int> >a;
	vector<int>O;
	vector<int>B;
	
	scanf("%d",&tnum);
	
	FOR(q,1,tnum+1)
	{
		scanf("%d",&n);
		a.clear();
		a.resize(n);
		FR(i,n) 
			scanf(" %c %d",&a[i].first,&a[i].second);
		O.clear();B.clear();
		FR(i,n)
			if(a[i].first=='B') B.push_back(a[i].second);
			else O.pb(a[i].second);
		int curO=1,curB=1;
		int idxO=0;int idxB=0;int idx=0;
		bool token=a[idx].first=='B'?BLUE:ORANGE;
		int sec=0;
		a.pb(make_pair('B',0));
		while(idx<n)
		{
			int dO,dB;
			if(idxO<O.size()) dO = O[idxO]-curO;
			else dO=0;
			if(idxB<B.size()) dB = B[idxB]-curB;
			else dB=0;
			if(token==BLUE)
			{
				if(abs(dB)>=abs(dO))
				{
					curO+=dO;
					sec += abs(dB)+1;
					curB+=dB;
					token = a[++idx].first=='B'?BLUE:ORANGE;
				}
				else
				{
					curO+=(dO/abs(dO))*(abs(dB)+1);
					token = a[++idx].first=='B'?BLUE:ORANGE;
					sec += abs(dB)+1;
					curB += dB;
				}//else
				idxB++;
			}
			else
			{
				if(abs(dO)>=abs(dB))
				{
					curB+=dB;
					sec+=abs(dO)+1;
					curO+=dO;
					token = a[++idx].first=='B'?BLUE:ORANGE;
				}
				else
				{
					curB+=(dB/abs(dB))*(abs(dO)+1);
					token = a[++idx].first=='B'?BLUE:ORANGE;
					sec += abs(dO)+1;
					curO += dO;
				}
				idxO++;
			}//else
		}//while
		printf("Case #%d: %d\n",q,sec);

	}
}