#include <iostream.h>
#include <fstream.h>
#include <math.h>

int main()
{
    int T,i;
    long int K,N,val,modval;
    ifstream infi;

    infi.open("big.in");
    infi >> T;

    ofstream myfile;
    myfile.open ("abig.out");

    i=0;
    while (i++<T) {
	infi >> N >> K;
	val = pow(2,N);
	modval = K % val;

	if((modval+1)==val)
		{
			myfile << "Case #" << i << ": ON\n";
		}
	else
		{
			myfile << "Case #" << i << ": OFF\n";
		}
    }

    infi.close();
    myfile.close();
    return 0;
}