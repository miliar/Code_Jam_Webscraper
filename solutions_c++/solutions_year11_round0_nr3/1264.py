#include<iostream>
#include<cstdio>
using namespace std;
int num[1000];
int main(){
	int t;
	cin>>t;
	for(int kk=1;kk<=t;++kk){
		int k;
		cin>>k;
		int ans = 0, minnum = 0x7fffffff, sum = 0;
		for(int i=0; i<k; ++i){
			cin>>num[i];
			sum += num[i];
			minnum = min(minnum, num[i]);
			ans ^= num[i];
		}
		if(ans==0){
			printf("Case #%d: %d\n",kk,sum-minnum);
		}else{
			printf("Case #%d: NO\n",kk);
		}
	}
	return 0;
}

