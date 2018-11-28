#include<iostream>
#include<algorithm>
using namespace std;

void swap(int &a,int &b){
	int temp;
	temp=a;
	a=b;
	b=temp;
}

int gcd(int a,int b){
	int temp;
	if(a<b)
		swap(a,b);
	while(b){
		temp=a%b;
		a=b;
		b=temp;
	}
	return a;
}

long long int *save;

int main(){
	int t,n,counter,b,c,temp;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>n;
		save=new long long int[n];
		for(b=0;b<n;++b)
			cin>>save[b];
		sort(save,save+n);
		for(temp=save[1]-save[0],c=2;c<n;++c)
			temp=gcd(temp,save[c]-save[c-1]);
		cout<<"Case #"<<counter<<": "<<(save[0]%temp?temp-save[0]%temp:0)<<endl;
	}
	return 0;
}



