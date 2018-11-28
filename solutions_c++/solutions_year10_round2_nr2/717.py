#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <algorithm>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <ctime>
#include <cmath>
#include <numeric>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define REP(i,b) For(i,1,b)

int main(int argc, char* argv[])
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int NumTest;
	scanf("%d", &NumTest);

	For(iTest, 1, NumTest){
		int N,K,T;
		int64 B;
		scanf("%d %d %lld %d\n",&N,&K,&B,&T);
		vector<int64> locAll(N,(int64)0);
		For(i,0,N-1)
			scanf("%lld",&locAll[i]);
		vector<int64> velAll(N,(int64)0);
		For(i,0,N-1)
			scanf("%lld",&velAll[i]);

		vector<long double> timeAll(N,0);
		Ford(i,N-1,0){
			timeAll[i] =(long double)(((long double)(B-locAll[i])/(long double)velAll[i]));
		}
		int numTotal=0;
		int idx=N-1;
		int numSwap=0;
		while(idx>=0)
		{
			if(timeAll[idx]<=(long double)T){
				numTotal++;
				numSwap=numSwap+(N-idx-numTotal);
			}
			if(numTotal==K){
				break;
			}
			idx--;
		}
		if(K==0){
			printf("Case #%d: 0\n",iTest);
		}
		else {
			if(idx>=0){
				printf("Case #%d: %d\n", iTest,numSwap);
			}
			else{
				printf("Case #%d: IMPOSSIBLE\n",iTest);
			}
		}
	}
}