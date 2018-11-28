//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>
#include <stdlib>
using namespace std;
long long gcd(long long a,long long b) {
	while ((a!=0)&&(b!=0))
	{
		if (a>b) a%=b;
		else b%=a;
	} ;
	return (a+b);
}
int main()
{
	long long a[3], n, t, res;
	ifstream in("B.in");
	ofstream out("B.out");
	in >> t;
	for (int l=0;l<t;l++) {
		in >> n;
		res = 0;
		for (int i=0;i<n;i++)
			in >> a[i];
		//res = abs(a[0]-a[1]);
		for (int i=0;i<n-1;i++)
			for (int j=i+1;j<n;j++)
			 res = gcd(res, abs((double)a[i]-a[j]));
		if (a[0] % res) res -= a[0] % res;
		else res = 0;
		out << "Case #" << l+1 << ": " << res << endl;
	}


	out.close();

}
//---------------------------------------------------------------------------
