
#include <stdio.h>

#include<string>
#include<map>

using namespace std;



main() {

  
  int T;

  char line[100];

  scanf("%d",&T);
  int length[100];
  
  
  for (int t = 1; t <= T; t++) {

    int N = 0;

    scanf("%d",&N);

    for (int i = 0; i <= N; i++)
      length[i] = 0;
    

    for (int i = 1; i <= N; i++) {
      scanf("%s",line);
      int l = 0;
      for (int p = 0; p < N; p++) {
	if (line[p]=='1')
	  l = p+1;
      }
      length[i] = l;
    }

    int result = 0;
    for (int i = 1; i <= N; i++) {
      if (length[i] > i) {
	int j;
	for (j = i+1; (j <= N) && (length[j] > i) ; j++);

	int l = length[j];
	for (int k = j; k > i; k--) {
	  result++;
	  length[k] = length[k-1];
	}
	length[i] = l;	
      }
    }

    printf("Case #%d: %d\n",t,result);
    
  }





}
