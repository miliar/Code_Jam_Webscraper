#include<iostream>

using namespace std;

int main(){
	int x,y,z;
	int n;
	int t;
	int a[1100];
	cin>>t;
	for(int j=1;j<=t;j++){
		cin>>n;
		x=0;
		y=10000000;
		z=0;
		for(int i=0;i<n;i++){
			cin>>a[i];
			z+=a[i];
			x=(x^a[i]);
			if(y>a[i]){
				y=a[i];
			}
		}
		if(x==0){
			cout<<"Case #"<<j<<": "<<z-y<<endl;
		}else{
			cout<<"Case #"<<j<<": NO"<<endl;
		}
	}
	return 0;
}
