#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace::std;

int main()
{
	string result = "";
	string invoke = "";
	int pos;
	map<string, char> combine;
	vector<string> oppose;
	ifstream input("D:\\in", ifstream::in);
	ofstream output("D:\\out", ofstream::out);
	char ch;
	int i, j;
	int len;
	string tmp, tmp1, tmp2, tmp3;
	int T, C, D, N;

	input >> T;
	for (i = 0; i < T; i++)
	{
		combine.clear();
		oppose.clear();
		result.clear();
		invoke.clear();
		pos = 0;
		input >> C;
		for (j = 0; j < C; j++)
		{
			input >> tmp;
			combine.insert(make_pair(tmp.substr(0,2), tmp[2]));
		}

		input >> D;
		for (j = 0; j < D; j++)
		{
			input >> tmp;
			oppose.push_back(tmp);
		}

		input >> N;
		input >> invoke;
		istringstream sout(invoke);
		sout >> ch;
		result.assign(1, ch);
		for (pos = 1; pos < N; pos++)
		{
			len = result.size();
			sout >> ch;
			if (len == 0)
			{
				result.assign(1, ch);
				continue;
			}
			tmp = tmp1.assign(1,ch) + tmp2.assign(1, result[len - 1]);
			tmp3 = tmp2.assign(1, result[len - 1]) + tmp1.assign(1,ch);

			if (combine.find(tmp) != combine.end())
			{
				result[len - 1] = combine[tmp];
				
				continue;
			}
			else if(combine.find(tmp3) != combine.end())
			{
				result[len - 1] = combine[tmp3];
				continue;
			}

			
			

			for (j = 0; j < len; j++)
			{
				tmp = tmp1.assign(1,ch) + tmp2.assign(1, result[j]);
				tmp3 = tmp2.assign(1, result[j]) + tmp1.assign(1,ch);

				if (find(oppose.begin(), oppose.end(), tmp) != oppose.end()
					|| find(oppose.begin(), oppose.end(), tmp3) != oppose.end())
				{
					result.clear();
					break;
				}
			}
			if (result.size() != 0)
				result.append(tmp.assign(1, ch));
		}

		output << "Case #" << i + 1 << ": [";
		len = result.size();
		if (len > 0)
		{
			output << result[0];
		}
		for (j = 1; j < len; j++)
		{
			output << ", " << result[j];
		}
		output << ']' << endl;
	}
	
}