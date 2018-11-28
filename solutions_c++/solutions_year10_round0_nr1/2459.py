#include <fstream>
using namespace std;

int main()
{
	bool flags;
	int T, N, K;
	ifstream fin("test.in");
	ofstream fout("test.out");

	fin>>T;
	for(int i=1; i<=T; i++)
	{
		flags = true;
		fin>>N>>K;
		for(int j=0; j<N; j++)
			if( ((K>>j)&0x01) == 0 )
			{
				flags = false;
				break;
			}
		fout<<"Case #"<<i<<": ";
		if( flags == true )
			fout<<"ON"<<endl;
		else
			fout<<"OFF"<<endl;
	}

	return 0;
}
