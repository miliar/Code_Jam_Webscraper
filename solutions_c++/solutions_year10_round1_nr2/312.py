#include<algorithm>
#include<stdlib.h>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<string.h>
#include<time.h>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#include<iostream>
using namespace std;

const int INF = (1<<25);

int main(){
	freopen("C:\\Users\\zgm\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\zgm\\Desktop\\out.txt","w",stdout);
	int T, D, L, M, N, a[108], d[101][256];
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d%d%d%d",&D,&L,&M,&N);
		int res = INF;
		for(int i=0; i<N; i++){
			scanf("%d",&a[i]);
			for(int k=0; k<256; k++) d[i][k] = INF;
			d[i][a[i]] = D*i;
			for(int k=0; k<256; k++){
				d[i][k] = d[i][a[i]]+abs(k-a[i]);
				for(int j=i-1; j>=0; j--){
					for(int r=0; r<256; r++){
						if( d[j][r]==INF ) continue;
						int w = d[j][r]+D*(i-j-1)+abs(k-a[i]);
						int dif = abs(k-r);
						if( dif>M ){
							if( M==0 ) w = INF;
							else if( dif%M==0 ) w += (dif/M-1)*L;
							else w += (abs(k-r)/M)*L;
						}
						d[i][k] = min( d[i][k], w );
					}
				}
				//if( k<7 ) printf("%d %d %d\n",i,k,d[i][k]);
				res = min( res, d[i][k]+(N-i-1)*D );
			}
		}
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}
