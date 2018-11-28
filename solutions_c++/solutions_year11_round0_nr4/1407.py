#include<iostream>
using namespace std;

int t,n,p,c;
int main(){
	cin>>t;
	for(int z=1;z<=t;z++){
		c=0;
		cin>>n;
		for(int y=1;y<=n;y++){
			cin>>p;
			if(p!=y)
				c++;
		}
		cout<<"Case #"<<z<<": "<<c<<".000000"<<endl;
	}
	return 0;
}
