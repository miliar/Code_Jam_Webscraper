// task3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
int P[101][101], Q[101][101];

int jeden(){
	int R; scanf("%d", &R);
	for(int i =0; i<101; i++)
		for(int j =0; j<101; j++)
			P[i][j]=0;
	for(int i = 0; i<R;i++){
		int a,b,c,d; scanf("%d%d%d%d", &a, &b, &c,&d);
		
		for(int j = a; j<=c; j++)
			for(int k = b; k<=d; k++)
				P[j][k]=1;
	}
	int round = 1;
	while(1){
		int sum = 0;
		for(int i =1; i<101; i++)
		for(int j =1; j<101; j++)
			if(P[i-1][j]==1 && P[i][j-1]==1 && P[i][j]==0)
			{Q[i][j]=1;sum++;}
			else if((P[i-1][j]==1 || P[i][j-1]==1) && P[i][j]==1)
			{Q[i][j]=1;sum++;}
			else Q[i][j]=0;
		for(int i =1; i<101; i++)
		for(int j =1; j<101; j++)
			P[i][j]=Q[i][j];
		if(sum==0) break;
		else round++;
	}
	return round;
}

int main(int argc, char* argv[])
{
	int c; scanf("%d", &c);
	for(int i = 0; i<c; i++){
		printf("Case #%d: %d\n", i+1, jeden());
	}
}

