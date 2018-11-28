#include <iostream>
#include <cmath>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define PB(A,B) A.push_back(B);

using namespace std;

int main()
{
	freopen("A-large.txt","r",stdin);
	freopen("Otpt_1-Large.txt","w",stdout);

	int T,N,K;
	scanf("%d",&T);

	EFOR(cases,1,T){
		scanf("%d%d",&N,&K);

		if((K+1)%(2<<(N-1))==0)
				printf("Case #%d: ON\n",cases);
		else
				printf("Case #%d: OFF\n",cases);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
