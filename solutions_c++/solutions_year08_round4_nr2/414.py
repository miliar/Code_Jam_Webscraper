#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <boost/foreach.hpp>

using namespace std;
using namespace boost;

int tran(int x1, int y1, int x2, int y2, int x3, int y3)
{
	return abs((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1));
}
int main()
{
	int caseN;
	int N,M,A;
	scanf("%d", &caseN);
	for(int cc=0; cc<caseN;cc++){
		scanf("%d %d %d", &N, &M, &A);
		int i;
		for(i=0;i<=N;i++){
			for(int j=0;j<=N;j++){
				for(int k=0;k<=M;k++){
					for(int l=0;l<=M;l++){
						if( A == tran( 0, 0, i, k, j, l) ){
							printf("Case #%d: %d %d %d %d %d %d\n", cc+1, 0, 0, i, k, j, l);
							goto end;
						}
					}
				}
			}
		}
end:
		if( i != N + 1){
		}else{
			printf("Case #%d: IMPOSSIBLE\n", cc+1);
		}
	}
	return 0;
}
