#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;

void main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");

	int t,n,k;
	int ii;
	ifs>>t;
	for(ii=0; ii<t; ii++)
	{
		ifs>>n>>k;
		ofs<<"Case #"<<ii+1<<": "<<((k+1)%(1<<n) ? "OFF" : "ON")<<endl;
//		cout<<"Case #"<<ii+1<<": "<<((k+1)%(1<<n) ? "OFF" : "ON")<<endl;
	}
}