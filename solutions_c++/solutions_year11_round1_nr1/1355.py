#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

bool solve(void)
{
	int N, PD, PG, i;

	scanf("%d%d%d", &N, &PD, &PG);
	
	if(PD<100 && PG==100) return  false;
	if(PD>0 && PG==0) return false;

	if(N>99){
		return true;
	}
	else {
		for(i=1; i<=N; i++)
			if(i*PD%100==0)
				break;
		if(i>N)  return false;
		return true;
	}
	return true;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int n, i;
	scanf("%d", &n);
	
	for(i=1; i<=n; i++){
		printf("Case #%d: ", i);
		puts(solve()?"Possible":"Broken");
	}

	return 0;
}