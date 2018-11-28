#include<iostream>
#include<vector>

using namespace std;
int main(){
	vector<int> ar;
	int t,r,k,n,g,i,j,m,sum,count,flag,Case=1,group;

	cin>>t;
	while(t--){
		cin>>r>>k>>n;
		ar.clear();
		for(i=0;i<n;i++){
			cin>>g;
			ar.push_back(g);	
		}
		count = sum = i = flag = 0;
		while(r--){
			//while(sum<=k){
			group=1;
				//cout<<"i ="<<i<<endl;
				while(1){
					
					if(sum+ar[i]>k || group > n){
						flag=1;
				//		cout<<sum<<" "<<i<<endl;					
						break;	
					}
					else
					{	sum+=ar[i];group++;}
					i++;

					if(i==n)
					{	i=0;}
					
				}
			//}
				count+=sum;
				sum=0;
		}
		cout<<"Case #"<<Case++<<": "<<count<<endl;
	}
}
