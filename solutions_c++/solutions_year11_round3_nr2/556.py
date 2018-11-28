#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <queue>
#include <set>
#include <map>
#include <vector>

using namespace std;

double dist[1001];
double total[1001];

int main(){
	int cases,L,N,C;
	double t;
	scanf("%d",&cases);
	for(int ca=1; ca<=cases; ++ca){
		scanf("%d %lf %d %d",&L,&t,&N,&C);
		double di=0;	
		for(int i=0; i<C; ++i){
			scanf("%lf",dist+i);
		}
		for(int i=0; i<N; ++i){
			total[i]=di;
			di+=dist[i%C];
		}
		di*=2; //slow ship
		//printf("Dist=%lf\n",di);
		double best=di;
		if(L>0){
			for(int i=0; i<N; ++i){
				double newdist=di;
				double wait=t-min(2*total[i],t);
				if(wait>=dist[i%C]*2) continue;
				double diff=dist[i%C]*2-(wait+(2*dist[i%C]-wait)/2);
				newdist-=diff;
				double newnewdist;
				if(L>1){
					for(int j=i+1; j<N; ++j){
						wait=t-min(2*total[j]-diff,t);
						if(wait>=dist[j%C]*2) continue;
						double ndiff=dist[j%C]*2-(wait+(2*dist[j%C]-wait)/2);
						newnewdist=newdist-ndiff;
						if(newnewdist<best){
							best=newnewdist;
						}
					}
					//printf("%d,%lf\n",i,best);
				}
				if(newdist<best){
					best=newdist;
				}
			}
		}

		printf("Case #%d: %d\n",ca,(int)best);
	}
		
		
		



	return 0;
}
