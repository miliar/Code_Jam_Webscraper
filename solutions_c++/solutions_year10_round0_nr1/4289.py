#include<stdio.h>
#include<stdlib.h>
#define ON 1

void toggel(int *a)
{
    if(*a == 1)
      *a = 0;
    else
      *a = 1;
}

void checkPreviosONOFF(int N,int *power,int *onOFF)
{
  int flag = 0,flag1 = 0;
  int j,k;
  for( int i = 1; i < N; i++ ){
    j = i;
    k = 0;
    flag = 0;
    while( j > 0){
      if( onOFF[ k ] == 0 || power[ k ] == 0){
	flag = 1;
      }
      j--;
      k++;
    }
    if( flag == 1){
      power[ i ] = 0;
    }
    else 	
      power[ i ] = 1;
  }
}

int result(int N,int *power,int *onOFF)
{
  int flag = 0;
  for(int i = 0; i < N; i++){
    if( onOFF[ i ] == 0 || power[ i ] == 0){
      flag = 1;
    }
  }
  if( flag == 1 )
    return 0;
  else
    return 1;
}

int main()
{
  FILE *fp;
  fp = fopen("A-small-attempt0.in","r");
  if(fp == NULL){
    exit(0);
  }
  int T;
  fscanf(fp,"%d",&T);
  int count = T-1;
  int tCount = T;
  int N,K;
  while( tCount > 0 ){
    fscanf(fp,"%d%d",&N,&K);
     int power[N],onOFF[N];
     for( int i = 0; i < N; i++){
	power[ i ] = 0;
	onOFF[ i ] = 0;
     }
     power[ 0 ] = 1;
    while( K > 0){
      for(int i = 0; i < N;i++ ){
	if( power[ i ] == ON ){
	  toggel(&onOFF[i]);
	}
      }
      checkPreviosONOFF(N,power,onOFF);
      K--;
    }
    int output = result(N,power,onOFF);
    if( output == 1){
      printf("Case #%d: ON\n",(T-count));
    }
    else{
      printf("Case #%d: OFF\n",(T-count));
    }
    count--;
    tCount--;
  }
  return 1;
} 
