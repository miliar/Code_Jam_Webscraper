#include <cstdio>

using namespace std;

int arrA[1600],depA[1600],arrB[1600],depB[1600];

int getTime(int h,int m){
  //printf("dla danych h=%d m=%d wynik to %d\n",h,m,h*60+m);
  return h*60+m;
}

int main(){

  int N,na,nb,i,t,wynA,wynB,deph,depm,arrh,arrm;

  scanf("%d",&N);

  for(int j=1;j<=N;j++){
    wynA=0;wynB=0;
    for(i=0;i<1500;i++){
      arrA[i]=0;arrB[i]=0;depA[i]=0;depB[i]=0;
    }

    scanf("\n%d\n%d %d",&t,&na,&nb);
    //printf("t=%d\n",t);
    for(i=0;i<na;i++){
      scanf("\n%d:%d %d:%d",&deph,&depm,&arrh,&arrm);
      depA[getTime(deph,depm)]++;
      arrB[getTime(arrh,arrm)+t]++;
    }
    for(i=0;i<nb;i++){
      scanf("\n%d:%d %d:%d",&deph,&depm,&arrh,&arrm);
      depB[getTime(deph,depm)]++;
      arrA[getTime(arrh,arrm)+t]++;
    }

    for(i=0;i<1440;i++){
      if(arrA[i]<depA[i]){
	//printf("zkwiekszam wynik o %d przy i=%d arrA=%d depA=%d\n",depA[i]-arrA[i],i,arrA[i],depA[i]);
	wynA+=depA[i]-arrA[i];
	arrA[i]=0;
      }else{
	arrA[i]-=depA[i];
      }
      arrA[i+1]+=arrA[i];


      if(arrB[i]<depB[i]){
	wynB+=depB[i]-arrB[i];
	arrB[i]=0;
      }else{
	arrB[i]-=depB[i];
      }
      arrB[i+1]+=arrB[i];
    }
    printf("Case #%d: %d %d\n",j,wynA,wynB);
  }
  return 0;
}
