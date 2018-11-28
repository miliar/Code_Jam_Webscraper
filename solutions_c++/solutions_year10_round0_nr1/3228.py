#include <fstream>
using namespace std;

int main()
{
	ifstream in("a.in");
	ofstream out("a.out");

	long int t,n,k;
	bool f;
	int m;
	in>>t;
	for(int i=1; i<=t; i++)
	{
		in>>n>>k;
		f = true;
		int m = 0;
		while (f && m<n)
		{
			if(k%2==0) 
				f = false;
			else
				k = k/2;
			m++;
		}
		out<<"Case #"<<i<<": ";
		if(f) out<<"ON"; else out<<"OFF";
		out<<"\n";
	}
	return 0;
}