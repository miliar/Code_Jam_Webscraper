#include <cstdio>

using namespace std;

int tab[10000];

void init(){
  for(int i=0;i<2000;i++){
    tab[i]=i;
  }
}

int find(int a){
  if(tab[a]!=a){
   return  tab[a]=find(tab[a]);
  }else{
    return a;
  }
  /*
  int tmp=a;
  while(tab[a]!=a){
    tmp=tab[tmp];
  }
  return tmp;

  //*/
}

void unio(int a,int b){
  int tmpa=find(a),tmpb=find(b);

  tab[tmpa]=tmpb;
}

int czyn[10000];


int main(){

  int A,B,C,P,wynik;

  for(int i=0;i<2000;i++){
    czyn[i]=1;
  }
  czyn[0]=0;

  for(int i=2;i<1010;i++){
    if(czyn[i]==1){
      for(int j=i;j<1010;j+=i){
	czyn[j]=i;
      }
    }
  }

  scanf("%d",&C);
  int dzi,dzj,tmpi,tmpj;
  for(int zest=1;zest<=C;zest++){
    scanf("%d %d %d",&A,&B,&P);
    wynik=B-A+1;
    init();
    for(int i=A;i<=B;i++){
      for(int j=i+1;j<=B;j++){
	//printf("para %d %d\n",i,j);

	tmpi=i;tmpj=j;
	dzi=czyn[tmpi];
	dzj=czyn[tmpj];
	tmpi/=dzi;
	tmpj/=dzj;

	while(dzi>1){

	  if(dzi==dzj){
	    //printf("znalazlem czynnik %d p=%d\n",dzi,P);
	    
	    if(dzi>=P){
	      //printf("jest pierwszy wiekszy od P\n");
	      if(find(i)!=find(j)){
		//printf("wynik --\n");
		wynik--;
		unio(i,j);
	      }
	      dzi=1;
	      break;
	    }
	  }

	  if(i==15 && j==20){
	    //printf("dzi=%d dzj=%d\n",dzi,dzj);
	  }
	  if(dzi<dzj){
	    dzj=czyn[tmpj];
	    tmpj/=dzj;
	  }else{
	    dzi=czyn[tmpi];
	    tmpi/=dzi;
	  }
	}

      }
    }
    printf("Case #%d: %d\n",zest,wynik);
  }
  /*
  for(int i=0;i<30;i++){
    printf("%d %d\n",i,czyn[i]);
    }//*/
  return 0;
}







