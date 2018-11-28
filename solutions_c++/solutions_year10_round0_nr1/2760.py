/*
Coder : Kushagra Gour
chinchang457@gmail.com
15 april 2010

complexity : --
*/
#include<iostream>
#include<fstream>
#include<stack>
#include<queue>
#include<vector>
#include<string>
#include<stdio.h>
#include<math.h>
#include<time.h>
using namespace std;

#define DEBUG 1
#define FOR(i,a,b) for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) FOR(i,0,n)

int main(){
	FILE *f; 
	FILE *pf;
	f=fopen("A-large.in","r+");
	pf=fopen("A-large.out","w+");
	
	int t; fscanf(f,"%d",&t);

	int N,K;
	REP(i,t){
		fscanf(f,"%d %d",&N,&K); 
		int on=int( (K)/pow((double)2,N-1) )%2; //cout<<on<<" ";
		int one=0;
		if(N-1!=0) one=( (K+1)%((int)pow((double)2,N-1)) ); 
		if(K==0 && N>1) one=1;
		//cout<<one;

		fprintf(pf,"Case #%d: ",i+1);

		if(on && one==0) fprintf(pf,"ON\n");
		else fprintf(pf,"OFF\n");
	


	}
}