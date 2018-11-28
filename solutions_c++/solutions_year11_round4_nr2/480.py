#include <cstdio>
#include <cstdlib>

using namespace std;

long long dif[555][555];
long long sum[555][555];
long long pondx[555][555];
long long pondy[555][555];

int min(int a, int b){
  return (a<b?a:b);
}

bool cmx(int ax, int ay, int k){
  int bx = ax+k;
  int by = ay+k;
  long long px = pondx[bx][by];
  long long sw = sum[bx][by];
  if (ax>0){
    px-=pondx[ax-1][by];
    sw-=sum[ax-1][by];
  }
  if (ay>0){
    px-=pondx[bx][ay-1];
    sw-=sum[bx][ay-1];
  }
  if (ax>0 && ay>0){
    px+=pondx[ax-1][ay-1];
    sw+=sum[ax-1][ay-1];
  }
  px -= ((dif[ax][ay]+dif[ax][by])*ax + (dif[bx][ay]+dif[bx][by])*bx);
  sw -= ((dif[ax][ay]+dif[bx][ay]) + (dif[ax][by]+dif[bx][by]));
  if (sw == 0){
    return (px == 0);
  }
  long long ans;
  if ((bx-ax)%2 == 0){
    if (px%sw != 0)
      return false;
    ans = px/sw;
    return (ans == (ax+bx)/2);
  }
  px *= 2;
  if (px%sw != 0)
    return false;
  ans = px/sw;
  return (ans == ax+bx);
}

bool cmy(int ax, int ay, int k){
  int bx = ax+k;
  int by = ay+k;
  long long py = pondy[bx][by];
  long long sw = sum[bx][by];
  if (ax>0){
    py-=pondy[ax-1][by];
    sw-=sum[ax-1][by];
  }
  if (ay>0){
    py-=pondy[bx][ay-1];
    sw-=sum[bx][ay-1];
  }
  if (ax>0 && ay>0){
    py+=pondy[ax-1][ay-1];
    sw+=sum[ax-1][ay-1];
  }

  py -= ((dif[ax][ay]+dif[bx][ay])*ay + (dif[ax][by]+dif[bx][by])*by);
  sw -= ((dif[ax][ay]+dif[bx][ay]) + (dif[ax][by]+dif[bx][by]));
  if (sw == 0){
    return (py == 0);
  }

 long long ans;
  if ((by-ay)%2 == 0){
    if (py%sw != 0)
      return false;
    ans = py/sw;
    return (ans == (ay+by)/2);
  }
  py *= 2;
  if (py%sw != 0)
    return false;
  ans = py/sw;
  return (ans == ay+by);
}

bool go(int r, int c){
  for (int k = min(r,c)-1; k >= 2; k--){
    for (int i = 0; i < r-k; i++){
      for (int j = 0; j < c-k; j++){
	if (cmx(i,j,k) && cmy(i,j,k)){
	  printf("%d\n", k+1);
	  return true;
	}
      }
    }
  }
  return false;
}

int main(){
  int t;
  

  scanf("%d", &t);
  for (int ka = 1; ka <=t; ka++){
    int r, c, d;
    scanf("%d %d %d", &r, &c, &d);
    for (int i = 0; i < r; i++){
      char buf[555];
      scanf("%s", buf);
      for (int j = 0; j < c; j++){
	dif[i][j] = buf[j]-'0';
      }
    }

    sum[0][0] = dif[0][0];
    pondx[0][0] = pondy[0][0] = 0;
    for (int i = 1; i < r;i++){
      sum[i][0] = sum[i-1][0]+dif[i][0];
      pondx[i][0] = pondx[i-1][0] + (dif[i][0]*i);
      pondy[i][0] = 0;
    }
    for (int j = 1; j < c; j++){
      sum[0][j] = sum[0][j-1]+dif[0][j];
      pondx[0][j] = 0;
      pondy[0][j] = pondy[0][j-1] + (dif[0][j]*j);
    }
    for (int i = 1; i < r; i++){
      for (int j = 1; j < c; j++){
	sum[i][j] = sum[i-1][j]-sum[i-1][j-1]+sum[i][j-1]+dif[i][j];
	pondx[i][j] = pondx[i-1][j]-pondx[i-1][j-1]+pondx[i][j-1]
	  +(dif[i][j]*i);
	pondy[i][j] = pondy[i-1][j]-pondy[i-1][j-1]+pondy[i][j-1]
	  +(dif[i][j]*j);
      }
    }

    /*for (int i = 0; i < r; i++){
      for (int j = 0; j < c; j++){
	printf("%lld ", pondx[i][j]);
      }
      printf("\n");
      }*/

    printf("Case #%d: ", ka);
    if (!go(r,c))
      printf("IMPOSSIBLE\n");
  }

  return 0;
}
