
#include <iostream>
using namespace std;

bool process(int n,int k)
{
	for(int i=0;i<n;++i){
		if( (k&1)==0 ){
			return false;
		}
		k>>=1;
	}

	return true;
}

int main()
{
	int t,n,k;
	cin>>t;

	for(int i=1;i<=t;++i){
		cin>>n>>k;
		cout<<"Case #"<<i<<": "<<(process(n,k)?"ON":"OFF")<<endl;
	}

	return 0;
}
