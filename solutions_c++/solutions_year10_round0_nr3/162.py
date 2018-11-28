#include <stdio.h>

main() {

  int T;
  
  int group[10000];
  
  int sum[10000]; // sum starting at pos i

  int next[10000]; // next begin, if we start at pos i

  scanf("%d",&T);

  for (int i = 1; i <= T; i++) {
    int r,k,n;
    
    scanf("%d %d %d",&r,&k,&n);
    
    for (int g = 0; g < n; g++) {
      scanf("%d",&group[g]);
    }
    

    int people = 0;
    
    int end = 0;
    for (int start = 0; start < n; start++) {
      if (start != 0) {
	// remove previous start value;
	people -= group[start-1];
      }
      
      // now add people from end, while they fit;
      
      while ((people + group[end]  <= k)) {
	people += group[end];
	
	end = (end + 1 )%n ;
	
	if (end == start) {
	  // everyone fits;
	  break;
	}
      }
      
      sum[start] = people;
      next[start] = end;
    }
    
    int pos = 0;

    long long int total = 0;

    for (int ride = 0; ride < r; ride++) {
      
      total += sum[pos];
      pos = next[pos];

    }

    printf("Case #%d: %lld\n",i,total);


  }



}
