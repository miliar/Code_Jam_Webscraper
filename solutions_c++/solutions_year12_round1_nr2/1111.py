#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	
  scanf("%d", &T);
  //printf("T: %d\n", T);
	
	for (int t=1; t<=T; t++) { 
	  //printf("t: %d\n", t);
    int N; 
    int one[1001];
    int two[1001];
    int visited_one[1001];
    int visited_two[1001];
    int stars = 0;
    int steps = 0;
    memset(visited_one, 0, 1001);
    memset(visited_two, 0, 1001);
    
    scanf("%d", &N);
    //printf("N: %d\n", N);
   	for (int n=1; n<=N; n++) { 
   	  scanf("%d %d", &one[n], &two[n]);
   	}
   	
   	//printf("done");

    while (true) {
      int tmp = stars;
      
     	for (int n=1; n<=N; n++) { 
     	  if (visited_two[n] == 1)
     	    continue;
     	    
     	  if (two[n] <= stars) {
     	    //printf("stars: %d | 2-star level %d\n", stars, n);
     	    steps++;
     	    visited_two[n] = 1;
     	    
     	    if (visited_one[n] == 1)
       	    stars++;
       	  else
       	    stars += 2;
     	  }
     	}
     	
     	if (stars != tmp) continue;
     	
     	int max_two = -100000; // minus infinite
     	int max_idx = -1;
     	for (int n=1; n<=N; n++) { 
     	  if ((visited_one[n] == 1) || (visited_two[n] == 1))
     	    continue;
     	    
     	  if (one[n] <= stars) {
          if (two[n] > max_two) {
            max_two = two[n];
            max_idx = n;
          }
     	  }
     	}
     	
     	if (max_idx != -1) {
       	//printf("stars: %d | 1-star level %d\n", stars, max_idx);
   	    steps++;
   	    stars++;
   	    visited_one[max_idx]++;
   	  }
     	
     	//printf("%d\n", stars);
     	if (stars == tmp) break;
    }
    
   	for (int n=1; n<=N; n++) { 
   	  if (visited_two[n] == 0) {
   	    printf("Case #%d: Too Bad\n", t);
   	    steps = -1;
   	    break;
   	  }
   	}
    
    if (steps != -1) {
      printf("Case #%d: %d\n", t, steps);
  	}
	}
	
  return 0;
}
