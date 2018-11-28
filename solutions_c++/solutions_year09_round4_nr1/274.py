#include<iostream>
#include<algorithm>
using namespace std;
int v[40];
int main(){
	int t;
	cin>>t;
	for(int k=1;k<=t;++k){
		int n;
		cin>>n;
		for(int i=0;i<n;++i){
			string s;
			cin>>s;
			v[i]=n;
			for(int j=n-1;j>=0 && s[j]!='1';--j)
				v[i]=j;
		}
		int ans=0;
		for(int i=0;i<n;++i){
			if(v[i]>i+1){
				int j=i+1;
				for(;v[j]>i+1;++j);
				for(;j>i;--j){
					++ans;
					swap(v[j],v[j-1]);
				}
			}
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}
