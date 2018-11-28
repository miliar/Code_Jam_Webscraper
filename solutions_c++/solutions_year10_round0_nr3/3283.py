#include <iostream>
#include <cmath>
#include <vector>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define PB(A,B) A.push_back(B);
#define VI vector<int>

using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0 Otpt.txt","w",stdout);

	int T,N,k,R;
	scanf("%d",&T);

	EFOR(cases,1,T){
		scanf("%d%d%d",&R,&k,&N);

		VI grps(N);
		FOR(inp,0,N)
			scanf("%d",&grps[inp]);

		long long fund=0;

		EFOR(trip,1,R){
			long long sum=0;
			for(int sel=0;sel<N && sum+grps[0]<=k;sel++){
				sum+=grps[0];
				int tmp=grps[0];
				grps.erase(grps.begin());
				PB(grps,tmp);
			}
			fund+=sum;
		}

		printf("Case #%d: %lld\n",cases,fund);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
