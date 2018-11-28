#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	string fname;
	if ( argc != 2 )
	{
		cout<<"enter input file name";
		cin>>fname;
	}
	else
		fname = argv[1];
	
	ifstream infile(fname.c_str());
	ofstream outfile("output.txt");

	int T;
	infile>>T;
	
	for( int i = 0; i != T; i++ )
	{
		int n;
		infile>>n;
		int x[n], y[n];
		for( int j = 0; j != n; j++ )
			infile>>x[j];
		for( int j = 0; j != n; j++ )
			infile>>y[j];
		sort( x, x+n );
		sort( y, y+n );
		long long res = 0;
		for( int j = 0; j != n; j++ )
			res += x[j] * y[n-j-1];
		outfile<<"Case #"<<i+1<<": "<<res<<endl;
	}

}
	
