#include <fstream>
#include <string>

using namespace std;

struct trip_struct
{
	int leave, arrive, dir;
	int free;
};

int main()
{
	ifstream fin("c:\\codejam\\train.txt");
	ofstream fout("c:\\codejam\\train_out.txt");
	int num_cases;
	fin >> num_cases;
	string tmp;
	for (int p=0; p<num_cases; p++)
	{
		int na, nb, t;
		fin >> t >> na >> nb;
		getline(fin, tmp);
		string str;
		trip_struct trip[500];
		for (int i=0; i<na; i++)
		{
			getline(fin, str);
			int a = (str[0] - '0') * 10 + (str[1] - '0');
			int b = (str[3] - '0') * 10 + (str[4] - '0');
			int c = (str[6] - '0') * 10 + (str[7] - '0');
			int d = (str[9] - '0') * 10 + (str[10] - '0');
			trip[i].leave = a * 60 + b;
			trip[i].arrive = c * 60 + d;
			trip[i].dir = 0;
			trip[i].free = 0;
		}
		for (int i=0; i<nb; i++)
		{
			getline(fin, str);
			int a = (str[0] - '0') * 10 + (str[1] - '0');
			int b = (str[3] - '0') * 10 + (str[4] - '0');
			int c = (str[6] - '0') * 10 + (str[7] - '0');
			int d = (str[9] - '0') * 10 + (str[10] - '0');
			trip[na + i].leave = a * 60 + b;
			trip[na + i].arrive = c * 60 + d;
			trip[na + i].dir = 1;
			trip[na + i].free = 0;
		}

		int n = na + nb;
		for (int i=0; i<n; i++)
		{
			for (int j=i+1; j<n; j++)
			{
				if (trip[i].leave > trip[j].leave)
				{
					trip_struct tmp_trip;
					tmp_trip = trip[i]; trip[i] = trip[j]; trip[j] = tmp_trip;
				}
			}
		}

		int ans[2];
		ans[0] = 0;
		ans[1] = 0;
		for (int i=0; i<n; i++)
		{
			if (trip[i].free == 0)
			{
				ans[trip[i].dir]++;
			}

			int k = trip[i].arrive + t;
			for (int j=i+1; j<n; j++)
			{
				if (k <= trip[j].leave && trip[j].dir != trip[i].dir && trip[j].free == 0)
				{
					trip[j].free = 1;
					break;
				}
			}
		}
		fout << "Case #" << p + 1 << ": " << ans[0] << " " << ans[1] << endl;
	}
	fin.close();
	fout.close();
	return 0;
}