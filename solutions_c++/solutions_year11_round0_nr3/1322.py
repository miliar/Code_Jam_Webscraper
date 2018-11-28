#include<iostream>
using namespace std;
void fuck(){
	long long n, t, sum, min, sums=0;
	cin>>n;
	sum=0;
	sums=0;
	while(n--){
		cin>>t;
		sum^=t;
		sums+=t;
		if(min==-1)
			min=t;
		else
			if(min>t)
				min=t;
	}
	if(sum==0){
		cout<<sums - min<<endl;
	}
	else{
		cout<<"NO"<<endl;
	}
}
int main(){
	int ncase;
	cin>>ncase;
	for(int i=0; i<ncase; i++){
		cout<<"Case #"<<i+1<<": ";
		fuck();
	}
}
