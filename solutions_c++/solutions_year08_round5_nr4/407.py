#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <map>
using namespace std;

int C[120][120];
const int MOD=10007;

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=0; t<T; t++){
    int H, W, R;
    scanf("%d %d %d", &H, &W, &R);
    set < pair<int, int> > rocks;
    for(int i=0; i<R; i++){
      pair <int, int> x;
      scanf("%d%d", &x.first, &x.second);
      rocks.insert(x);
    }
    for(int i=H+2; i>=1; i--)
      for(int j=W+2; j>=1; j--) 
	C[i][j]=0;
	
    for(int i=H; i>=1; i--)
      for(int j=W; j>=1; j--){
	if(i==H and j==W) { C[i][j]=1; continue; }
	if(rocks.find(make_pair(i, j))!=rocks.end()){
	  C[i][j]=0; continue;
	}
	C[i][j]=C[i+1][j+2]+C[i+2][j+1];
	C[i][j]%=MOD;
      }
    printf("Case #%d: %d\n", t+1, C[1][1]);
  }
  return 0;
}
