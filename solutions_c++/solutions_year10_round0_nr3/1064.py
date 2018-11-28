#include <cstdio>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <math.h>
#include <limits.h>
#include <float.h>
#include <algorithm>
#include <iostream>

using namespace std;

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
typedef __int64 LL;
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define FORR(a,s,b) for(int a=s;a<=b;a++)
#define CLR(a,b) memset(a,b,sizeof(a))
#define VI vector<int>
#define VS vector<string>

int main()
{
	int t;
	cin >> t;

	FORR(cn,1,t) {
		cout << "Case #"<<cn<<": ";

		int rounds,capacity,n;
		cin >> rounds >> capacity >> n;

		int gi[1024],MoveTo[1024],MoneyTo[1024],MoneyBefore[1024];
		FOR(i,n) cin >> gi[i];

		LL sum = accumulate(gi,gi+n,0LL );

		LL money=0;
		int start=0;
		int t=1;

		if(capacity>=sum) {
			money = rounds*LL(sum);

		} else {
			// Possible to be O(N) but isn't really needed
			FOR(start,n) {
				int Free=capacity % sum;
				int i=start;
	
				FOR(rep,n) {
					if(Free<gi[i]) break;
					Free-=gi[i]; if(++i==n) i=0;
				}
				MoveTo[start]=i;
				MoneyTo[start]=capacity-Free;
			}
	
			int was[1024]={0};

			while(rounds && was[start] ==0) {
	            rounds--;
				was[start]=t++;
				MoneyBefore[start]=money;
	
				money+=MoneyTo[start];
				start=MoveTo[start];
			}
	
			div_t q = div( rounds, t-was[start] );
			money += q.quot * LL(money - MoneyBefore[start]);
			rounds = q.rem;

			while(rounds--) {
				money+=MoneyTo[start];
				start=MoveTo[start];
			}

		}


		cout << money << "\n";
	}

	return 0;
}
