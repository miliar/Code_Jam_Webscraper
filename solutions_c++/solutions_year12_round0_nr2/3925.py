#include<stdio.h>
#include<stdlib.h>

int main(){
  int nlines, ngooglers, nsup, threshold;
  int great, possible;
  int score;
  int dev, surp;
  int i, j;

  scanf("%d", &nlines);
  for(i = 0; i < nlines; i++){
    getchar();
    scanf("%d%d%d", &ngooglers, &nsup, &threshold);
    great = 0, possible = 0;
    for(j = 0; j < ngooglers; j++){
      scanf("%d", &score);
      dev = score / 3;
      surp = score % 3;
      if(dev >= threshold){
	great++;
      }
      else if(dev == threshold - 1){
	if(surp == 0){
	  if(dev > 0) possible++;
	}
	else great++;
      }
      else if(dev == threshold - 2){
	if(surp == 2) possible++;
      }
    }
    if(possible <= nsup) great += possible;
    else great += nsup;
    printf("Case #%d: %d\n", i + 1, great);
  }
}
