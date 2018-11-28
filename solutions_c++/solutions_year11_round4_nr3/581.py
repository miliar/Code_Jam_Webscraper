#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <bitset>

using namespace std;

int prime[1000002];
int h = 0;
bitset<1000100> pirminis;

void retis(){
  for(int i = 0; i <= 1000090; i++)
    pirminis[i] = true;
  for(int i = 2; 2*i <= 1000090; i++)
    if(pirminis[i])
      for(int j = 2; i*j <= 1000090; j++)
	pirminis[i*j] = false;
      
  for(int i = 2; i <= 1000090; i++)
    if(pirminis[i])
      prime[h++] = i;
    
  //for(int i = 0; i < h; i++)
  //  cout << prime[i] << endl;
}

void solve(int test){
  int times[90000];
  fill(times, times + 90000, 0);
  
  int n;
  scanf("%d", &n);
  
  for(int j = 1, i = 1; j <= n; j++, i = j)
    for(int y = 0; y < h && prime[y] <= i; y++){
      int p = 0;
      while(i % prime[y] == 0){
	//cout << i << " " << prime[y] << " " << i / prime[y] << endl;
	p++;
	i = i / prime[y]; 
      }
      times[y] = max(times[y], p);
    }
    
  int ats = 0;
  for(int i = 0; i <= h; i++)
    if(times[i] != 0)
      ats += times[i]-1;
  if(n != 1)
    ats += 1;
    
  printf("Case #%d: %d\n", test, ats);
}

int main(){
  retis();
  int testcases;
  scanf("%d", &testcases);
  for(int test = 1; test <= testcases; test++)
    solve(test);
  
  return 0;
}