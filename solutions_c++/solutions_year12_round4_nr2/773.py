
//Problem B. 

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <cmath>

using namespace std;

int n,w,l;
int r[6000];
int used[6000];
int unext[6000];
int uprev[6000];
double resx[6000];
double resy[6000];
int leftind[6000];
int leftcount;
int total;
int sortind[6000];

struct myclass1 {
  bool operator() (int i,int j) {
	  return r[i]>r[j];
  }
} myobject1;

void dfs(double left, double top, double width, double height, int istopedge, int isbottomedge){
	int i,j,k;
	double x,y;
	if (width<0 || height<0) return;
	if (total>=n) return;
	//printf("... %.1f,%.1f,%.1f,%.1f,%d,%d\n",left,top,width,height,istopedge,isbottomedge);
	for (i=leftcount;i<n;i++){
		k=sortind[i];
		if (used[k]==0){
			if (istopedge && isbottomedge){
				if (width>=r[k]){
					resx[k]=left+r[k];
					resy[k]=top;
					used[k]=1;
					total++;
					//printf("%d a %d %.1f,%.1f\n",total,k,resx[k],resy[k]);
					if (height-r[k]>=0) dfs(left,top+r[k],width,height-r[k],0,isbottomedge);
					if (width-2*r[k]>=0) dfs(left+2*r[k],top,width-2*r[k],height,istopedge,isbottomedge);
					break;
				}
			}else if (istopedge){
				if (width>=r[k] && height>=r[k]){
					resx[k]=left+r[k];
					resy[k]=top;
					used[k]=1;
					total++;
					//printf("%d b %d %.1f,%.1f\n",total,k,resx[k],resy[k]);
					if (height-r[k]>=0) dfs(left,top+r[k],width,height-r[k],0,isbottomedge);
					if (width-2*r[k]>=0) dfs(left+2*r[k],top,width-2*r[k],height,istopedge,isbottomedge);
					break;
				}
			}else if (isbottomedge){
				if (width>=r[k] && height>=r[k]){
					resx[k]=left+r[k];
					resy[k]=top+r[k];
					used[k]=1;
					total++;
					//printf("%d c %d %.1f,%.1f\n",total,k,resx[k],resy[k]);
					if (height-2*r[k]>=0) dfs(left,top+2*r[k],width,height-2*r[k],0,isbottomedge);
					if (width-2*r[k]>=0) dfs(left+2*r[k],top,width-2*r[k],height,istopedge,isbottomedge);
					break;
				}
			}else {
				if (width>=r[k] && height>=2*r[k]){
					resx[k]=left+r[k];
					resy[k]=top+r[k];
					used[k]=1;
					total++;
					//printf("%d d %d %.1f,%.1f\n",total,k,resx[k],resy[k]);
					if (height-2*r[k]>=0) dfs(left,top+2*r[k],width,height-2*r[k],0,0);
					if (width-2*r[k]>=0) dfs(left+2*r[k],top,width-2*r[k],height,0,0);
					break;
				}
			}
		}
	}
}

void compute(){
	int i,j,k;
	double x,y, width, height;
	
	total=0;
	leftcount=0;

	//init
	for (i=0;i<n;i++){
		used[i]=0;
		resx[i]=0;
		resy[i]=0;
		sortind[i]=i;
	}
	sort(sortind,sortind+n,myobject1);
	//sort from large to small

	x=0;y=0;
	leftcount=1;
	k=sortind[0];
	resx[k]=0;
	resy[k]=0;
	used[k]=1;
	y+=r[k];
	total=1;
	for (i=1;i<n;i++){
		k=sortind[i];
		if (y+r[k]<=l){
			resx[k]=x;
			resy[k]=y+r[k];
			used[k]=1;

			y+=2*r[k];
			total++;
			leftcount++;
		}else{
			break;
		}
	}

	y=0;
	for (i=0;i<leftcount;i++){
		k=sortind[i];
		x=r[k];
		width=w-r[k];
		height=2*r[k];
		if (i==0) height=r[k];
		if (i==leftcount-1) height=r[k]+l-resy[k];
		if (i==0 && i==leftcount-1) height=l;
		//printf("left: %d %.1f,%.1f,%.1f,%.1f   %d\n",i,x,y,width,height,r[k]);
		dfs(x,y,width,height,(i==0),(i==leftcount-1));

		x=0;
		if (i==0) y+=r[k];
		else y+=2*r[k];
	}
}

int main(){
	int t;
	int i,j,k;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>n>>w>>l;
		for (j=0;j<n;j++) cin>>r[j];
	
		compute();
		cout<<"Case #"<<(i+1)<<":";
		for (j=0;j<n;j++) printf(" %.2f %.2f",resx[j],resy[j]);
		
		/*
		for (j=0;j<n;j++){
			if (resx[j]<0 || resx[j]>w || resy[j]<0 || resy[j]>l) printf("outbound %d %.1f,%.1f %d,%d\n",j,resx[j],resy[j],w,l);
			for (k=0;k<n;k++){
				if (j!=k){
					if ( ((resx[j]-resx[k])*(resx[j]-resx[k])+(resy[j]-resy[k])*(resy[j]-resy[k])) < (r[j]+r[k])*(r[j]+r[k]) ){
						printf("!!! %d,%d %.1f,%.1f,%d %.1f,%.1f,%d\n",j,k,resx[j],resy[j],r[j],resx[k],resy[k],r[k]);
					}
				}
			}
		}
		*/
		

		cout<<endl;
		//for (j=0;j<n;j++) cout<<rpi[j]<<endl;
		//for (j=0;j<n;j++) printf("%f %f %f %.10f\n",wp[j],owp[j],oowp[j],rpi[j]);

	}
}
