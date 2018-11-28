#include<fstream>
using namespace std;
bool f(unsigned int n, unsigned int k)
{
	unsigned int mask=(((unsigned)1)<<n)-1;
	if((mask & k)==mask)
		return true;
	return false;
}
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int N;
	int n,k;
	fin>>N;
	int i;
	for(i=1;i<=N;++i)
	{
		fin>>n>>k;
		if(f(n,k))
			fout<<"Case #"<<i<<":"<<" ON\n";
		else	
			fout<<"Case #"<<i<<":"<<" OFF\n";
	}
	return 0;
}
		
		
