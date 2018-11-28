#include<fstream>
using namespace std;
int n,k,t;

int main()
{
	int i;
	ifstream fin("A-large.in");
	ofstream fout("A-small.out");
	fin >> t;
	for (i = 0;i < t;i ++)
	{	
		fin >> n >> k;
		if (k == 0) 
		{
			fout << "Case #" << i + 1 << ": OFF" << endl;
			continue;
		}
		if ((k + 1) % (1 << (n)) == 0)
			fout << "Case #" << i + 1 << ": ON" << endl;
		else
			fout << "Case #" << i + 1 << ": OFF" << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
		