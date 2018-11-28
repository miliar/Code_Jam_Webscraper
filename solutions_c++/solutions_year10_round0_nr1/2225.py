//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	long long n,k,t,st=1;
	ifstream in("A.in");
	ofstream out("A.out");
	in >> t;
	for (int i=0;i<t;i++) {
		in >> n >> k;
		st = 1;
		for (int j=0;j<n;j++)
			st *= 2;
		k++;
		if (k % st) out << "Case #" << i+1 << ": OFF" << endl;
		else out << "Case #" << i+1 << ": ON" << endl;
	}
	out.close();

}
//---------------------------------------------------------------------------
