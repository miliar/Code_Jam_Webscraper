
#include <stdio.h>

int sumX[501][501];
int sumY[501][501];
int sumW[501][501];

int x[500][500];
int y[500][500];

char weight[500][500];


int solveCase() {
  int r, c, d;
  scanf("%d %d %d", &r, &c, &d);
//  printf("r: %d; c : %d\n", r, c);
  for(int i=0;i<r;i++) {
  scanf(" ");
    for(int j=0;j<c;j++) {
      scanf("%c", &weight[i][j]); weight[i][j] -= '0'; }
   }
  for(int i=0;i<r;i++)
    for(int j=0;j<c;j++) {
      x[i][j] = j * weight[i][j];
      y[i][j] = i * weight[i][j];
    }
  for(int i=0;i<=r;i++)
    for(int j=0;j<=c;j++) {
      if(i == 0 || j == 0)
        sumX[i][j] = sumY[i][j] = sumW[i][j] = 0;
      else {
        sumX[i][j] = sumX[i-1][j] + sumX[i][j-1] - sumX[i-1][j-1] + x[i-1][j-1];
        sumY[i][j] = sumY[i-1][j] + sumY[i][j-1] - sumY[i-1][j-1] + y[i-1][j-1];
        sumW[i][j] = sumW[i-1][j] + sumW[i][j-1] - sumW[i-1][j-1] + weight[i-1][j-1];
      }
    }
//  printf("sumX[6][6]: %d; sum[1][1]: %d; sum[1][6]: %d; sum[6][1]: %d\n", sumX[6][6], sumX[1][1], sumX[1][6], sumX[6][1]);
  for(int size=500;size>=3;size--)
    for(int i=0;i<=r-size;i++)
      for(int j=0;j<=c-size;j++) {
        int sqsX = sumX[i+size][j+size] - sumX[i][j+size] - sumX[i+size][j] + sumX[i][j];
        int sqsY = sumY[i+size][j+size] - sumY[i][j+size] - sumY[i+size][j] + sumY[i][j];
        int sqsW = sumW[i+size][j+size] - sumW[i][j+size] - sumW[i+size][j] + sumW[i][j];
        
//        if(i==1 && j==1)
//          printf("precut: %d: %d %d\n", size, sqsX, sqsY);
        sqsX -= (x[i][j] + x[i+size-1][j] + x[i][j+size-1] + x[i+size-1][j+size-1]);
        sqsY -= (y[i][j] + y[i+size-1][j] + y[i][j+size-1] + y[i+size-1][j+size-1]);
        sqsW -= (weight[i][j] + weight[i+size-1][j] + weight[i][j+size-1] + weight[i+size-1][j+size-1]);
        
        int expectedX = sqsW * (j*2 + (size-1));
        int expectedY = sqsW * (i*2 + (size-1));
        if(expectedX % 2 == 1) continue;
        if(expectedY % 2 == 1) continue;
        expectedX /= 2;
        expectedY /= 2;
        
//        if(i==1 && j==1)
//          printf("sz: %d: %d %d vs %d %d \n", size, sqsX, sqsY, expectedX, expectedY);
        if(expectedX == sqsX && expectedY == sqsY)
          return size;
      }
  return -1;
}

int main(){
    int tc = 0;
    scanf("%d", &tc);
    
    for(int ti=0;ti<tc;ti++) {
        printf("Case #%d: ", ti+1);
        int res = solveCase();
        if(res == -1)
          printf("IMPOSSIBLE\n");
        else
          printf("%d\n", res);
    }
}

