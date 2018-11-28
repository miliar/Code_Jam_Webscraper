#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool b[101][101];

void evol()
{
	bool bb[101][101];
	for (int i=1;i<=100;i++)
		for (int j=1;j<=100;j++)
		{
			if (j-1>=0 && b[i][j-1] && i-1>=0 && b[i-1][j])
				bb[i][j] = true;
			else if ((j==1 || !b[i][j-1]) && (i==1 || !b[i-1][j]))
				bb[i][j] = false;
			else
				bb[i][j] = b[i][j];
		}
	for (int i=1;i<=100;i++)
		for (int j=1;j<=100;j++)
			b[i][j] = bb[i][j];
}
bool zero()
{
	for (int i=1;i<=100;i++)
		for (int j=1;j<=100;j++)
			if (b[i][j]) return false;
	return true;
}

int main()
{
    ifstream ifs("C-small-attempt0.in");
    ofstream ofs("C-small-attempt0.out");

    int T, R;
	int x1, x2, y1, y2;

	//ofs.setf(ios::fixed, ios::floatfield);
	//ofs.precision(7);

    ifs >> T;
    for (int i=0;i<T;i++)
    {	
		ifs >> R;
		for (int j=1;j<=100;j++)
			for (int l=1;l<=100;l++)
				b[j][l] = false;
		for (int j=0;j<R;j++)
		{
			ifs >> x1 >> y1 >> x2>>y2;
			for(int l1=x1;l1<=x2;l1++)
				for (int l2=y1;l2<=y2;l2++)
					b[l1][l2] = true;
		}

		long long count = 0;
		while (!zero())
		{
			evol();
			count++;
		}


		ofs << "Case #" << i+1 << ": " << count << endl;
    }

    ifs.close();
    ofs.close();

    return 0;
}
