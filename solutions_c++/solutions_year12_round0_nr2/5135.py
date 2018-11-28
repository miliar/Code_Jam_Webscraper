#include<iostream>

using namespace std;

int main(){
	int i,t,n,s,p,m,r,x,ans[100];
	for(int k=0;k<100;k++){ans[k]=0;}
	cin>>t;i=0;
	while(i<t){
		cin>>n>>s>>p;
		for(int j=0;j<n;j++){
			cin>>x;
			r= x%3;
			m = x/3 + ((r==0)?0:1);
			if(m>=p)ans[i]++;
			else if (m == p-1){
				if(x>=2 && x<=28)
				if(r!=1 && s>0) ans[i]++;--s;
			}
		}
		++i;
	}
	i=0;
	while(i<t){
		cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
		++i;
	}
}
		
		
