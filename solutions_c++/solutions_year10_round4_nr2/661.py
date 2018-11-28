
#include <stdio.h>

#include <stdlib.h>

#define INF 0x3F3F3F3F
using namespace std;


main() {


  int T;
  
  int M[1025];
  
  long long int prices[10][1024];
  
  
  scanf("%d",&T);

  long long int cost[10][1024][10];
  

  for (int t = 1; t <= T; t++) {

    int P;
    
    scanf("%d",&P);
    int numTeams = 1 << P;
    
    for (int m = 0; m < numTeams; m++) {
      scanf("%d",&M[m]);
    }

    for (int round = 0; round < P; round++) {
      int numGames = 1 << (P-round - 1);
      for (int i = 0; i < numGames; i++) {
	scanf("%lld",&prices[round][i]);
      }
    }
  
    
    for (int round = 0; round < P; round++) {
      

      int numGames = 1 << (P-round - 1);
      for (int i = 0; i < numGames; i++) {
	
	int firstCand = i * (numTeams /numGames);
	int lastCand =  (i+1) * (numTeams /numGames) - 1;
	// compute min M[firstCand,lastCand],
	int canMiss = P;
	for (int team = firstCand; team <= lastCand; team++) {
	  if (canMiss > M[team])
	    canMiss = M[team];
	}
	
	for (int haveMissed = 0; haveMissed < P; haveMissed++) {
	  // assume already missed haveMissed;

	  long long int mycost = 0;
	  
  
          if (haveMissed > canMiss) {
	    mycost = INF;
	  }
	  else {
	    if (round == 0) {

	      if (haveMissed == canMiss) {
		mycost = prices[round][i];
	      }
	      else {
		mycost = 0;
	      }
	    }
	    else {
	      if (haveMissed == canMiss) {
		mycost = prices[round][i];
		mycost += cost[round-1][i*2][haveMissed] +
		  cost[round-1][i*2+1][haveMissed];
	      }
	      else {
		int c1 =  prices[round][i] + cost[round-1][i*2][haveMissed] +
		  cost[round-1][i*2+1][haveMissed];
		int c2 =  cost[round-1][i*2][haveMissed+1] +
		  cost[round-1][i*2+1][haveMissed+1];
		
		mycost = (c1 < c2) ? c1 : c2;
		
	      }
	    }
	  }
	  //printf("Cost round %d game %d missed %d = %d\n",
	  // round,i,haveMissed,mycost);
	  cost[round][i][haveMissed] = mycost;
	}
      }
    }
    
    long long int minCost = cost[P-1][0][0];
    for (int m = 0; m < P; m++) {
      if (minCost > cost[P-1][0][m]) {
	minCost = cost[P-1][0][m];
      }
    }
    
    printf("Case #%d: %lld\n",t,minCost);

    

  }

  


}
