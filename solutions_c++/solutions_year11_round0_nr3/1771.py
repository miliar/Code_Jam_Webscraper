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
using namespace std;

int N,T,D;
int c[1005];

int main(){
	int i,j,k,len,t,n,m,maxv,max,a,b,v,count;
	int result;

	scanf("%d",&T);
	for(t=1; t<=T;t++){
		scanf("%d",&N);
		result = 0;
		v=0;
		for(i=0; i<N;i++){
			scanf("%d",&c[i]);
			result^=c[i];
			v+=c[i];
		}
		sort(c,c+N);
		
		if(result!=0)
			printf("Case #%d: NO\n",t);
		else{

			printf("Case #%d: %d\n",t,v-c[0]);
		}
	}
	
	return 0;
}
