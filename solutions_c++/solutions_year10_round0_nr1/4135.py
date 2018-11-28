#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(int argc,char *argv[])
{
	ifstream myInfile;
	long int tests = 0;
	int snappers = 0;
	int snaps = 0;
	long int numOn = 0;

	myInfile.open(argv[1]);

	myInfile>>tests;
	for (int i = 0; i < tests; i++)
	{
		myInfile>>snappers;
		myInfile>>snaps;

		numOn = pow(2,snappers);
//		cout<<numOn<<endl;

		if(snaps < (numOn-1))
			cout<<"Case #"<<i+1<<": OFF"<<endl;
		else if((snaps >= (numOn-1)) && ((snaps - (numOn-1))%numOn == 0))
			cout<<"Case #"<<i+1<<": ON"<<endl;
		else
			cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
    


	myInfile.close();
	
	return 0;
}
