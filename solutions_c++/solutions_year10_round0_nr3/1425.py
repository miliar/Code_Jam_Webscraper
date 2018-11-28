#include<iostream>
using namespace std;
int main(){
	int r,k,n,t,sum,sumx,p,sp;
	int g[1000];
	cin>>t;
	for(int x=1;x<=t;++x){
		sum=0;
		cin>>r>>k>>n;
		for(int y=0;y<n;++y)
			cin>>g[y];
		sum=p=0;
		for(int y=0;y<r;y++){
			sumx=0;
			sp=p;
			while(sumx+g[p]<=k){
				sumx+=g[p];
				p=(p+1)%n;
				if(p==sp)
					break;
			}
			sum+=sumx;
		}
		printf("Case #%d: %d\n",x,sum);
	}
	
}
