#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
	int t, caseN,n,sum,min,xr, a, i;
	fin>>t;
	for(caseN=1; caseN<=t; ++caseN)
	{
		fin>>n;
		fin>>a;
		sum = min = xr = a;
		for(i=1; i<n; ++i)
		{
			fin>>a;
			sum+=a;
			if(min>a)
				min = a;
			xr = xr ^ a;
		}
		fout<<"Case #"<<caseN<<": ";
		if(xr != 0)
		{
			fout<<"NO";
		}
		else
			fout<<sum - min;
		fout<<endl;
	}
	return 0;
}