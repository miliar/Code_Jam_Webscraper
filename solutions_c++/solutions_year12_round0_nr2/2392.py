#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
	int t,i=1;
	cin>>t;
	while(t-->0){
		int n,s,p,arr[101];
		cin>>n>>s>>p;
		for(int j=0;j<n;++j)
			cin>>arr[j];
		int threshold_p=3*p-4,threshold_normal=3*p-2;
		
		int no_p=0,res=0;
		for(int j=0;j<n;++j){
			if(arr[j]>=threshold_p && arr[j]<threshold_normal && arr[j]>0){
				no_p+=1;
			}
			else if(arr[j]>=threshold_p && arr[j]>=threshold_normal)
				++res;
		}
		if(no_p>s)
			no_p=s;
		printf("Case #%d: %d\n",i,res+no_p);
		++i;
	}
}