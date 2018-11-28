#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;

#define MAX 550
#define eps 1e-12

int T;
int R,C,D;
char grid[MAX][MAX];
int weight[MAX][MAX];
double vectorSum[MAX][MAX][2];
double weightSum[MAX][MAX];

double wquery(int r, int c, int r2, int c2){
    //printf("r=%d c=%d r2=%d, c2=%d %.6f\n",r,c,r2,c2,weightSum[r2+1][c]);
    //cout<<weightSum[r][c]<<" "<<weightSum[r2+1][c]<<" "<<weightSum[r][c2+1]<<" "<<weightSum[r2+1][c2+1]<<endl;
    return weightSum[r][c] - weightSum[r2+1][c] - weightSum[r][c2+1] + weightSum[r2+1][c2+1];
}
double vxquery(int r, int c, int r2, int c2){
    return vectorSum[r][c][0] - vectorSum[r2+1][c][0] - vectorSum[r][c2+1][0] + vectorSum[r2+1][c2+1][0];
}
double vyquery(int r, int c, int r2, int c2){
    return vectorSum[r][c][1] - vectorSum[r2+1][c][1] - vectorSum[r][c2+1][1] + vectorSum[r2+1][c2+1][1];
}

int main(){
    scanf("%d",&T);
    for (int caseID = 1; caseID <= T; caseID++){
	scanf("%d%d%d",&R,&C,&D);
	for (int i = 0; i < R; i++){
	    scanf("%s",grid[i]);
	    for (int j = 0; j < C; j++){
		int d = (int)(grid[i][j]-'0');
		weight[i][j] = D + d;
	    }
	}
	memset(vectorSum, 0, sizeof vectorSum);
	memset(weightSum, 0, sizeof weightSum);
	
	for (int i = R-1; i >= 0; i--){
	    double wSum = 0;
	    double vSumx = 0, vSumy = 0;
	    for (int j = C-1; j >= 0; j--){
		wSum += weight[i][j];
		vSumx += j * weight[i][j];
		vSumy += i * weight[i][j];		
		//if (i == 2 && j == 1) cout<<"abc"<<weight[i][j]<<" "<<weight[i][j+1]<<" "<<wSum << " "<<weightSum[i+1][j]<<endl;
		if (i == R-1){
		    weightSum[i][j] = wSum;
		    vectorSum[i][j][0] = vSumx;
		    vectorSum[i][j][1] = vSumy;
		} else{
		    weightSum[i][j] = weightSum[i+1][j] + wSum;
		    vectorSum[i][j][0] = vectorSum[i+1][j][0] + vSumx;
		    vectorSum[i][j][1] = vectorSum[i+1][j][1] + vSumy;
		}
	    }
	}
	int K;
	bool can = false;
	for (K = 501; K >= 3 && !can; K--){
	    if (K > R || K > C) continue;	    
	    for (int i = 0; i < R-K+1; i++)
		for (int j = 0; j < C-K+1; j++){
		    //if (K == 3)// && i == 1 && j == 1)
			//cout<<wquery(i,j,i+1,j+1)<<endl;
		    double xC = (double)(j + j + K - 1)/2.0;
		    double yC = (double)(i + i + K - 1)/2.0;
		    
		    double x = vxquery(i,j,i+K-1,j+K-1);
		    double y = vyquery(i,j,i+K-1,j+K-1);
		    
		    x -= xC*wquery(i,j,i+K-1,j+K-1);
		    y -= yC*wquery(i,j,i+K-1,j+K-1);
		    
		    x -= ((double)j-xC)*weight[i][j];
		    y -= ((double)i-yC)*weight[i][j];
		    x -= ((double)j+K-1-xC)*weight[i][j+K-1];
		    y -= ((double)i-yC)*weight[i][j+K-1];
		    x -= ((double)j+K-1-xC)*weight[i+K-1][j+K-1];
		    y -= ((double)i+K-1-yC)*weight[i+K-1][j+K-1];
		    x -= ((double)j-xC)*weight[i+K-1][j];
		    y -= ((double)i+K-1-yC)*weight[i+K-1][j];
		    
		    if (fabs(x) < eps && fabs(y) < eps)
			can = true;
		    if (can) break;
		}
	    if (can) break;
	}
	printf("Case #%d: ",caseID);
	if (K < 3) printf("IMPOSSIBLE\n");
	else printf("%d\n",K);
    }
    return 0;    
}

