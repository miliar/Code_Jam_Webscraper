#include <iostream>
#include <fstream>
#include <cmath>
#include <queue>
#include <utility>

using namespace std;

int M[1024];
int price[10][1024];
bool occ[10][1024];
int P;

int find(int n)
{
	unsigned int m = 1<<(P-1); 
	int l=P-1;
	while(1)
	{
		int x = m & n;
		if (!occ[l][x])
		{
			occ[l][x];
			return x;
		}
		unsigned int mm = m>>1;
		m = m+mm;
		l--;
	}

	return -1;
}

int main()
{
    ifstream ifs("B-small-attempt0.in");
    ofstream ofs("B-small-attempt0.out");

    int T;

	//ofs.setf(ios::fixed, ios::floatfield);
	//ofs.precision(7);

    ifs >> T;
    for (int i=0;i<T;i++)
	{
		ifs >> P;
		int nP = 1;
		for (int j=0;j<P;j++)
			nP*=2;
		for (int j=0;j<nP;j++)
			ifs >> M[j];

		int NP = nP;
		for (int j=0;j<P;j++)
		{
			nP/=2;
			for (int l=0;l<nP;l++)
			{
				ifs >> price[j][l];
				occ[j][l] = false;
			}
		}

		for (unsigned j=0;j<NP;j++)
		{
			int l=P-1;
			while(l>=0 && M[j]<P)
			{
				unsigned int x = j;
				x>>=(l+1);
				occ[l][x] = true;
				l--;
				M[j]++;
			}
		}

		int count = 0;
		for (int j=0;j<P;j++)
		{
			NP/=2;
			for (int l=0;l<NP;l++)
				if (occ[j][l])
					count++;
		}
		
		ofs << "Case #" << i+1 << ": " << price[0][0]*count << endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}
