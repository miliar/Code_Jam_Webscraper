#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define MAX_SEG 1010
#define eps 1e-12

int T,S,R,N,t;
int B[ MAX_SEG ],E[ MAX_SEG ];
int w[ MAX_SEG ];
int X;
int order[MAX_SEG];

int cmp(int id1, int id2){
    return w[id1] < w[id2];    
}

int main(){
    scanf("%d",&T);
    for (int caseID = 1; caseID <= T; caseID++){
	scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
	double soFar = 0;
	double distRemain = X;
	//cout<<"X is "<<distRemain<<"\n";
	for (int i = 0; i < N; i++){
	    scanf("%d%d%d",&B[i],&E[i],&w[i]);
	    order[i] = i;
	    distRemain -= (double)(E[i]-B[i]);
	    //cout<<"remain : "<<distRemain<<endl;
	}
	sort(order, order+N,cmp);
	if (soFar < t){
	    double distRun = (double)R * (t-soFar);
	    //cout<<"distRuN:"<<distRun<<" distRem: "<<distRemain<<endl;
	    if (distRun < distRemain){
		soFar = t + (distRemain-distRun) / (double)S;		
	    } else {
		soFar += distRemain / (double)R;
	    }
	} else soFar += distRemain / (double)S;
	//cout<<"soFar:"<<soFar<<endl;
	for (int k = 0; k < N; k++){
	    int i = order[k];
	    double len = E[i] - B[i];
	    if (soFar < t) {
		double speed = w[i] + R;
		double time = len/speed;
		if (soFar + time <= t) soFar += time;
		else{ 
		    double timeRemain = t-soFar;
		    soFar = t;
		    soFar += (len - timeRemain * speed) / (double)(S+w[i]);
		}
	    }else{
		soFar += len / (double)(S+w[i]);
	    }
	    distRemain -= len;
	}
	
	printf("Case #%d: %.9f\n",caseID,soFar);
    }
    return 0;
}

