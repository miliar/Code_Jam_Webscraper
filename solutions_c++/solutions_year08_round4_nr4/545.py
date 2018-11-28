#include <fstream>
#include <string>

using namespace std;

int n;
string s;
char r[2000];
bool v[100];
int x[100];
int ans;

void Try(int dep)
{
	if (dep >= n)
	{
		int cur = 1;
		for (int i=0; i<s.length() / n; i++)
		{
			for (int j=0; j<n; j++)
			{
				r[i * n + j] = s[i * n + x[j]];
			}
		}
		for (int i=1; i<s.length(); i++)
		{
			if (r[i] != r[i - 1])
			{
				cur++;
			}
		}
		if (cur < ans)
		{
			ans = cur;
		}
		return;
	}

	for (int i=0; i<n; i++)
	{
		if (v[i] == false)
		{
			v[i] = true;
			x[dep] = i;
			Try(dep + 1);
			v[i] = false;
		}
	}
}

int main()
{
	ifstream fin("c:\\codejam\\perm1.txt");
	ofstream fout("c:\\codejam\\perm_out.txt");
	int num_cases;
	fin >> num_cases;
	for (int p=0; p<num_cases; p++)
	{
		fin >> n;
		fin >> s;

		memset(v, 0, sizeof(v));
		ans = 1000000;
		
		Try(0);
		fout << "Case #" << p + 1 << ": " << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}