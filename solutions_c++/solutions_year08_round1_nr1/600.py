#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;
using namespace __gnu_cxx;

int main() {
  int T;
  scanf("%d ", &T);
  for (int inst = 0; inst < T; inst++){
    int n;
    scanf("%d ", &n);
    vector<long long> x;
    vector<long long> y;
    int num;
    for (int i = 0; i < n; i++){
      scanf("%d ", &num);
      x.push_back(num);
    }
    for (int i = 0; i < n; i++){
      scanf("%d ", &num);
      y.push_back(num);
    }

    sort(x.begin(), x.end());
    sort(y.begin(), y.end());

    long long min = 0;

    int iX = 0;
    int fX = n-1;
    int iY = 0;
    int fY = n-1;
    
    int count = 0;

    while (count < n){
    
      if (x[fX] > y[fY]){
	min += x[fX]*y[iY];
	fX--;
	iY++;
      }
      else{
	min += x[iX]*y[fY];
	fY--;
	iX++;
      }
      count++;
    }
    printf("Case #%d: %Ld\n", inst+1, min);
  }
  return 0;
}
