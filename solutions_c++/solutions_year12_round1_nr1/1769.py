/*
 * main.cpp
 *
 *  Created on: 2011/09/24
 *      Author: taik
 */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <vector>
#include <algorithm>

typedef long long s64;

//#define debug_printf printf
#define debug_printf


int main(int argc,const char *argv[]){

  if (argc < 2){
    printf("Usage : %s input\n",argv[0]);
    return 0;
  }

  FILE *file = fopen(argv[1],"r");

  char line[65536];
  int tc; // test case
  const char *delim = " ";

  if(fgets(line,sizeof(line),file) == NULL){
    return 0;
  }
  tc = atoi(line);
  for(int i=0;i<tc;++i){
    printf("Case #%d: ",i+1);
    fgets(line,sizeof(line),file);
    char *cp = line;
    double A = (double)atoi(strtok(cp,delim));
    cp = NULL;
    double B = (double)atoi(strtok(cp,delim));

    double Ai[100000];
    fgets(line,sizeof(line),file);
    cp = line;
    for(int j=0;j<A;j++){
	    Ai[j] = atof(strtok(cp,delim));
	    cp = NULL;
    }
    double ans = A + B + 1;
    if (ans > B + 2 ){
      ans = B + 2;
    }
    // b = 0;
//    printf("%d,%lf\n",__LINE__,ans);
    double threshold = -1.0 * (ans - 2.0 * B + A - 2.0) / ( B + 1.0 );
    double p = 1.0;
    bool apply = true;
    for(int j=0;j<A;j++){
      p *= Ai[j];
      if (p < threshold){// 枝狩
    	apply = false;
    	break;
      }
    }
//    printf("%d,%lf\n",__LINE__,ans);
    if (apply){
      ans = 2.0 * B - A + 2.0 - p * (B + 1);
    }
//    printf("%d,%lf\n",__LINE__,ans);

    // A > b > 1;
    for(int b=1;b<A;b++){
          apply = true;
    	threshold = (ans - 2.0 * b - B + A - 1.0) / (B + 1.0);
    	p = 1.0 - Ai[0];
    	for(int t = 2; t <= (A - b);++t){
    	  	double sigma = 1.0 - Ai[t - 1];
    	      	for(int k = 1; k <= (t - 1);++k){
    	      	  sigma *= Ai[k-1];
    	      	}

    	   p += sigma;
    	   if (p > threshold){
    		 apply = false;
    		 break;
    	   }
    	}
//    	printf("%d,%lf\n",__LINE__,ans);
       if (apply){
         double candidate = 2.0 * b + B - A + 1.0 + p * (B + 1.0);
         if (candidate < ans){
           ans = candidate;
         }
       }
//       printf("%d,%lf\n",__LINE__,ans);
    }

    printf("%lf\n",ans);
  }

  fclose(file);



  return 0;
}


