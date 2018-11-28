#include <iostream>
using namespace std;
 
int main(){
	freopen("C:\\gcj\\A-small.in","r",stdin);
	freopen("C:\\gcj\\A-small.out","w",stdout);
	long n;
	long a,b,i,j;
	long c;
	cin>>n;
	for(i=0;i<n;i++){
		cin>>a>>b;
		c=1;
		for(j=0;j<a;j++)
			c*=2;
		b++;
		if ( b % c == 0)
			cout<<"Case #"<<i+1<<": ON"<<endl;
		else
			cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
	
	return 0;
}