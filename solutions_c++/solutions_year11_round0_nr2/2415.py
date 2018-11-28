#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<cstdio>
#include<string>
#include<list>
using namespace std;

class rezept
{
public:
	char a, b, c;
	rezept(char _a = '_', char _b = '_', char _c = '_'): a(_a), b(_b), c(_c) {}
};
vector<rezept> rs;
void print_str(string &s)
{
	cout << "[";
	for(int i = 1; i < s.size(); i++)
		if(i == 1)
			cout << s[i];
		else
			cout << ", " << s[i];
	cout << "]";

	return;
}

char get_new_el(char a, char b)
{
	for(int i = 0; i < rs.size(); i++)
		if(rs[i].a == a && rs[i].b == b || rs[i].a == b && rs[i].b == a)
			return rs[i].c;
	return ' ';
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out", "w", stdout);
	
	int t;
	string s;
	cin >> t;
	for(int cs = 1; cs <= t; cs++)
	{
		rs.clear();
		int c;
		cin >> c;
		
		for(int i = 0; i < c; i++)
		{
			cin >> s;
			rs.push_back(rezept(s[0], s[1], s[2]));
		}




		int d;
		cin >> d;
		vector<pair<char, char> > os;
		for(int i = 0; i < d; i++)
		{
			cin >> s;
			os.push_back(make_pair(s[0], s[1]));
		}



		int n;
		bool found;
		char q;
		cin >> n;
		char str[1000];
		scanf("%s", str);
		int len = strlen(str);

		string w = " ";
		for(int i = 0; i < len; i++)
		{
			q = get_new_el(w[w.size()-1], str[i]);
			if(q != ' ')
				w[w.size()-1] = q;
			else
			{
				found = false;
				for(int j = 0; !found && j < os.size(); j++)
					if(os[j].first == str[i] && w.find(os[j].second)!=string::npos || os[j].second == str[i] && w.find(os[j].first)!=string.npos)
						found = true;
				if(!found)
					w += str[i];
				else
					w = " ";
			}
		}





		cout << "Case #" << cs << ": ";
		print_str(w);
		cout << endl;
	}





	return 0;
}