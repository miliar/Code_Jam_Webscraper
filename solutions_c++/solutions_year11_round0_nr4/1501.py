#include<iostream>
#include<cstdio>

using namespace std;

int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int t,f=1,counter;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int arr[1001];
		counter=0;
		for(int i=1;i<=n;i++){
			cin>>arr[i];
			if(arr[i]!=i) counter++;
		}
		printf("Case #%d: %.6lf\n",f++,(double)counter);
	}
	return 0;
}
