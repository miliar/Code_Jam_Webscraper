#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <cmath>
#include <set>
#include <stack>
#include <sstream>

using namespace std;

string toString(int val)
{
    ostringstream oss;
    oss << val;
    return oss.str();
}

int fromString(const std::string& s) 
{
  istringstream iss(s);
  int res;
  iss >> res;
  return res;
}	

int main() 
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": [";
		int c;
		cin >> c;
		vector <string> combines(c);
		for (int i = 0; i < c; ++i)
		{
			cin >> combines[i];
		}
		int d;
		cin >> d;
		vector <string> opposed(d);
		for (int i = 0; i < d; ++i)
		{
			cin >> opposed[i];
		}
		int length;
		cin >> length;
		string s;
		cin >> s;
		vector <char> answer;
		for (int i = 0; i < length; ++i)
		{
			answer.push_back(s[i]);
			if (answer.size() > 1)
			{
				int size = answer.size();
				for (int j = 0; j < c; ++j)
				{
					if (((answer[size - 2] == combines[j][0]) && (answer[size - 1] == combines[j][1])) || ((answer[size - 2] == combines[j][1]) && (answer[size - 1] == combines[j][0])))
					{
						answer.pop_back();
						answer.pop_back();
						answer.push_back(combines[j][2]);
						break;
					}
				}
			}
			vector <bool> first(d, false), second(d, false);
			for (int j = 0; j < d; ++j)
			{
				for (int k = 0; k < (int) answer.size(); ++k)
				{
					if (opposed[j][0] == answer[k])
					{
						first[j] = true;
					}
					if (opposed[j][1] == answer[k])
					{
						second[j] = true;
					}
				}					
			}
			for (int j = 0; j < d; ++j)
			{
				if ((first[j]) && (second[j]))
				{
					answer.clear();
				}
			}
		}		
		for (int i = 0; i < (int) answer.size() - 1; ++i)
		{
			cout << answer[i] << ", ";
		}
		if (answer.size() > 0)
		{
			cout << answer[answer.size() - 1];
		}
		cout << "]" << endl;
	}
	return 0;
}







