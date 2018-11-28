#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#define MP make_pair
#define ST first
#define ND second
#define PII pair<int,int>
#define PB push_back
#define VII vector<int>
#define VIT vector<int>::iterator
#define LL long long

using namespace std;


int num_cases, n;
double res[150];
double WP[150];
double OWP[150];
double OOWP[150];
int games[150];

char tab[150][150];

int main(){
  scanf("%d", &num_cases);
  
  for(int tc = 1; tc <= num_cases; tc++){
      scanf("%d", &n);
      for(int i = 0; i < n; i++){
	  res[i] = WP[i] = OWP[i] = OOWP[i] = 0.0;
	  scanf("%s", tab[i]);
      }
      for(int i = 0; i < n; i++){
	  games[i] = 0;
	  for(int j = 0; j < n; j++){
	      if(tab[i][j] != '.'){
		  games[i]++;
		  WP[i] += ((tab[i][j] == '1')?(1.0):(0.0));
	      }
	  }
	  WP[i] /= (1.0 * games[i]);
	  res[i] += 0.25 * WP[i];
      }
      
      for(int i = 0; i < n; i++){
	  for(int j = 0; j < n; j++){
	      if(tab[i][j] != '.'){
		  OWP[i] += (WP[j] * games[j] - ((tab[i][j] == '1')?(0.0):(1.0)))/(1.0 * (games[j] - 1));
	      }
	  }
	  OWP[i] /= (1.0 * games[i]);
	  res[i] += 0.5 * OWP[i];
      }
      
      for(int i = 0; i < n; i++){
	  for(int j = 0; j < n; j++){
	      if(tab[i][j] != '.'){
		  OOWP[i] += OWP[j];
	      }
	  }
	  OOWP[i] /= (1.0 * games[i]);
	  res[i] += 0.25 * OOWP[i];
      }
      
    
      printf("Case #%d:\n", tc);
      for(int i = 0; i < n; i++){
	  printf("%.7lf\n", res[i]);
      }
  }
  
  return 0;
}