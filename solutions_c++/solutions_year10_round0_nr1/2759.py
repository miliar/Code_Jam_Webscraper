#include <fstream>

using namespace std;

int main()
{
	ifstream f("A-large.in");
	ofstream f2("output.out");

	long long int n,k,n2;
	int T;
	f>>T;

	for(int TEST=0;TEST<T;TEST++)
	{
		f>>n>>k;
		n2=1;
		for(int i=0;i<n;i++)
			n2=n2*2;
		if((k+1)%n2==0)
			f2<<"Case #"<<TEST+1<<": ON"<<endl;
		else
			f2<<"Case #"<<TEST+1<<": OFF"<<endl;
	}
	f.close();
	f2.close();
	return 0;
}
