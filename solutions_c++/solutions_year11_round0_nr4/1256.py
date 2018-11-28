#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int num[1000];
int count(int x){
	if(num[x]==x)
		return 0;
	int sum=1;
	while(num[x]!=x){
		swap(num[num[x]], num[x]);
		++sum;
	}
	return sum;
}
int main(){
	int t;
	cin>>t;
	for(int kk=1;kk<=t;++kk){
		int k;
		cin>>k;
		for(int i=0; i<k; ++i){
			cin>>num[i];
			--num[i];
		}
		double ans = 0.0;
		for(int i=0; i<k; ++i)
			ans+=count(i);
		printf("Case #%d: %.6f\n",kk,ans);
	}
	return 0;
}

