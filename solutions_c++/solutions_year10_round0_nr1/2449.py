#include <iostream>
#include <fstream>
#include <string>

using namespace std;

unsigned int N,K;

bool run()
{
	unsigned int tmpN = 1<<N;
	if(K%tmpN==(tmpN-1)) return true;
	return false;
}

int main(int argc,char **argv)
{
	ifstream fin(argv[1]);
	int T;
	fin>>T;

	for (int i=1;i<=T;i++)
	{
		fin>>N>>K;
		bool b = run();
		cout<<"Case #"<<i<<": "<<(b?"ON":"OFF")<<endl;
	}

}
