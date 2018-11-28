#include <iostream>
using namespace std;
int main(){
	int m,n,k,s;
	cin>>m;
	for (int i=0;i<m;i++){
		cin>>n>>k;
		s=1;
		for (int j=0;j<n;j++) s<<=1;
		cout<<"Case #"<<i+1<<": "<<((k+1)%s==0?"ON":"OFF")<<endl;
	}
	return 0;
}