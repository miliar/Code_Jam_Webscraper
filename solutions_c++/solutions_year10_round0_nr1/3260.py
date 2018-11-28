#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

bool simulate(int n,int k)
{
	bool acces=true;
	while(n--)
		if (!(k&(1<<n)))
		{
			acces=false;
			break;
		}
	return acces;
}

int main()
{
	int lines;
	ifstream fin("A-large.in");
	fin>>lines;
	for(int i=1;i<=lines;++i)
	{
		int n,k;
		fin>>n>>k;
		cout<<"Case #"<<i<<": "<<(simulate(n,k)?"ON":"OFF")<<endl;
	}
}
