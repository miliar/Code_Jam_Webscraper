#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	int t,k,s,p,b,temp,sum,counter;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>k>>s>>p;
		for(b=0,sum=0;b<k;++b){
			cin>>temp;
			if((temp+2)/3>=p)
				++sum;
			else if(temp>1&&(temp+2)/3==p-1&&s){
				++sum;
				--s;
			}
		}
		cout<<"Case #"<<counter<<": "<<sum<<endl;
	}
	return 0;
}
