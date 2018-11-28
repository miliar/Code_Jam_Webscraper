#include<iostream>

using namespace std;

void task(){
	int N;
	int a,b,min,sum;
	int i;

	cin>>N;
	cin>>b;
	min=b;
	sum=b;
	for(i=1;i<N;i++){
		cin>>a;
		b=a^b;
		if(a<min) min=a;
		sum+=a;
	}
	if(b==0) cout<<sum-min;
	else cout<<"NO";
}

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		task();
		cout<<"\n";
	}
	return 0;
}


