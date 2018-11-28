#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef long long LL;
typedef long double LD;

typedef vector<int> VI;


void sol(int cutest, LL N, LL M, LL A){

	for(LL p=0;p<=M;p++)
	for(LL q=0;q<=N;q++)

	for(LL xc=0;xc<=N;xc++)
	for(LL yc=0;yc<=M;yc++)
	
	{
		LL ar=p*xc+q*yc-p*q;
		if(ar!=A)
			continue;

		printf("Case #%d: 0 %I64d %I64d 0 %I64d %I64d\n",cutest, p, q, xc, yc);
		return;
	}
	printf("Case #%d: IMPOSSIBLE\n",cutest);
}

int main()
{

	int ttt;
	cin >> ttt;
	for(int cutest=1;cutest<=ttt;cutest++){
		LL N,M,A;
		cin >> N >> M >> A;
		
		sol(cutest, N,M,A);
		
	}

}
