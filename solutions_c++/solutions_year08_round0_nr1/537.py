#include <iostream>
#include <string>
#include <map>
#include <cstring>
#include <cstdio>

#define S 128
#define Q 1024

using namespace std;

int main (void)
{
	int x, n;
	int s, q;
	int i;
	int res;
	int used, id;
	map<string, int> engine;
	bool search[S];
	char c_name[S];

	string name;

	cin >> n;

	for(x = 1; x <= n; x++)
	{
		cin >> s;
		memset(search, 0, s);
		used = 0;
		res = 0;

		for(i = 0; i < s; i++)
		{
			gets(c_name);
			name.assign(c_name);
			if(!name.size())
			{
				i--;
				continue;
			}
			//cout << name << endl;
			engine[name] = i;
		}
		//cout << s << "!" << endl;
		cin >> q;
		for(i = 0; i < q; i++)
		{
			gets(c_name);
			name.assign(c_name);
			if(!name.size())
			{
				i--;
				continue;
			}
			//cout << name << endl;
			id = engine.find(name)->second;
			//cout << id << endl;
			if(!search[id])
			{
				used++;
				search[id] = true;
				if(used >= s)
				{
					memset(search, 0, s);
					used = 1;
					search[id] = true;
					res++;
				}
			}
		}

		cout << "Case #" << x << ": " << res << endl;
	}
	return 0;
}
