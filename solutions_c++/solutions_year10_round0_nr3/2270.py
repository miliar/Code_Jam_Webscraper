#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	vector <int> v,v2;
	int t,k,n,r,x,sum,c,j,cnt;
	cin>>t;
	for(int z=1;z<=t;z++){
		v.clear();
		sum=0;
		cin>>r>>k>>n;
		for(int i=0;i<n;i++){
			cin>>x;
			v.push_back(x);
		}
		j=0;
		c=0;
		cnt=0;
		for(int i=0;i<r;i++){
			x=0;
			cnt=0;
			while(1){
				x+=v[j];
				if(x<=k){
					j++;
					cnt++;
				}else{
					x-=v[j];
					break;
				}
				if(j==v.size())
					j=0;
				if(cnt==v.size()){
					break;
				}
			}
			sum+=x;
			if(j==0){
				c=i+1;
				break;
			}
		}
		
		if(c!=0){
			sum=sum*((r/c));
			r=r%c;
			j=0;
	
			for(int i=0;i<r;i++){
				x=0;
				cnt=0;
				while(1){
					x+=v[j];
					if(x<=k){
						j++;
						cnt++;
					}else{
						x-=v[j];
						break;
					}
					if(j==v.size())
						j=0;
					if(cnt==v.size()){
						break;
					}
				}
				sum+=x;
			}
		}
		cout<<"Case #"<<z<<": "<<sum<<endl;
	}
	return 0;
}
