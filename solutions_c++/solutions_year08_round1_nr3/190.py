#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

main(int argc, char **argv){
	int T;
	cin>> T;
	for(int t=0;t<T;t++){
		long n;
		cin>>n;
		int a[3];
		a[0]=2;
		a[1]=6;
		for(int i=2;i<=n;i++){
			int t=6*a[(i+2)%3]-4*a[(i+1)%3];
			while(t<=0) t+=1000;
			a[i%3]=t%1000;
		}
		printf("Case #%d: %03d\n",t+1,a[n%3]-1);
	}
}	
