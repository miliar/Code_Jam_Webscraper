#include<fstream>
using namespace std;

int main()
{
	int t,n,s,p,sum,pnum;
	int i,j;
	ifstream fin("2.in");
	ofstream fout("2.out");
	fin >> t;
	for (i = 0; i < t; i++)
	{
		fin >> n >> s >>p;
		pnum=0;
		for (j=0; j < n; j++)
		{
			fin >> sum;
			if (sum >= p*3-2) { pnum++; continue;}
			if ((s > 0)&&(sum >= p*3-4) && (p-2>=0)) { pnum++; s--; continue;}
		}
		fout << "Case #" << i+1 <<": " << pnum <<'\n';
	}
	fin.close();
	fout.close();
	return 0;
}