#include <iostream>
#include <math.h>

using namespace std;

int main(){
	freopen("A-large.in" , "r" , stdin);
	//freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);

	int t;
	cin>>t;
	for(int i = 0 ; i < t ; i++){
		unsigned long long n , k;
		cin>>n>>k;
		unsigned long long needed;
		
		needed = pow(2.0,1.0*n) - 1;
		if(k==needed)
			cout<<"Case #"<<i+1<<": ON\n";
		else if(k < needed)
			cout<<"Case #"<<i+1<<": OFF\n";
		else{
			k -= needed;
			if(k%(needed+1)==0)
				cout<<"Case #"<<i+1<<": ON\n";
			else
				cout<<"Case #"<<i+1<<": OFF\n";
		}
	}
	return 0;
}
