#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

char mat[600][600];
long long sumX[600][600], sumY[600][600], sumM[600][600];

int main(){
	int caso = 1;
	int casos;
	int R,C,D;
	
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		scanf("%d%d%d", &R, &C, &D);
		
		for(int i = 0; i < R; i++){
			scanf("%s", mat[i]);
		}
		
		for(int i = 0; i < R; i++){
			for(int j = 0; j < C; j++){
				sumX[i][j] = (D+mat[i][j]-'0')*((long long)(i+i+1));
				if(i > 0)
					sumX[i][j] += sumX[i-1][j];	
				if(j > 0)
					sumX[i][j] += sumX[i][j-1];
				if(i > 0 && j > 0)
					sumX[i][j] -= sumX[i-1][j-1];
				
				sumY[i][j] = (D+mat[i][j]-'0')*((long long)(j+j+1));
				if(i > 0)
					sumY[i][j] += sumY[i-1][j];	
				if(j > 0)
					sumY[i][j] += sumY[i][j-1];
				if(i > 0 && j > 0)
					sumY[i][j] -= sumY[i-1][j-1];
				
				
				sumM[i][j] = (D+mat[i][j]-'0');
				if(i > 0)
					sumM[i][j] += sumM[i-1][j];	
				if(j > 0)
					sumM[i][j] += sumM[i][j-1];
				if(i > 0 && j > 0)
					sumM[i][j] -= sumM[i-1][j-1];
				//printf("%d %d = %lld\n",i,j,sumX[i][j]);
			}
		}	
		
		int res = -1;
		int menor = min(R,C);
		
		for(int k = 3; k <= menor; k++){
			bool achei = false;
			for(int i = 0; i + k-1 < R && !achei; i++){
				for(int j = 0; j + k-1 < C && !achei; j++){
					long long xx,yy, massa;
					xx = sumX[i+k-1][j+k-1];
					
					if(i > 0)
						xx -= sumX[i-1][j+k-1];
					if(j > 0)
						xx -= sumX[i+k-1][j-1];
					if(i > 0 && j > 0)
						xx += sumX[i-1][j-1];
					yy = sumY[i+k-1][j+k-1];
					if(i > 0)
						yy -= sumY[i-1][j+k-1];
					if(j > 0)
						yy -= sumY[i+k-1][j-1];
					if(i > 0 && j > 0)
						yy += sumY[i-1][j-1];
					massa = sumM[i+k-1][j+k-1];
					if(i > 0)
						massa -= sumM[i-1][j+k-1];
					if(j > 0)
						massa -= sumM[i+k-1][j-1];
					if(i > 0 && j > 0)
						massa += sumM[i-1][j-1];
					
					xx -= (D+mat[i][j]-'0')*((long long)(i+i+1));
					xx -= (D+mat[i+k-1][j]-'0')*((long long)(i+k-1+i+k));
					xx -= (D+mat[i][j+k-1]-'0')*((long long)(i+i+1));
					xx -= (D+mat[i+k-1][j+k-1]-'0')*((long long)(i+k-1+i+k));
					
					yy -= (D+mat[i][j]-'0')*((long long)(j+j+1));
					yy -= (D+mat[i+k-1][j]-'0')*((long long)(j+j+1));
					yy -= (D+mat[i][j+k-1]-'0')*((long long)(j+k-1+j+k));
					yy -= (D+mat[i+k-1][j+k-1]-'0')*((long long)(j+k-1+j+k));
					
					massa -= (D+mat[i][j]-'0');
					massa -= (D+mat[i+k-1][j]-'0');
					massa -= (D+mat[i][j+k-1]-'0');
					massa -= (D+mat[i+k-1][j+k-1]-'0');
					
				//	printf("%d,%d e k = %d => %lld,%lld\n",i,j,k,xx,yy);
					
					if(xx == (i+i+k)*massa && yy == (j+j+k)*massa){
						res = k;
						achei = true;
					}
				}
			}	
		}
		if(res != -1)
			printf("Case #%d: %d\n", caso++, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", caso++);
	}
	
	return 0;
}
