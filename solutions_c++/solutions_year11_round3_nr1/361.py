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


int num_cases;
int n, m;

char tab[60][60];

int main(){
  scanf("%d", &num_cases);
  
  for(int tc = 1; tc <= num_cases; tc++){
      bool possible = true;
      scanf("%d %d", &n, &m);
      printf("Case #%d:\n", tc);
      for(int i = 0; i < n; i++) scanf("%s", tab[i]);
      
      for(int i = 0; i < n; i++){
	  for(int j = 0; j < m; j++){
	      if(tab[i][j] == '#'){
		  if(j < m-1 && i < n-1 && tab[i][j+1] == '#' && tab[i+1][j] == '#' && tab[i+1][j+1] == '#'){
		      tab[i][j] = '/';
		      tab[i][j+1] = '\\';
		      tab[i+1][j] = '\\';
		      tab[i+1][j+1] = '/';
		  }
		  else{
		      possible = false;
		      break;
		  }
	      }
	  }
	  if(!possible) break;
      }
      
      if(possible){
	for(int i = 0; i < n; i++){
	    for(int j = 0; j < m; j++){
		printf("%c", tab[i][j]);
	    }
	    printf("\n");
	}
      }
      else{
	  printf("Impossible\n");
      }
  }
  
  return 0;
}