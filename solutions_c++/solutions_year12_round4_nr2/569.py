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
#include <queue>
#include <math.h>
#include <map>
#define MaxLength INT_MAX
#define MaxNode 12
#define MN 1005
using namespace std;

int D,T,N,W,L;
pair<long long,int> r[MN];
int x[MN],y[MN];
int main(){
	int i,j,k,tt,a,b;
	scanf("%d",&T);
	for(tt=1; tt<=T;tt++){
		printf("Case #%d:",tt);
		scanf("%d %d %d",&N, &W, &L);
		for(i=0; i<N ;i++){
			scanf("%lld",&r[i].first);
			r[i].first *= -1;
			r[i].second = i;
		}
		//sort(r,r+N);
		for(i=0; i<N; i++)
			r[i].first *= -1;
		x[0] = y[0] = 0;
		for(i=1; i<N; i++){
			x[i] = y[i] = 0;
			for(j=0; j<i; j++){
				long long X = x[i]-x[j];
				long long Y = y[i]-y[j];
				k=0;
				while((X*X + Y*Y) <=(r[i].first+r[j].first) * (r[i].first+r[j].first)){
					if(x[i]+r[i].first<=W)
						x[i] += r[i].first;
					else if(y[i]+r[i].first<=L){
						x[i]=0;
						y[i]+=r[i].first;
					}else{
						puts("F");
						break;
					}
					X = x[i]-x[j];
					Y = y[i]-y[j];
					k=1;
				}
				if(k)
					j=-1;
			}
		}
		for(i=0; i<N; i++)
			for(j=0; j<N; j++)
				if(r[j].second == i){
					printf(" %d %d",x[j],y[j]);
					break;
				}
		puts("");
	}
	return 0;
}
