/*
INPUT:

R k N


3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

OUTPUT:
Case #1: 21
Case #2: 100
Case #3: 20

*/

#include <iostream>
#include <cstdio>

using namespace std;

int t, r, k, n, nji[1010], j, loc;

int data[1010][2]; //where, 2 go, number

long long stevec;

int main(){
  
  scanf("%d", &t);
  
  for(int tt=0;tt<t;tt++){
  
    stevec = 0;
    loc=0;
    
    scanf("%d %d %d", &r, &k, &n);
    for(int i=0;i<n;i++)
      scanf("%d", &nji[i]);
    
    for(int i=0;i<n;i++){
      data[i][1] = nji[i];
      for(j=i+1;j!=i;j++){
	if(j==n) j=0;
	if(j==i) break;
	if(data[i][1] + nji[j] <= k){
	  data[i][1] += nji[j];
	} else {
	  break;
	}
      }
      data[i][0] = j;
    }
    
    for(int i =0;i<r;i++){
      stevec = stevec + data[loc][1];
      loc = data[loc][0];
    }
    
    printf("Case #%d: %lld\n", tt+1, stevec);
  
  }
  
  return 0;
}