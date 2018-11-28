#include <cstdint>
#include <iostream>
#include <fstream>
#include <bitset>

using namespace std;


int main(int argc, char* argv[])
{
	ifstream in("3.small.in");
	ofstream out("3.small.out");

	bitset<2000001> bm;

	int T,A,B;

	in >> T;

	for (int t=1;t<=T;t++)
	{
		bm.reset();

		in >> A >> B;
		
		int min=1, digits=1;

		int b=A;

		while(b/=10) { min*=10; digits++; }

		int rv=0;

		for (int i=A;i<=B;i++)
		{
			if (bm[i]) continue;
			
			int n=0, v=i;

			for (int j=1;j<digits;j++)
			{
				v=v/10+v%10*min;
				if (v>=A && v<=B && v!=i && !bm[v])
				{
					n++;
					bm.set(v);
				}
			}

			rv+=(n+1)*n/2;
		}

		out << "Case #" << t << ": " << rv << endl;
	}

	return 42;
}

