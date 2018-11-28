#include <iostream>

using namespace std;

__int64 i,n,k;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-small-attempt.out","w",stdout);
	int test;
	cin>>test;
	i=0;
	while (test--) {
	i++;
	cin>>n>>k;
	k%=1<<n;
	cout<<"Case #"<<i<<": ";
	if(k==(1<<n)-1)
		cout<<"ON"<<endl;
	else
		cout<<"OFF"<<endl;
	
	}
	return 0;
};
