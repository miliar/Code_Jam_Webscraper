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

	string str;
	getline(cin, str);

	queue<int> blue, orange;
	queue<pair<char, int> > overall;

	queue<string> output;

	for (int i = 0; i < n; i++)
	{
		getline(cin, str);

		istringstream s(str);

		int k;
		s >> k;

		for (int j = 0; j < k; j++)
		{
			int pos;
			s >> str;
			s >> pos;
			if (str == "O")
			{
				orange.push(pos);
			}
			else
			{
				blue.push(pos);
			}

			overall.push(make_pair(str[0], pos));
		}

		int blue_pos = 1, orange_pos = 1;
		int time = 0;

		while (!overall.empty())
		{
			pair<char, int> p = overall.front();
			overall.pop();			
			
			if (p.first == 'B')
			{
				do
				{
					if (blue_pos == p.second)
					{
						if (!orange.empty() && orange_pos != orange.front())
						{
							if (orange_pos < orange.front())
								orange_pos++;
							else
								orange_pos--;
						}

						blue.pop();

						time++;

						break;
					}

					if (blue_pos < blue.front())
						blue_pos++;
					else
						blue_pos--;

					if (!orange.empty() && orange_pos != orange.front())
					{
						if (orange_pos < orange.front())
							orange_pos++;
						else
							orange_pos--;
					}

					time++;
				}
				while (!orange.empty() || !blue.empty());
			}
			else
			{
				do
				{
					if (orange_pos == p.second)
					{
						if (!blue.empty() && blue_pos != blue.front())
						{
							if (blue_pos < blue.front())
								blue_pos++;
							else
								blue_pos--;
						}

						orange.pop();

						time++;

						break;
					}

					if (orange_pos < orange.front())
						orange_pos++;
					else
						orange_pos--;

					if (!blue.empty() && blue_pos != blue.front())
					{
						if (blue_pos < blue.front())
							blue_pos++;
						else
							blue_pos--;
					}

					time++;
				}
				while (!orange.empty() || !blue.empty());
			}
		}

		ostringstream out;
		out << "Case #" << i + 1 << ": " << time << endl;
		output.push(out.str());

		while (!orange.empty()) orange.pop();
		while (!blue.empty()) blue.pop();
	}

	while (!output.empty())
	{
		cout << output.front();
		output.pop();
	}

	return 0;
}