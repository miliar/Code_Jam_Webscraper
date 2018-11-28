#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>
using namespace std;

int main(){
	int casos;
	scanf("%d",&casos);
	for (int runs = 1; runs <= casos; runs++){
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		long long v[1002]={0};
		for(int i=0;i<n;i++)
			scanf("%lld",&v[i]);

		
		long long sum[1002]={0},saltos[1002]={0};
		int p = 0;
		for(int i=0;i<n ;i++){
			p=i;
			sum[i]=0;
			while(sum[i]< k){
				sum[i]+=v[p];
				p++;
				p%=n;
				if(p == i) break;
				if(sum[i] + v[p] > k) break;
			}
			saltos[i]=p;
		}
		int salto = 0;
		long long euros = 0;
		while(r--){
			euros+= sum[salto];
			salto = saltos[salto];
		}
		printf("Case #%d: %lld\n",runs,euros);
	}
	return 0;
}