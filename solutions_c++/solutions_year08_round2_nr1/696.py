#include<iostream>
using namespace std;
int main(){
	int c;
	cin>>c;
	for(int cc=0;cc<c;++cc){
		long long A,B,D,C,M,n,x0,y0,res=0;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		long long x[n+1],y[n+1];
		x[0]=x0;
		y[0]=y0;
		for(int i=1;i<n;++i){
			x[i]=(A *x[i-1] + B)%M;
			y[i]=(C *y[i-1] + D)%M;
		}
		for(int i=0;i<n;++i){
			for(int j=i+1;j<n;++j){
				for(int k=j+1;k<n;++k){
					if(((x[i]+x[j]+x[k])%3==0 )&&( (y[i]+y[j]+y[k])%3==0)){
						res++;
					}
				}
			}
		}
		cout<<"Case #"<<cc+1<<": "<<res<<endl;
	}
	return 0;
}


