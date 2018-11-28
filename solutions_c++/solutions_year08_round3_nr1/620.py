#include <cstdio>
#include <algorithm>

using namespace std;

int tab[10000];

int kla[10000];

int main(){
  int zest,N,p,k,l,wynik,i,mini,j;
  bool czy;
  scanf("%d",&N);
  for(zest=1;zest<=N;zest++){
    wynik=0;
    scanf("%d %d %d",&p,&k,&l);
    for(i=0;i<l;i++){
      scanf("%d",&(tab[i]));
    }
    sort(tab,tab+l);
    /*
    for(i=l-1;i>=0;i--){
      printf("%d ", tab[i]);
    }
    //*/
    for(i=0;i<=k;i++){
      kla[i]=1;
    }
    mini=0;
    czy=false;
    for(i=l-1;i>=0;i--){
      czy=false;
      mini=0;
      for(j=0;j<k;j++){
	if(kla[j]<=p){
	  czy=true;
	  if(kla[mini]>kla[j]){
	    mini=j;
	  }
	}
      }
      if(czy==true){
	wynik+=tab[i]*kla[mini];
	kla[mini]++;
      }else{
	wynik=-100;
      }
    }

    if(wynik>=0){
      printf("Case #%d: %d\n",zest,wynik);
    }else{
      printf("Case #%d: Impossible\n");
    }
  }
  return 0;
}
