#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main()
{
	ifstream file;
	ofstream file2;
	file2.open("out");
	file.open("A-large.in");
	int t = 0;
	if(file.is_open())
	{
		file >> t;
		for(int i = 0; i < t; i++)
		{
			int s = 0;
			map<string, int> engines = map<string, int>();
			file >> s;
			string line;
			getline(file, line);
			for(int j = 0; j < s; j++)
			{
				getline(file, line);
				engines[line] = j;
			}
			int sum = s * (s + 1) / 2;
			bool done[100];
			for(int k = 0; k < s; k++)
				done[k] = false;
			int total = 0;
			int q = 0;
			file >> q;
			int answer = 0;
			getline(file, line);
			for(int j = 0; j < q; j++)
			{
				getline(file, line);
				if(!done[engines[line]])
				{
					done[engines[line]] = true;
					total += engines[line] + 1;
					if (sum == total)
					{
						total = engines[line] + 1;
						answer++;
						for (int k = 0; k < s; k++)
							done[k] = false;
						done[engines[line]] = true;
					}
				}
			}
			file2 << "Case #" << i + 1 << ": " << answer << endl;
		}
		file.close();
		file2.close();
	}
	return 0;
}