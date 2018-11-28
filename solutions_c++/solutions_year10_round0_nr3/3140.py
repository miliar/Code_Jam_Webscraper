#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>

using namespace std;


int main(int argc,char **argv){
  
  int T;
	int N;
	long R;
	long k;
	//long gi;
	long gi[1000]; 
  char line[10*1000 + 1000];
  int index;
  unsigned long long Euro;

	//Red Number of test cases
	scanf("%d",&T);

	for(int i = 0;i<T;i++){

		//read R,K
		scanf("%ld %ld %d",&R,&k,&N);
    
	 	//read N
		
		for (int j =0; j < N; j++) {
      scanf("%s",line); 
      gi[j] = strtol(line,NULL,10);
    }
/*		char *p = strtok(line," ");
		for (int j =0; p; j++) {
	   p = strtok(NULL, " ");
     gi[j] = strtol(p,NULL,10);
		}*/

	  index = 0;
		Euro = 0;
    for(int r = 0;r<R;r++){
		  
		  int peopleCnt = 0;
		  for(int n=0; ( (gi[index] + peopleCnt) <= k) && n < N;n++ ) {

        peopleCnt += gi[index];
			  index= (index+1) % N;

			};
      
			Euro += peopleCnt;
		};

    printf("Case #%d: %llu\n",i+1,Euro);
	}

  return 0;
}
