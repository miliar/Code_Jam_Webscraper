#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char* argv[])
{
	int t,r,k,n,sum=0,wy=0; 
	int el,temp; //element do vectora
	vector<int> a; //vector grupy

	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>r>>k>>n;
		
		for(int j=0;j<n;j++){
			cin>>el;
			a.push_back(el);
		}
		for(int l=0;l<r;l++){
			for(int m=0;m<a.size();m++){
				sum+=a[0];

				if(sum<=k){
					temp=a[0];
					a.erase(a.begin());
					a.push_back(temp);

				}
				else {
					sum-=a[0];
					break;
				}
			}
			wy+=sum;
			sum=0;
		}
		cout<<"Case #"<<i<<": "<<wy<<endl;
		wy=0;
		a.erase(a.begin(),a.end());
	}
	
	
	/*
	for(int i=0;i<5;i++){
		cin>>el;
		a.push_back(el);
	}
	cout<<a[0]<<endl;

	a.erase(a.begin());

	cout<<a[0]<<endl;

	cout<<"size: "<<a.size();*/

	return 0;
}

