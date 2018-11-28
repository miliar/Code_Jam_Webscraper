#include<fstream>
using namespace std;
int main()
{
	ifstream fin("A-large.in");//
	ofstream fout("1.out");
	int N,Case;
	int n,k;
	fin>>N;
	Case=1;
	while(Case<=N)
	{
		fout<<"Case #"<<Case<<": ";
		fin>>n>>k;
		n=(1<<n);
		if((k+1)%n==0)
			fout<<"ON"<<endl;
		else fout<<"OFF"<<endl;
		Case++;
	}
	return 0;
}