#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin("c:\\codejam\\saving3.txt");
	ofstream fout("c:\\codejam\\saving_out.txt");
	int num_cases;
	fin >> num_cases;
	string tmp;
	for (int p=0; p<num_cases; p++)
	{
		int n, m;
		fin >> m;
		string name[200];
		getline(fin, tmp);
		for (int i=0; i<m; i++)
		{
			getline(fin, name[i]);
		}

		int last_cost[200];
		int cur_cost[200];
		for (int i=0; i<m; i++)
		{
			last_cost[i] = 0;
			cur_cost[i] = 0;
		}

		fin >> n;
		getline(fin, tmp);
		for (int i=0; i<n; i++)
		{
			string query;
			getline(fin, query);

			for (int j=0; j<m; j++)
			{
				last_cost[j] = cur_cost[j];
			}

			for (int j=0; j<m; j++)
			{
				if (query == name[j])
				{
					cur_cost[j] = 1000000;
				}
				else
				{
					cur_cost[j] = last_cost[j];
					int b = 1000000;
					for (int k=0; k<m; k++)
					{
						if (k != j && last_cost[k] + 1 < b)
						{
							b = last_cost[k] + 1;
						}
					}
					if (b < cur_cost[j])
					{
						cur_cost[j] = b;
					}
				}
			}
		}

		int ans = 1000000;
		for (int i=0; i<m; i++)
		{
			if (cur_cost[i] < ans)
			{
				ans = cur_cost[i];
			}
		}
		
		fout << "Case #" << p + 1 << ": " << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}