//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	long long t,r,k,g[1000], count=0, curtr;
	long long ntr,n,sum;
	ifstream in("A.in");
	ofstream out("A.out");
	in >> t;
	for (int l=0;l<t;l++) {
		in >> r >> k >> n;
		ntr = 0;
		count = 0;
		for (int i=0;i<n;i++)  {
			in >> g[i];
			sum += g[i];
		}
		while (r) {
			curtr = 0;
			while ((curtr + g[ntr] <= k)&&(curtr + g[ntr] <= sum)) { curtr += g[ntr];ntr++;if (ntr==n) ntr=0;}
			count += curtr;
			r--;
		}
		out << "Case #" << l+1 << ": " << count << endl;
	}


	out.close();

}
//---------------------------------------------------------------------------
