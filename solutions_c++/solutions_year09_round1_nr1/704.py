#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <set>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

vector<int> bases;

int Calc()
{
	vector<int> shown;
	for(int i = 2;;++i)
	{
		bool flag = true;
		for(int j = bases.size() - 1; j >= 0; --j)
		{
			shown.clear();
			shown.push_back(i);

			int sum = i, n, b = bases[j];
			while(true)
			{
				n = sum;
				sum = 0;
				while(n > 0)
				{
					sum += (n % b) * (n % b);
					n /= b;
				}
				if(sum == 1)
				{
					break;
				}
				else
				{
					for(int k = 0; k < shown.size(); ++k)
					{
						if(sum == shown[k])
						{
							flag = false;
							break;
						}
					}
					if(flag)
					{
						shown.push_back(sum);
					}
					else
					{
						break;
					}
				}
			}
			if(!flag)
			{
				break;
			}
		}
		if(flag)
		{
			return i;
		}
	}
}

int main()
{
	int t;

	fin >> t;
	string s;
	getline(fin, s);

	for(int i = 0; i < t; ++i)
	{
		bases.clear();
		getline(fin, s);
		for(int j = 0; j < s.length(); j += 2)
		{
			if(s[j] > '1')
			{
				bases.push_back(s[j] - '0');
			}
			else if(s[j] == '1')
			{
				bases.push_back(10);
				++j;
			}
		}

		fout << "Case #" << i + 1 << ": " << Calc() << endl;
	}

	return 0;
}