#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

#define IN fin
#define OUT fout

#define MIN(a,b) ((a)<(b) ? (a):(b))

int main()
{
	ifstream fin("C.in");
	ofstream fout("C.out");
	
	int T;
	IN>>T;
	for(int t=1;t<=T;t++)
	{
		int sum=0;
		int mn=1000001;    //1e6 + 1
		int x=0;
		int N;
		IN>>N;
		for(int i=0;i<N;i++)
		{
			int tmp;
			IN>>tmp;
			
			x ^= tmp;
			mn = MIN(mn,tmp);
			sum += tmp;
		}
		OUT<<"Case #"<<t<<": ";
		if(0 == x)
		{
			OUT<<sum - mn<<"\n";
		}
		else
		{
			OUT<<"NO\n";
		}
	}
	return 0;
}
