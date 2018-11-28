# include <vector>
# include <string>
# include <cstring>
# include <fstream>
# include <iostream>
using namespace std;

bool same(char a, char b, char c, char d)
{
	return (a == c && b == d) || (a == d && b == c);	
}
int main()
{
	ifstream cin("B-in.txt");
	ofstream cout("B-out.txt");

	int t;
	int case_num = 0;
	cin >> t;
	while(t - case_num++)
	{
		vector<char> v(110, '\0');
		int exists[26] = {0};
		int c, d, n;
		std::string comb[40];
		std::string rem[30];
		std::string str;
		cin >> c;
		for(int i = 0; i < c; ++i)
			cin >> comb[i];
		cin >> d;
		for(int i = 0; i < d; ++i)
			cin >> rem[i];
		cin >> n >> str;

		int index = 0;
		for(int i = 0; i < n; ++i)
		{
			v[index] = str[i];
			if(index > 0)
			{
				int j = 0;
				for(; j < c; ++j)
					if(same(comb[j][0], comb[j][1], v[index - 1], v[index]))
					{
						--exists[v[index - 1] - 'A'];
						v[index - 1] = comb[j][2];
						++exists[v[index - 1] - 'A'];
						break;
					}
				if(j == c)
				{
					int h = 0;
					for(; h < d; ++h)
						if((rem[h][0] == v[index] && exists[rem[h][1] - 'A']) || (rem[h][1] == v[index] && exists[rem[h][0] - 'A']))
						{
							index = 0;
							memset(exists, 0, sizeof(exists));
							break;
						}
					if(h == d)
					{
						++exists[v[index] - 'A'];
						++index;
					}
				}
			}
			else
			{
				++exists[v[index] - 'A'];
				++index;
			}
		}
		string ans = "[";
		for(int i = 0; i < index; ++i)
		{
			ans += v[i];
			if(i < index - 1)
				ans += ", ";
		}
		ans += "]";
		cout << "Case #" << case_num << ": " << ans << endl;
	}
	return 0;
}
