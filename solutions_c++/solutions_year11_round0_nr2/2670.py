#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void print (vector<char> lista)
{
	printf ("[");
	for (int i = 0; i < (int) lista.size(); ++i)
	{
		if(i) printf (", ");
		printf ("%c", lista[i]);
	}
	printf ("]\n");
}

int main (void)
{
	int teste;
	vector<char> lista;
	set<pair<char,char> > opos;
	map<pair<char,char>,char> combo;
	
	scanf ("%d", &teste);
	
	for (int t = 1; t <= teste; t++)
	{
		opos.clear();
		combo.clear();
		lista.clear();
		
		int c;
		scanf ("%d", &c);
		
		for (int i = 0; i < c; ++i)
		{
			char s[4];
			scanf ("%s", s);
			
			combo[make_pair(s[0], s[1])] = combo[make_pair(s[1], s[0])] = s[2];
		}
		
		int d;
		scanf ("%d", &d);
		
		for (int i = 0; i < d; ++i)
		{
			char s[4];
			scanf ("%s", s);
			
			opos.insert(make_pair(s[0], s[1]));
			opos.insert(make_pair(s[1], s[0]));
		}
		
		int n;
		scanf ("%d", &n);
		
		for (int i = 0; i < n; i++)
		{
			char b;
			scanf (" %c", &b);
			
			if (lista.size() > 0)
			{
				map<pair<char,char>,char>::iterator it = combo.find(make_pair(b, lista.back()));
				if (it != combo.end())
				{
					lista[lista.size()-1] = it->second;
				}
				else
				{
					bool problema = false;
					for (int j = 0; j < (int) lista.size(); ++j)
					{
						set<pair<char,char> >::iterator it = opos.find(make_pair(lista[j], b));
						if (it != opos.end())
						{
							problema = true;
							break;
						}
					}
					
					if (problema)
					{
						lista.clear();
					}
					else
					{
						lista.push_back(b);
					}
				}
			}
			else
			{
				bool problema = false;
				for (int j = 0; j < (int) lista.size(); ++j)
				{
					set<pair<char,char> >::iterator it = opos.find(make_pair(lista[j], b));
					if (it != opos.end())
					{
						problema = true;
						break;
					}
				}
				
				if (problema)
				{
					lista.clear();
				}
				else
				{
					lista.push_back(b);
				}
			}
		}
		
		printf ("Case #%d: ", t);
		
		print(lista);
	}

	return 0;
}

