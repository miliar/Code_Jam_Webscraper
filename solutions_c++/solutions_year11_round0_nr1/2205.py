#include <fstream>
#include <cmath>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T, N;
	fin >> T;
	for(int t=0; t<T; t++)
	{
		char c[201];
		int num[201];
		int x = 1, y = 1;
		int ans = 0;
		fin >> N;
		for(int i=0; i<N; i++)
		{
			fin >> c[i];
			fin >> num[i];
		}
		for(int i=0; i<N; i++)
		{
			if(c[i] == 'O')
			{
				ans += abs(x - num[i]) + 1;
				int next = -1;
				for(int j=i; j<N; j++)
					if(c[j] == 'B')
					{
						next = num[j];
						break;
					}
				if(next != -1)
				if(abs(next - y) <= abs(x - num[i]) + 1)
					y = next;
				else
					if(y <= next)
						y = y + (abs(x - num[i]) + 1);
					else
						y = y - (abs(x - num[i]) + 1);
				x = num[i];
			}
			else
			{
				ans += abs(y - num[i]) + 1;
				int next = -1;
				for(int j=i; j<N; j++)
					if(c[j] == 'O')
					{
						next = num[j];
						break;
					}
				if(next != -1)
				if(abs(next - x) <= abs(y - num[i]) + 1)
					x = next;
				else
					if(x <= next)
						x = x + (abs(y - num[i]) + 1);
					else
						x = x - (abs(y - num[i]) + 1);
				y = num[i];
			}
		}
		fout << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}

