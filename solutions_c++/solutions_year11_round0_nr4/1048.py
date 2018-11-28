#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int n;
int a[1001];

int main()
{
	int n,ans,i,t;
	int caseN;
	fin>>t;
	for(caseN = 1; caseN <=t ; ++caseN)
	{
		fin>>n;
		ans = 0;
		for(i=1; i<=n; ++i)
		{
			fin>>a[i];
			if(a[i] != i)
				ans++;
		}
		
		fout<<"Case #"<<caseN<<": "<<ans<<".000000"<<endl;
	}
	return 0;
}