#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
//int sum[100]={0};
int Group[1005];
int info[1005][2];
int main(){
	int t,cn=0,i;
	scanf("%d",&t);
	while(cn<t){
		int R,K,N,period,rn=0,ix,v,euro,st,sum,lv;
		scanf("%d %d %d",&R,&K,&N);
		for(i=0;i<N;i++){
			scanf("%d",&Group[i]);
		}
		//for 0
		//preprocessing
		v=0;
		sum=0;
		ix=0;
		while(v<=N and sum<=K){
			st=sum;
			sum+=Group[ix%N];
			ix++;
			v++;
		}
		info[0][0]=st;
		info[0][1]=(ix-1)%N;

		//cout<<st<<" and "<<(ix-1)%N<<" :: "<<v-1<<endl;
		//lv=v;
		for(i=1;i<N;i++){
			v-=2;
			sum=info[i-1][0]-Group[i-1];
			ix=info[i-1][1];
			//cout<<"see "<<sum<<endl;
			while(v<N and sum<=K){
				st=sum;
				sum+=Group[ix%N];
				ix++;
				v++;
				//cout<<" see "<<v<<endl;
			}
			info[i][0]=st;
			info[i][1]=(ix-1)%N;
			//cout<<st<<" and "<<(ix-1)%N<<" :: "<<v-1<<endl;
			//lv=v;
		}
		//done 
		ix=0;
		euro=0;
		for(i=0;i<R;i++){
			euro+=info[ix][0];
			ix=info[ix][1];
		}
		cn++;
		printf("Case #%d: %d\n",cn,euro);

	}
	return 0;
}
