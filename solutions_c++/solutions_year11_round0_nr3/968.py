#include <fstream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;


int main()
{
	ifstream fin;
	fin.open("test1.txt");
	ofstream fout;
	fout.open("test2.txt");
	
	int t;
	fin>>t;
	
	for (int i=0; i<t; i++)
	{
		int c,n,s(0),sum(0),min(10000001);
		fin>>n;
		for (int j=0; j<n; j++)
		{
		fin>>c;
		sum+=c;
		if (c<min) min=c;
		s^=c;
		}
		if (s!=0) fout<<"Case #"<<i+1<<": NO"<<endl;
		else fout<<"Case #"<<i+1<<": "<<sum-min<<endl;
		
	}
	
	fin.close();
	fout.close();

	return 0;
}
