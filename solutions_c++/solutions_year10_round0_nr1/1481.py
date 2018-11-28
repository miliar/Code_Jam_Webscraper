#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define ulli unsigned long long int
#define lli long long int

#define f(i,n) for(ulli i = 0; i < n; i++)


int main(){
	int ntc = 0;
	cin>>ntc;
	
	f(tc,ntc){
		ulli n, k;
		int t = 1;
		cin >>n >>k;
		k++;
		f(i,n){
			if (k&1){
				t = 0;
				break;
			}
			k = k>>1;
		}
			cout << "Case #"<<tc+1<<": ";
		if(t)
			cout <<"ON"<<endl;
		else
			cout <<"OFF"<<endl;
	}
	return 0;
}
