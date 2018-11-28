#include <fstream>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int t,n,a;
double g;
int main()
{
	out.setf(ios::fixed);
	out.precision(7);
	in >> t;
	for (int x=1;x<=t;x++)
	{
		g=0.0;
		in >> n;
		for (int i=1;i<=n;i++)
		{
			in >> a;
			if (a!=i) g+=1.0;
		}
		out << "Case #" << x << ": " << g << "\n";
	}
	return 0;
}
