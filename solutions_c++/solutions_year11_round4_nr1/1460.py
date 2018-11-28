
//Problem A. 

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <cmath>

using namespace std;

int n;
int x,s,r,rt;
int walka[1000];
int walkb[1000];
int w[1000];
int distarr[2005];
int speedarr[2005];
double runtimeleft;

double cal(int dist, int speed){
	double res=0;
	if (dist==0) return 0;
	double tmp;
	if (runtimeleft<=0.0000000000000000001) return dist/(double)(s+speed);

	tmp=dist/(double)(r+speed);
	if (tmp<=runtimeleft){
		//run all time
		runtimeleft-=tmp;
		return tmp;
	}

	res=runtimeleft;
	res+=(dist-(r+speed)*(double)runtimeleft)/(double)(s+speed);
	runtimeleft=0;
	
	return res;
}

double compute(){
	int i,j,k,ii;
	runtimeleft=rt;
	double totaltime=0;


	/*
	totaltime+=cal(walka[0],0);
	totaltime+=cal(x-walkb[n-1],0);
	totaltime+=cal(walkb[0]-walka[0],w[0]);
	//printf("first total: %f\n",totaltime);
	for (i=1;i<n;i++){
		//printf("i:%d ",i);
		totaltime+=cal(walka[i]-walkb[i-1],0);
		//printf("%f ",totaltime);
		totaltime+=cal(walkb[i]-walka[i],w[i]);
		//printf("%f ",totaltime);
		//printf("\n");
	}
	*/

	k=0;
	distarr[k]=walka[0]-0;
	speedarr[k]=0;
	k++;
	distarr[k]=x-walkb[n-1];
	speedarr[k]=0;
	k++;
	distarr[k]=walkb[0]-walka[0];
	speedarr[k]=w[0];
	k++;
	for (i=1;i<n;i++){
		distarr[k]=walka[i]-walkb[i-1];
		speedarr[k]=0;
		k++;
		distarr[k]=walkb[i]-walka[i];
		speedarr[k]=w[i];
		k++;
	}

	for (i=k-1;i>=1;i--){
		for (j=0;j<i;j++){
			if (speedarr[j]>speedarr[j+1]){
				ii=distarr[j];
				distarr[j]=distarr[j+1];
				distarr[j+1]=ii;
				ii=speedarr[j];
				speedarr[j]=speedarr[j+1];
				speedarr[j+1]=ii;
			}
		}
	}

	for (i=0;i<k;i++){
		totaltime+=cal(distarr[i],speedarr[i]);
		//printf("i:%d %f %d %d\n",i,totaltime,distarr[i],speedarr[i]);
	}



	return totaltime;
}

int main(){
	int t;
	int i,j,k;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>x>>s>>r>>rt>>n;
		for (j=0;j<n;j++) {
			cin>>walka[j]>>walkb[j]>>w[j];
		}
		//printf("%d %d %d %d %d\n",x,s,r,rt,n);
	
		double res=compute();
		cout<<"Case #"<<(i+1)<<": ";
		printf("%.10f\n",res);
	}
}
