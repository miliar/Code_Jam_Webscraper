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
#define MaxNode 12
#define MN 1000005
using namespace std;

int M,T,N,S;
int mem[MN];
int size;
int main(){
	int i,j,k,len,tt,res,p;
	scanf("%d",&T);
	for(tt=1; tt<=T;tt++){
		res = 0;
		scanf("%d %d %d",&N,&S,&p);
		//printf("%d %d %d\n",N,S,p);
		for(i=0; i<N;i++){
			scanf("%d",&k);
			if(p==0 ||k>(max(0,(p-1))*3))
				res++;
			else if(S>0 && k>(max((p-2),0)*3+1)){
				S--;
				res++;
			}
		}
		printf("Case #%d: %d\n",tt,res);
	}

	return 0;
}
