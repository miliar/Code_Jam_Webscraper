#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <iostream>

#define min(a,b) (a<b)?(a):(b);
#define max(a,b) (a>b)?(a):(b);
#define PI 3.14159265358979323846264338327950288

using namespace std;


int main(int argc,char *argv[]){
	int  c,i,j,k,l,nCases;
	long long n, A, B, C, D, x0, y0,M,X,Y,T;
	long long P[10000][3];
	
	
	cin >> nCases;
	for(c=0;c<nCases;c++){				
		cin >> n;
		cin >> A;
		cin >> B;
		cin >> C;
		cin >> D;
		cin >> x0;
		cin >> y0;
		cin >> M;
	
		X = x0;
		Y = y0;
		P[0][0] = X;
		P[0][1] = Y;
		P[0][2] = 0;
		for(i=1;i<n;i++){
			X = (A * X + B)% M;
			Y = (C * Y + D)% M;
			P[i][0] = X;
			P[i][1] = Y;
			P[i][2] = 0;
		}
		
		T=0;
		
		for(j=0;j<n;j++){			
			for(k=j+1;k<n;k++){
				for(l=k+1;l<n;l++){
					if((fmod((double)(P[j][0]+P[k][0]+P[l][0]),(double)3.F)==0.F)&&
					   (fmod((double)(P[j][1]+P[k][1]+P[l][1]),(double)3.F)==0.F)){							   
						++T;						 						   					   
					}													
				}
			}			
		}
		printf("Case #%d: %d\n",c+1,T);		
	}

	return 0;
}