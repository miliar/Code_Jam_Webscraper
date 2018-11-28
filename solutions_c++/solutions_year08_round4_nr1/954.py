#include <stdio.h>
#include <queue>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>
//#include <cmath>


using namespace std;
#define ASIZE 80000

int arvore[ASIZE];//valores das folhas
int gate[ASIZE];//0 and 1 or
int change[ASIZE];//0 doesn't change 1 changes
int minzero[ASIZE];
int minone[ASIZE];
           
#define INF 100000 //se ret > inf, retorna inf


//pensar no caso de so raiz
int m,v;


int isFolha(int no){
	return no >= ((m-1)/2);
}

int getMin(int no,int valor){
	//printf("No %d valor %d\n",no,valor);
	if(valor==0){
		if(minzero[no]!=-1)
			return minzero[no];
	}
	else{
		if(minone[no]!=-1)
			return minone[no];
	}
	
	if(isFolha(no)){
		if(arvore[no]==0){
			minzero[no]=0;
			minone[no]=INF;
		}
		else{
			minone[no]=0;
			minzero[no]=INF;
		}
		if (arvore[no]==valor){			
			return 0;
		}		
		else{
			return INF;
		}
	}
	else{		
		int f1 = 2*no+1;
		int f2 = 2*no+2;
		int andMinZero = min( 	getMin(f1,0)+getMin(f2,0),
								min(
								getMin(f1,0)+getMin(f2,1),
								getMin(f1,1)+getMin(f2,0)));
		int andMinOne  = 		getMin(f1,1)+getMin(f2,1);
		
		int orMinZero =			getMin(f1,0)+getMin(f2,0);
		int orMinOne  =	min(	getMin(f1,0)+getMin(f2,1),
				min(
								getMin(f1,1)+getMin(f2,0),
								getMin(f1,1)+getMin(f2,1)));
		//printf("No %d f1 %d f2 %d\n",no,f1,f2);
		//printf("andMinZero %d andMinOne %d orMinZero %d orMinOne %d\n",
				//andMinZero,andMinOne,orMinZero,orMinOne);
		
		int myMinZero,myMinOne;
		if(change[no]==1){
			//!!!! fazer logica de adicionar 1!!!
			if(gate[no]==1){//and
				//printf("No and\n");
				if(andMinZero<=orMinZero){
					myMinZero = andMinZero;
				}
				else{
					myMinZero = orMinZero+1;
				}
				//printf("andMinOne %d orMinOne %d\n",andMinOne,orMinOne);
				if(andMinOne<=orMinOne){
					myMinOne = andMinOne;					
				}
				else{
					
					myMinOne = orMinOne+1;
				}
				//printf("My min one %d\n",myMinOne);
			}
			else{//gate eh do tipo or
				if(andMinZero<orMinZero){
					myMinZero = andMinZero+1;
				}
				else{
					myMinZero = orMinZero;
				}
				if(andMinOne<orMinOne){
					myMinOne = andMinOne+1;					
				}
				else{
					myMinOne = orMinOne;
				}

			}
				
			//myMinZero= min( andMinZero, orMinZero);
			//myMinOne = min( andMinOne, orMinOne);					
		}
		else{//nao muda
			//printf("Gate nao muda! Tipo %d\n",gate[no]);
			if(gate[no]==1){//and
				myMinZero=andMinZero;
				myMinOne =andMinOne;
			}
			else{//or
				myMinZero=orMinZero;
				myMinOne =orMinOne;
			}
		}
		
		if(myMinZero>INF)
			myMinZero=INF;
		if(myMinOne>INF)
			myMinOne=INF;
		//printf("Result myMinZero %d myMinOne %d\n",myMinZero,myMinOne);
		minzero[no]=myMinZero;
		minone[no]=myMinOne;
		if(valor==0)
			return myMinZero;
		else
			return myMinOne;
		
	}
}


int main(){
	int cases;
	scanf("%d",&cases);
	
	for(int i=0;i<cases;i++){
		//limpa
		for(int j=0;j<ASIZE;j++){
			minzero[j]=-1;
			minone[j]=-1;
		}
		
		scanf("%d%d",&m,&v);
		for(int j=0;j<(m-1)/2;j++){
			int g,c;
			scanf("%d%d",&g,&c);
			gate[j]=g;
			change[j]=c;
		}
		for(int j= (m-1)/2;j<m;j++){
			int v;
			scanf("%d",&v);
			arvore[j]=v;
		}
		int myMin = getMin(0,v);
		printf("Case #%d: ",i+1);
		if(myMin<INF)
			printf("%d",myMin);
		else
			printf("IMPOSSIBLE");
		
		/*for(int j=0;j<m;j++){
			printf("%d %d %d\n",j,minzero[j],minone[j]);
		}*/
		printf("\n");
	}
	
}