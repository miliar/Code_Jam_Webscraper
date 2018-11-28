#include <iostream>
#include <string.h>
#include <cstdio>
using namespace std;
int main(){
	int data[1001][2];
	for(int i = 0;i < 1001;i++)
		for(int j = 0; j < 2;j++)
				data[i][j] = 0;
	for(int i = 0;i < 1001;i++){
		int temp;
		if(i > 11 && i < 99){
			temp = (i%10)*10 + (i/10);
			if( temp > i  && i%10 != 0 && temp%10 !=0)
				data[i][0] = temp;
		}else if(i > 100 && i < 999){
			temp = (i%10)*100 + (i/10);
			if( temp > i  && i%10 != 0)
				data[i][0] = temp;
			temp = (i%100)*10 + (i/100);
			if( temp > i  && i%100 != 0)
				data[i][1] = temp;
		}
	}
	// for(int i = 100;i <= 500;i++){
		// if(data[i][0] <= 500 && data[i][0] != 0)
			// printf("%d %d\n",i,data[i][0]);
		// if(data[i][1] <= 500 && data[i][1] != 0)
			// printf("%d %d\n",i,data[i][1]);
	// }
	FILE *ptrin = fopen("32.in","r"),*ptrout = fopen("32.out","w");
	int T;
	fscanf(ptrin,"%d\n",&T);
	for(int i = 0; i < T;i++){
		int A,B;
		fscanf(ptrin,"%d %d",&A,&B);
		int result = 0;
		for(int j = A; j <= B;j++){
			if(j > 11 && j < 99 && data[j][0] <= B && data[j][0] != 0)
				result++;
			else if(j > 100 && j < 999){
				if(data[j][0] <= B && data[j][0] != 0)
					result++;
				if(data[j][1] <= B && data[j][1] != 0)
					result++;
			}
		}
		fprintf(ptrout,"Case #%d: %d\n",i+1,result);
	}
}