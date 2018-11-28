#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <utility>

using namespace std;

int main()
{
	set< pair<string, string> > s;
	int t, a, b;
	cin >> t;
	int k = 1;
	while(t--)
	{
		stringstream ss1, ss2;
		cin >> a >> b;
		ss1 << a;
    		string s1 = ss1.str();
		ss2 << b;
    		string s2 = ss2.str();
		for(int i = a; i < b; i++)
		{
			stringstream ss;
			ss << i;
    			string a1 = ss.str();
    			for(int j = 1; j < a1.size(); j++)
			{
				if(a1[j] >= a1[0])
				{
					string a2 = a1.substr(j) + a1.substr(0, j);
					if(a2.size() < s2.size() && a2 > a1)
					{
						s.insert(make_pair(a1, a2));
						//cout << a1 << " " << a2 << endl;
					}
					else if(a2.size() == s2.size() && a2 > a1)
					{
						if(a2 <= s2)
						{
							s.insert(make_pair(a1, a2));
							//cout << a1 << " " << a2 << endl;
						}
					}
				}
			}
		}
		cout << "Case #" << k << ": "<< s.size() << endl;
		s.clear();
		k++;
	}
	return 0;
}
