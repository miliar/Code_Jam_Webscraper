#include <fstream>
#include <map>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

inline string shift(const string &str)
{
	char tmp = str[str.size() - 1];
	string res = str;
	for (int i = str.size() - 1; i > 0; i--)
	{
		res[i] = res[i-1];
	}
	res[0] = tmp;
	return res;
}

int main()
{
	ifstream file("problem_c.txt");

	if (file.is_open())
	{
		int T;
		file >> T;

		string line;
		getline (file, line);

		int A, B, res;
		string str;

		for (int i = 1; i <= T; i++)
		{
			file >> A >> B;

			res = 0;
			for (int j = A; j <= B; j++)
			{
				stringstream ss;
				ss << j;
				str = ss.str();

				int n = str.size() - 1;
				for (int h = 0; h < n; h++)
				{
					str = shift(str);
					istringstream buffer(str);
					int v;
					buffer >> v;
					if (v > j && v <= B)
					{
						//cout << "(" << j << "," << /*str << "," <<*/ v << ")" << " " << endl;
						res++;
					}
				}
			}

			cout << "Case #" << i << ": "<< res << endl;
		}

		file.close();
	}

	return 0;
}
