#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 1000100;

int main(){
  //freopen("a.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  
  int testcases;
  scanf("%d", &testcases);
  
  long long boosters, statyba, n, b;
  int dist[MAXN];
  for(int test = 0; test < testcases; test++){
    long long total = 0;
    scanf("%lld %lld %lld %lld", &boosters, &statyba, &n, &b);
    for(int i = 0; i < b; i++)
      scanf("%d", &dist[i]);
    for(int i = 0, j = 0; j < n; i = (i + 1) % b, j++)
      dist[j] = dist[i];
    
    long long summa = (long long)0;
    for(int j = 0; j < n; j++)
      summa += (long long)dist[j]/0.5;
    
    int begin = n;
    for(int i = 0; i < n; i++){
      if(total + dist[i] / 0.5 < statyba)
	total += (long long)dist[i] / 0.5;
      else{
	dist[i] = dist[i] - ((statyba - total) / 2);
	//cout << statyba - total << endl;
	total = statyba;
	begin = i;
	break;
      }
    }
    
    sort(dist + begin, dist + n);
    
    for(int j = n-1, i = 0; j >= begin && i < boosters; j--, i++)
      summa -= (long long)dist[j];
    
    //for(int i = 0; i < n; i++)
    //  printf("%d ", dist[i]);  
    //cout << summa << endl;
    printf("Case #%d: %lld\n", test+1, summa);
  }
  
  return 0;
}