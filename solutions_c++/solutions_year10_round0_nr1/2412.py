#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

int main()
{

	ifstream file("A-large.in");
	int T;
	file>>T;
	for (int i=0;i<T;i++)
	{

		int N, K;
		file>>N>>K;


		long a1 = (long)pow(2, N)-1;
		long ak;
		int j=2;
		long C = (long)pow(2, N);
		for(ak=a1;;ak=a1 + ((j-1)*C), ++j)
		{
			if(ak==K)
			{
				cout<<"Case #"<<i+1<<": ON"<<endl;
				break;
			}
			else if (ak>K)
			{
				cout<<"Case #"<<i+1<<": OFF"<<endl;
				break;
			}
		}
	}
return 0;
}
