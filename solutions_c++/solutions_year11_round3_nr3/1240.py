//#include<stdio>
#include<iostream>
using namespace std;

void harmony();

int main(){
	int T;		//Total number of test cases
//	cout<<"Enter total number of test cases\t";
	cin>>T;
	for (int i=1;i<=T;i++){
		cout<<"Case #"<<i<<": ";harmony();
		
	}
	return 0;
}

void harmony(){
	int  N,L,H,i,l,c;
	cin>>N>>L>>H;
	int a[N];
	for(i=0;i<N;i++)
		cin>>a[i];
l=L;
while(l<=H){
	c=1;
	for(i=0;i<N;i++){
		if(a[i]%l==0||l%a[i]==0){
			c++;		
		}
		else {
			c=0;break;
		}
	}	
	if(c>=N){
		cout<<l<<endl;return;
	}
	l++;
}
cout<<"NO"<<endl;
}



