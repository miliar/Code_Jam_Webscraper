#include <fstream>
#include <vector>
using namespace std;

class Snapper
{
public:
	bool IsReceiving;
	bool IsON;
};

int main()
{
	Snapper temp;
	temp.IsReceiving = false;
	temp.IsON = false;

	ifstream fin("D:\\A-small-attempt2.in");
	ofstream fout("D:\\output.txt");
	int t = 0;
	fin >> t;
	for (int i = 0; i < t; i++)
	{
		int n, k;
		fin >> n >> k;
		vector<Snapper> a(n, temp);
		a[0].IsReceiving = true;
		
		for (int j = 0; j < k; j++)
		{
			for (int m = 0; m < n; m++)
			{
				if (a[m].IsReceiving)
				{
					a[m].IsON = !(a[m].IsON);
				}
				else break;
			}

			int p = 1;
			for (int m = 1; m < n; m++)
			{
				if (a[m - 1].IsON)
				{
					a[m].IsReceiving = true;
					p = m + 1;
				}
				else break;
			}

			for (int m = p; m < n; m++)
			{
				a[m].IsReceiving = false;
			}
		}

		bool IsON = true;
		for (int j = 0; j < n; j++)
		{
			if (!a[j].IsON)
			{
				IsON = false;
				break;
			}
		}

		fout << "Case #" << i + 1 << ": ";
		if (IsON) fout << "ON" << endl;
		else fout << "OFF" << endl;
	}
	fout.close();
}