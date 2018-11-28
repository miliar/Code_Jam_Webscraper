#include<iostream>
#include<cmath>

using namespace std;

int main(int argc, char* argv[])
{
	unsigned int t,n,k,temp,klap=0;
	
	cin>>t;
	for(int i=1;i<=t;i++){

		cin>>n>>k;
		
		k++;
		if(k%static_cast<int>(pow(2.0,n))==0){
			cout<<"Case #"<<i<<": ON"<<endl;
		} else {
			cout<<"Case #"<<i<<": OFF"<<endl;
		}	
	}

	return 0;
}
