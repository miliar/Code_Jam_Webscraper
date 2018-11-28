#include <fstream>
#include <math.h>
#include <cstdlib>
using namespace std;

int main()
{
	ifstream is;
	ofstream os;
	int N;
	int K;
	int t;

	is.open("A-large.in");
	os.open("A-large.out");
	
	int n;
	is>>n;
	

	for(int i = 1; i <= n; i++)
	{
		is>>N;
		is>>K;
		t = ((1<<N) - 1);
		if(K%(t+1) == t )
		{
			os<<"Case #"<<i<<": ON"<<endl;
		}
		else 
			os<<"Case #"<<i<<": OFF"<<endl;
	}
	
	is.close();
	os.close(); 		

	return 0;
}
