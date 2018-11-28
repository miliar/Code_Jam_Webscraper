#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <list>

using namespace std;

int main()
{
	int n;
	cin >> n;

	queue<string> output;

	for (int i = 0; i < n; i++)
	{
		int count;

		queue<char> base;
		vector<string> combine;
		vector<string> opposite;		

		cin >> count;

		for (int j = 0; j < count; j++)
		{
			string str;
			cin >> str;

			combine.push_back(str);
		}

		cin >> count;

		for (int j = 0; j < count; j++)
		{
			string str;
			cin >> str;

			opposite.push_back(str);
		}

		cin >> count;
		{
			string str;
			cin >> str;

			for (unsigned int i = 0; i < str.size(); i++)
			{
				base.push(str[i]);
			}
		}

		string list;
		
		while (!base.empty())
		{
			list += base.front();
			base.pop();

			if (list.size() == 1 && base.size())
			{
				list += base.front();
				base.pop();
			}

			if (list.size() == 1 && base.empty())
				break;

			bool replaced = false;

			for (unsigned int i = 0; i < combine.size(); i++)
			{
				string str = combine[i].substr(0, 2);

				string n, r;

				n += list[list.size() - 2];
				n += list[list.size() - 1];

				r += list[list.size() - 1];
				r += list[list.size() - 2];

				if (str.find(n) != -1 || 
					str.find(r) != -1)
				{
					list.replace(list.size() - 2, list.size(), 1, combine[i][2]);
					replaced = true;
					break;
				}
			}

			if (!replaced)
				for (unsigned int i = 0; i < list.size(); i++)
				{
					for (unsigned int j = 0; j < list.size(); j++)
					{
						string n, r;

						n += list[i];
						n += list[j];

						r += list[j];
						r += list[i];

						for (unsigned int k = 0; k < opposite.size(); k++)
						{
							string str = opposite[k];

							if (str.find(n) != -1 || 
								str.find(r) != -1)
							{
								list.clear();
								break;
							}
						}
					}
				}
		}

		ostringstream out;
		out << "Case #" << i + 1 << ": [";

		for (unsigned int i = 0; i < list.size(); i++)
		{
			out << list[i];

			if (i != list.size() - 1)
				out << ", ";
		}

		out << "]" << endl;

		output.push(out.str());
	}

	while (!output.empty())
	{
		cout << output.front();
		output.pop();
	}

	return 0;
}