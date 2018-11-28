#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    int noc, n;
    cin>>noc;
    long div,k;
    for (int i = 0; i < noc; i++) {
	cin>>n>>k;
	div = (long int)pow(2,n);
	cout<<"Case #"<<i+1<<": ";
	cout<< ((((k + 1) % div) == 0) ? "ON\n" : "OFF\n");

/*	if ( ( (k + 1) % div ) == 0 )
	    cout<<"ON\n";
	else
	    cout<<"OFF\n";*/
    }
    return(0);
}
