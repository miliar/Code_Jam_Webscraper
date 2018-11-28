#include<iostream>
#include<stdio.h>

using namespace std;

int arry[1005];
int T,N;

int main(){
	freopen("D-large.in", "r", stdin);
	freopen("outlarge.txt", "w", stdout);
	cin>>T;
	int cas=0;

	while(cas++<T){
		cin>>N;

		int cnt=0;
		for(int i=0; i<N; i++){
			cin>>arry[i];
			if(arry[i]!=i+1) cnt++;
		}
		/*
		for(int j=0; j<N-1; j++){
			for(int k=j+1; k<N; k++){
				if(arry[k-1]>arry[k]){
					int t=arry[k-1];
					arry[k-1]=arry[k];
					arry[k]=t;
					cnt++;
				}
			}
		}*/

		printf("Case #%d: %0.6lf\n", cas, 1.0*cnt);
	}

	return 0;
}
