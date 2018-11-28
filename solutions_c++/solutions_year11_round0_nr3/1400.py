#include<iostream>
using namespace std;
long long t,n,s,v,c,a;
int main(){
	cin>>t;
	for(int z=1;z<=t;z++){
		cin>>n;
		s=0;
		c=0;
		v=10000000;
		for(int i=0;i<n;i++){
			cin>>a;
			if(a<v)
				v=a;
			s+=a;
			c^=a;
		}
		cout<<"Case #"<<z<<": ";
		if(c!=0)
			cout<<"NO"<<endl;
		else
			cout<<(s-v)<<endl;
	}
	return 0;
}
