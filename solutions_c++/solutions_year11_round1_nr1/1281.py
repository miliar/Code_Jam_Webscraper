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
#define MN 513
using namespace std;

int N,M,T,D;


char mem[MN][MN];
int large[MN][MN];
int re[MN];

int main(){
	int i,j,k,len,t,n,m,maxv,v;
	bool success;
	int last, result;
	int pd,pg;
	scanf("%d",&T);
	for(t=1; t<=T;t++){
		success=false;
		scanf("%d %d %d", &N, &pd, &pg);
		if((pg==100 && pd<100) || (pg==0 && pd>0))
			success=false;
		else{
			for(i=1; i<=N && !success;i++){
				if(((pd*i)%100)==0 && (pd*i)/100<=i){
					success=true;
				}
			}
		}

		if(success)
			printf("Case #%d: Possible\n",t);
		else
			printf("Case #%d: Broken\n",t);

	}
	
	return 0;
}
