#include <cstdio>
#include <iostream>
int matchs[100][100];


void result(){
  int N;
  double WP[100];
  double OWP[100];
  double OOWP[100];
  int played[100];
  int winned[100];
  
  scanf("%d",&N);
  for(int p = 0; p < N; p++){
    for(int d = 0; d < N; d++){
      char r;
      std::cin >> r;
      matchs[p][d] = r;
    }
  }

  //wp
  for(int i = 0; i < N; i++){
    int matchsPlayed = 0,matchsWinned = 0;
    for(int rival = 0; rival < N; rival++){
      if(matchs[i][rival] == 49 ||matchs[i][rival] == 48){
	matchsPlayed++;
	if(matchs[i][rival] == 49) matchsWinned++;
      }
    }
    WP[i] = (double)matchsWinned/matchsPlayed;
    winned[i] = matchsWinned; played[i] = matchsPlayed;
  }
  
  
  //owp
  for(int i = 0; i < N; i++){
    double owp = 0.0;
    for(int rival = 0; rival < N; rival++){
      if(matchs[i][rival] == 49){
	owp += (winned[rival])/(played[rival] - 1.0);
      }else{
	if(matchs[i][rival] == 48){
	  owp += (winned[rival]-1.0)/(played[rival] - 1.0);	  
	}
      }
    }
    OWP[i] = owp/played[i];
  }


  //oowp
  for(int i = 0; i < N; i++){
    double oowp = 0.0;
    for(int rival = 0; rival < N; rival++){
      if(matchs[i][rival] == 49 || matchs[i][rival] == 48){
	oowp += OWP[rival];
      }
    }
    OOWP[i] = oowp / played[i];
  }
  

  //print
  for(int i = 0; i < N; i++){
    double rpi;
    rpi = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
    printf("%f\n",rpi);
  }
}



int main(){
  int cases;
  scanf("%d",&cases);
  for(int c = 1; c <= cases; c++){
    printf("Case #%d:\n",c);
    result();
  }

}
