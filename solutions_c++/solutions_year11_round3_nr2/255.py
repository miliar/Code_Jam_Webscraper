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
#define MN 1000005
using namespace std;

int M,T,D,N,L,H,C;

struct cc{
	long long v;
	int no;
}typedef Link;

Link link[MN];



int cmp(const void * x, const void * y){
	Link * a = (Link *)x;
	Link * b = (Link *)y;
	if(b->v > a->v)
		return 1;
	if(b->v == a->v)
		return 0;
	return -1;
}

int main(){
	int i,j,k,len,tt,n,m,maxv,maxi,minv;
	long long result;
	long long t;
	scanf("%d",&T);
	long long temp = 0;
	for(tt=1; tt<=T;tt++){
		result =0;
		temp = 0;
		scanf("%d %lld %d %d",&L,&t,&N,&C);
		for(i=0; i<C;i++){
			scanf("%d",&link[i].v);
			link[i].no = N/C;
			if(i<N%C)
				link[i].no++;
			result += link[i].v * link[i].no * 2;
			//printf("%d %d\n",link[i].v, link[i].no);
		}
		if(result >= t){
			result =0;
			i=0;
			while(result < t){
				result += link[i].v * 2;
				link[i].no--;
				i++;
				i%=C;
			}
			i = (i+C-1) % C;
			/*i--;
			i%C;*/
			link[C].v = (result - t)/2;
			//printf("%lld %lld\n",(result- t)/2, link[C].v);
			link[C].no = 1;
			result = t;
			C++;
			qsort(link,C,sizeof(Link),cmp);

			for(i=0; i<C;i++){
				link[i].no *= 2;
				//printf("%lld %d\n",link[i].v, link[i].no);
				j = L < link[i].no/2? L : link[i].no/2;
				link[i].no -= j;
				L-=j;
				result += link[i].v * link[i].no;
			}
		}
		
		printf("Case #%d: %lld\n",tt,result);
	}
	
	return 0;
}
