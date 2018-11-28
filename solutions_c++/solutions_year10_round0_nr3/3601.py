#include <fstream>
#include <queue>
using namespace std;

int main()
{
	int t = 0;
	ifstream fin("D:\\C-small-attempt0.in");
	ofstream fout("D:\\output.txt");

	fin >> t;

	for (int i = 0; i < t; i ++)
	{
		int r, k, n;
		queue<int> a, b;

		fin >> r >> k >> n;
		
		for (int j = 0; j < n; j++)
		{
			int tmp;
			fin >> tmp;
			a.push(tmp);
		}

		int money = 0;
		for (int j = 0; j < r; j++)
		{
			int sum = 0;
			while (!a.empty() && sum + a.front() <= k)
			{
				sum += a.front();
				b.push(a.front());
				a.pop();
			}
			while (!b.empty())
			{
				a.push(b.front());
				b.pop();
			}
			money += sum;
		}

		fout << "Case #" << i + 1 << ": " << money << endl;
	}

	fout.close();
}