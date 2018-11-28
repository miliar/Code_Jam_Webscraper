#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(b);++i)

char W[600];
int PD[600][600];
int MOD = 10000;
int N;
string R = "welcome to code jam";

int main()
{
	gets(W);
	sscanf(W,"%d",&N);
	for(int t=0; t<N; ++t){
		gets(W);
		int len = strlen(W);
		memset(PD,0,sizeof(PD));
		FOR(i,0,len+1) PD[0][i] = 1;

		FOR(i,1,R.size()+1)
				FOR(j,1,len+1) {
					if(R[i-1] != W[j-1])
						PD[i][j] = PD[i][j-1];
					else
						PD[i][j] = PD[i][j-1] + PD[i-1][j-1];
					PD[i][j] %= MOD;
				}
		printf("Case #%d: %04d\n",1+t,PD[R.size()][len]);

	}
	return 0;
}
