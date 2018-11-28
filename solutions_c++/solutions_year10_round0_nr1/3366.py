#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int isOn(long int n,long int k)
{	
	long int n2;
	n2 = 1<<n;
	//cout << n << " " << n2 << " " <<(k+1)%(n2) << endl;
	if ((k+1)%(n2)==0) {
		return(1);
	}
	else {
		return(0);
	};
};

int main (int argc, char * const argv[]) {
	int t,i = 0;
    cin >> t;
	int n,k;
	string isOns;
	while (t--) {
		cin>>n>>k;
		i++;
		if (isOn(n, k) == 1)
			isOns = "ON";
		else isOns = "OFF";
		cout<<"Case #"<<i<<": "<<isOns<<endl;
	}
    return 0;
}
