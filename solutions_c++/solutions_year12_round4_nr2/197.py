#include <stdio.h>
#include <queue>
#include <string>
#include <stdlib.h>
#include <time.h>
using namespace std;

int N;
double gx[1001], gy[1001];
double r[1001];
int W, L;
//FILE *forsok;

void run(int fall){
	printf("Case #%d:", fall);
	scanf("%d %d %d", &N, &W, &L);
	queue<int> q;
	for(int i=0;i<N;i++){
		scanf("%lf", &r[i]);
		gx[i] = gy[i] = -1e6;
		q.push(i);
		/*fscanf(forsok, "%lf %lf", &gx[i], &gy[i]);
		printf("\n%lf %f\n", gx[i], gy[i]);
		if(gx[i]<0)printf("FEL1\n");
		if(gy[i]<0)printf("FEL2\n");
		if(gx[i]>W)printf("FEL3\n");
		if(gy[i]>L)printf("FEL4\n");*/
	}
	while(!q.empty()){
		int nu = q.front();
		q.pop();
		double x = (rand()/(double)RAND_MAX) * W;
		double y = (rand()/(double)RAND_MAX) * L;
		for(int i=0;i<N;i++){
			if(gx[i] < -1)continue;
			double xdist = gx[i]-x;
			double ydist = gy[i]-y;
			double dist2 = xdist*xdist+ydist*ydist;
			//printf("%lf %lf\n", (r[nu] + r[i])       *(r[nu] + r[i])+1e-3, 
			//	                (r[nu] + r[i] + 1e-4)*(r[nu] + r[i] + 1e-4));
			if(dist2 <= (r[nu]+r[i])*(r[nu]+r[i])+1e-3){
			//if(dist2 <= (r[nu] + r[i] + 1e-4)*(r[nu] + r[i] + 1e-4)){
				gx[i] = gy[i] = -1e6;
				q.push(i);
			}
			/*double dist = sqrt((gx[i]-x)*(gx[i]-x) + (gy[i]-y)*(gy[i]-y));
			if(dist <= r[nu] + r[i] + 1e-4){
				gx[i] = gy[i] = -1e6;
				q.push(i);
			}*/
			/*double dist2 = xdist*xdist+ydist*ydist;
			if(dist2 <= (r[nu] + r[i] + 1e-4)*(r[nu] + r[i] + 1e-4)){
				gx[i] = gy[i] = -1e6;
				q.push(i);
			}*/
		}
		gx[nu] = x;
		gy[nu] = y;
	}
	/*for(int i=0;i<N;i++){
		for(int j=i+1;j<N;j++){
			double dist = sqrt((gx[i]-gx[j])*(gx[i]-gx[j]) + (gy[i]-gy[j])*(gy[i]-gy[j]));
			if(dist < r[i]+r[j]){
				printf("FEL5 %d %d\n", i, j);
			}
		}
	}
	return;*/
	for(int i=0;i<N;i++){
		printf(" %.5lf %.5lf", gx[i], gy[i]);
	}
	printf("\n");
}


int main(){
	//forsok = fopen("B-small-attempt0.forsok2", "r");
	//srand(time(0));
	srand(42);
	int T;
	scanf("%d", &T);
	for(int i=0;i<T;i++){
		run(i+1);
	}	
}

