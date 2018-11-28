#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream in("2.small.in");
	ofstream out("2.small.out");

	int T,N,S,p,e;

	in >> T;

	for (int i=1;i<=T;i++)
	{
		in >> N >> S >> p;

		int st = p + 2*max(0,p-2);
		int ut = p + 2*max(0,p-1);
		int rv=0;

		for (int j=0;j<N;j++)
		{
			in >> e;
			if (e>=ut)
				rv++;
			else if (e>=st && S>0)
			{
				rv++;
				S--;
			}
		}

		out << "Case #" << i << ": " << rv << endl;
	}

	return 0;
}

