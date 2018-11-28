#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxr = 500;
const int maxc = 500;

struct vec {
  long x, y;

  vec(long xx, long yy) : x(xx), y(yy) {}
  vec() : x(0), y(0) {}

  vec& operator-=(vec b) {
    x -= b.x;
    y -= b.y;
    return *this;
  }

  vec& operator+=(vec b) {
    x += b.x;
    y += b.y;
    return *this;
  }
};

vec operator-(vec a, vec b){
  return a-=b;
}

vec operator+(vec a, vec b){
  return a+=b;
}

vec operator*(long c, vec a){
  return vec(c * a.x, c* a.y);
}

bool operator==(vec a, vec b) {
  return (a.x == b.x) && (a.y == b.y);
}


int r, c, d;
int grid[maxr][maxc];
vec sum[maxr+1][maxc+1];
long sumj[maxr+1][maxc+1];


int main() {
  int t;
  cin >> t;
  //  cerr << sizeof(int) << ' ' << sizeof(long) << '\n';
  for(int tcase=1;tcase<=t;tcase++){

    int r, c, d;

    cin >> r >> c >> d;

    for(int i=0;i<r;i++)
      for(int j=0;j<c;j++){
	char cur;
	cin >> cur;
	grid[i][j] = cur - '0';
      }

    for(int j=0;j<=c;j++){
      sum[0][j] = vec(0, 0);
      sumj[0][j] = 0;
    }

    for(int i=1;i<=r;i++){
      sum[i][0] = vec(0, 0);
      sumj[i][0] = 0;
      for(int j=1;j<=c;j++){
	sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + grid[i-1][j-1] * vec(i-1,j-1);
	sumj[i][j] = sumj[i-1][j] + sumj[i][j-1] - sumj[i-1][j-1] + grid[i-1][j-1];
      }
    }
      
    int sol = 0;
    
    for(int k=3;k<=min(r, c);k++)
      for(int i=0;i<=r-k;i++)
	for(int j=0;j<=c-k;j++){
	  vec alpha = sum[i+k][j+k]-sum[i][j+k]-sum[i+k][j]+sum[i][j];
	  alpha -= grid[i][j] * vec(i, j) + grid[i+k-1][j]*vec(i+k-1, j)  + grid[i][j+k-1]*vec(i, j+k-1)  + grid[i+k-1][j+k-1]*vec(i+k-1, j+k-1);
	  long beta = sumj[i+k][j+k]-sumj[i][j+k]-sumj[i+k][j]+sumj[i][j];
	  beta -= grid[i][j] + grid[i+k-1][j] + grid[i][j+k-1] + grid[i+k-1][j+k-1];
	  if(beta*vec(i*2+k-1,j*2+k-1) == 2*alpha)
	    sol = k;
	}
    if(sol)
      cout << "Case #" << tcase << ": " << sol << '\n';
    else
      cout << "Case #" << tcase << ": IMPOSSIBLE\n";
  }
}
