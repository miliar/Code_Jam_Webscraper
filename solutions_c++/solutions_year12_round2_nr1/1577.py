#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		int n;
		cin>>n;
		int A[n];
		int sum=0;
		for(int j=0;j<n;j++){
			cin>>A[j];
			sum+=A[j];
			}
		float B[n];
		float csum=0;
		float C[n];
		int count = 0;
		for(int j=0;j<n;j++){
			B[j]=(((2*float(sum)/float(n))-float(A[j]))/float(sum));
			if (B[j]<=0) { csum+=B[j];C[j]=0;count++;}
			}
		
		for(int j=0;j<n;j++){
			if (B[j]>0) { C[j] = B[j] + csum/(n-count) ;}
			}
		cout<<"Case #"<<i+1<<":";
		for(int j=0;j<n;j++){
			 printf(" %.6f",C[j]*100);
			 if(j==n-1) {cout<<endl;}
			 }
			 }
		return 0;
		}
