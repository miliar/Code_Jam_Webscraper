#include <cstring>
#include <iostream>
#include <sstream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <set>
#include <list>
#include <map>
#include <iterator>
#include <cctype>
#include <stack>
#include <cassert>
#include <cmath>
using namespace std;

#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define FALL(ii,vv) for (int (ii)=0; (ii)<(vv).size();(ii)++)
#define REP(ii,vv) for (int (ii)=0; (ii)<(vv); (ii)++)
#define ALL(a) a.begin(), a.end()
#define MP make_pair
#define PB push_back

typedef long long ll;
typedef pair<int,int> pii;

int n,k,R;
int when[1010],next[1010],t[1010];
long long ile[1010];
ll sum[1010];

int main(){
	int test;
	scanf("%d",&test);
	REP(tN,test){
		scanf("%d %d %d",&R,&k,&n);
		REP(i,n) scanf("%d",&t[i]),when[i]=-1;
		
		int start = 0;
		ll res = 0;
		
		when[start]=0;
		int ilosc_kolejek = 0;
		
		while(true){
			if (R==ilosc_kolejek) break;
			int i=start;
			
			ilosc_kolejek++;
			ile[start]=0;
			
			while(ile[start] + t[i] <= k){
				ile[start] += t[i];
				i++;
				if (i==n) i=0;
				if (i == start) break;
			}
			
			res+=ile[start];
			next[start] = i;
			
			if (when[i]!=-1){
				start = i;
				break;
			}
			
			sum[i] = res;
			when[i] = ilosc_kolejek;
			start = i;
		}
		
		if( R != ilosc_kolejek){
			int cycle_length = ilosc_kolejek - when[start];
			ll cycle_cost = res - sum[start];
		
			R -= ilosc_kolejek;
		
			int okrazenia = R / cycle_length;
			R = R - cycle_length * okrazenia;
			res += cycle_cost * okrazenia;
		
			while(R--){
				res += ile[start];
				start = next[start];
			}
		}
		printf("Case #%d: %lld\n",tN+1,res);
	}
	return 0;
}
