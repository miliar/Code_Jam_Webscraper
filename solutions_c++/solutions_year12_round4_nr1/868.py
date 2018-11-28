
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
int ind[10001];
int vined[10001];
int vinel[10001];
int maxd[10001];

struct myclass1 {
  bool operator() (int i,int j) {
	  if (vined[i]>vined[j]) {
		  int a=vinel[j];
		  vinel[j]=vinel[i];
		  vinel[i]=a;
		  a=vined[j];
		  vined[j]=vined[i];
		  vined[i]=a;
		  return -1;
	  }
	  return 1;
  }
} myobject1;


void compute(){
	int i,j,k,a;
	for (i=0;i<n;i++) {
		maxd[i]=0;
		ind[i]=i;
	}
	//sort(ind,ind+n,myobject1);
	for (i=n-1;i>0;i--){
		for (j=0;j<i;j++){
			if (vined[j]>vined[j+1]){
				 a=vinel[j];
				  vinel[j]=vinel[j+1];
				  vinel[j+1]=a;
				  a=vined[j];
				  vined[j]=vined[j+1];
				  vined[j+1]=a;
			}
		}
	}

	//for (i=0;i<n;i++) printf("%d_%d\n",vined[i],vinel[i]);
	//maxd[0]=vinel[0];
	if (vined[0]>vinel[0]) return;
	maxd[0]=vined[0];
	for (i=0;i<n;i++){
		//printf("%d: %d\n",i,maxd[i]);
		for (j=i+1;j<=n;j++){
			if (vined[j]-vined[i]<=maxd[i]){
				k=vinel[j];
				if (vined[j]-vined[i]<k) k=vined[j]-vined[i];
				if (maxd[j]<k) maxd[j]=k;
			} else break;
		}
	}
}

int main(){
	int t;
	int i,j,k;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>n;
		for (j=0;j<n;j++) {
			cin>>vined[j]>>vinel[j];
		}
		cin>>vined[n];
		vinel[n]=0;
		maxd[n]=-1;

			
		compute();
		cout<<"Case #"<<(i+1)<<": ";
		//for (j=0;j<n;j++) cout<<rpi[j]<<endl;
		if (maxd[n]>=0) printf("YES");
		else printf("NO");
		printf("\n");
		//for (j=0;j<n;j++) printf("%f %f %f %.10f\n",wp[j],owp[j],oowp[j],rpi[j]);
	}
}
