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
#define MaxNode 10000
#define MN 105
using namespace std;

int M,T,D,N,L,H;
int mem[MN];
int test[MaxNode];
int prime[MaxNode];
int fact[MaxNode];

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
	int result;
	/*
	memset(test,0,MaxNode);
	size=0;
	for(i=2; i<N;i++){
		if(test[i]==0){
			prime[size++]=i;
			j=i+i;
			while(j<MaxNode){
				test[j] = 1;
				j+=i;
			}
		}
	}*/
	scanf("%d",&T);
	/*
	memset(fact,0,size);
	memset(test,0,MaxNode);*/
	int id=0;
	for(t=1; t<=T;t++){
		scanf("%d %d %d", &N,&L,&H);
		id++;
		maxv=-1;
		for(i=0; i<N;i++){
			scanf("%d",&mem[i]);
			/*
			if(mem[i]>1){
				for(j=0; j<size;j++)
					if(mem[i]%prime[j]==0){
						fact[j]=id;
						if(maxv<j)
							maxv=j;
					}
			}*/
		}
		bool success = false;
		for(i=L; i<=H && !success;i++){
			for(j=0; j<N;j++)
				if(i%mem[j]!=0 && mem[j]%i!=0)
					break;
			if(j==N)
				success = true;
		}
		if(!success)
			printf("Case #%d: NO\n",t);
		else
			printf("Case #%d: %d\n",t,i-1);
	}
	
	return 0;
}
