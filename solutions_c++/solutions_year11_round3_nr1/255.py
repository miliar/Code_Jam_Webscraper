#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <map>
#define MaxLength INT_MAX
#define MaxNode 1000000
#define MN 55
using namespace std;

int M,T,D,N;
char mem[MN][MN];
int size;
int cmp(const void * x, const void * y){
	long long * a = (long long *)x;
	long long * b = (long long *)y;
	if(*a-*b>0)
		return 1;
	else
		if(*a-*b==0)
			return 0;
		else return -1;
}
bool vaild(int r, int c){
	return r>=0 && r<N && c<M && c>=0;
}
int main(){
	int i,j,k,len,t,n,m,maxv,minv;
	long long result;
	
	long long upper, lower,mid;
	scanf("%d",&T);
	for(t=1; t<=T;t++){
		scanf("%d %d\n", &N,&M);
		for(i=0; i<N;i++)
			gets(mem[i]);
		bool success=true;
		for(i=0; i<N && success;i++){
			for(j=0; j<M && success;j++)
				if(mem[i][j]=='#'){
					if(vaild(i+1,j) && mem[i+1][j]=='#'
						&& vaild(i+1,j+1) && mem[i+1][j+1]=='#'
						&& vaild(i,j+1) && mem[i+1][j+1]=='#'
						){
							mem[i][j]='/';
							mem[i][j+1]='\\'; 
							mem[i+1][j]='\\';
							mem[i+1][j+1]='/';
					}
					else
						success=false;
				}
		}
		if(success){
			printf("Case #%d:\n",t);
			for(i=0; i<N;i++)
				puts(mem[i]);
		}
		else
			printf("Case #%d:\nImpossible\n",t);
	}
	
	return 0;
}
