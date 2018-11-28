#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
const int N=1000;
int main()
{
	int t,n,arr[2000];
	double res;
	int i,j;
	cin>>t;
	for(i=1;i<=t;++i){
		res=0;
		cin>>n;
		for(j=0;j<n;++j){
			cin>>arr[j];
			arr[j+N]=arr[j];
		}
		sort(arr,arr+n);
		for(j=0;j<n;++j){
			if(arr[j]!=arr[j+N])res+=1;
		}
		printf("Case #%d: %.6f\n",i,res);
	}
}
