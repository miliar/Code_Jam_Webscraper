
//Problem B. 

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <cmath>

using namespace std;

int n,s,p;
int scores[200];
int res;

void compute(){
	int i,j,k;
	int count=0;
	int potential=0;
	for (i=0;i<n;i++){
		if ((scores[i]+2)/3>=p) count++;
		else if ( ((scores[i]+2)/3==p-1) && scores[i]%3!=1 && scores[i]>1) potential++;
	}
	if (potential>s) potential=s;
	res=count+potential;
}

int main(){
	int t;
	int i,j,k;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>n>>s>>p;
		for (j=0;j<n;j++) cin>>scores[j];
	
		compute();
		cout<<"Case #"<<(i+1)<<": "<<res<<endl;
		//for (j=0;j<n;j++) cout<<rpi[j]<<endl;
		//for (j=0;j<n;j++) printf("%f %f %f %.10f\n",wp[j],owp[j],oowp[j],rpi[j]);
	}
}
