#include <iostream>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	string fname;
	if ( argc != 2 )
	{
		cout<<"enter input file name: ";
		cin>>fname;
	}
	else
		fname = argv[1];
	
	ifstream infile(fname.c_str());
	ofstream outfile("output.txt");

	int N;
	infile>>N;
	
	for( int i = 0; i != N; i++ )
	{
		int P, K, L;
		infile>>P>>K>>L;
		
		long long alpha[L];
		
		for( int j = 0; j != L; j++ )
			infile>>alpha[j];
		
		if ( P * K < L )
			outfile<<"Case #"<<i+1<<": Impossible"<<endl;
		else
		{
			long long res;
			res = 0;
			
			int ti;
			ti = 1;
			
			sort(alpha, alpha + L );
			
			int key = 0;
			for( int j = L-1; j >= 0; j-- )
			{
				key++;
				if ( key > K )
				{
					key = 1;
					ti++;
				}
				res += alpha[j] * ti;
			}

			outfile<<"Case #"<<i+1<<": "<<res<<endl;
		}
	}

}
	
