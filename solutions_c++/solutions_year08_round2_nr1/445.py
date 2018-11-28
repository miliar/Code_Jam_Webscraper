#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <queue>
#include <vector>
#include <cstdio>
#include <map>
#include <math.h>
#include <stack>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})
#define For(i,a,b) for(i=a;i!=b;i++)
#define Rep(i,n) For(i,0,n)
#define set(a,c) memset(a,c,sizeof(a))
#define pb push_back
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ii> vii;
typedef vector<vi> vvi;
long long x[100010], y[100010];
long long points[3][3];
int main() {
  int N = GI;
  int test,i,j;
  Rep(test,N) {
    set(points,0);
    int n = GI;
    int A = GI, B = GI, C = GI, D = GI;
    x[0] = GI, y[0] = GI;
    int M = GI;
    points[x[0]%3][y[0]%3]++;
    
    For(i,1,n) {
      x[i] = (x[i-1]*A)%M + B;
      x[i] = x[i]%M;
      y[i] = (y[i-1]* C)%M +D;
      y[i] = y[i]%M;
      points[x[i]%3][y[i]%3]++;
    }
    long long num = 0;
    num += points[0][0]*points[0][1]*points[0][2];
    num += points[0][0]*points[1][0]*points[2][0];
    num += points[1][0]*points[1][1]*points[1][2];
    num += points[0][1]*points[1][1]*points[2][1];
    num += points[2][0]*points[2][1]*points[2][2];
    num += points[0][2]*points[1][2]*points[2][2];

    num += points[0][0]*points[1][1]*points[2][2];
    num += points[0][0]*points[1][2]*points[2][1];

    num += points[0][1]*points[1][0]*points[2][2];
    num += points[0][1]*points[1][2]*points[2][0];

    num += points[0][2]*points[1][0]*points[2][1];
    num += points[0][2]*points[1][1]*points[2][0];
    
    
    Rep(i,3) {
      Rep(j,3) {
	long long c = points[i][j];
	c = (c*(c-1)*(c-2))/6;
	num += c;
      }
    }
    cout << "Case #" << test+1 << ": " << num << endl;
  }
}
