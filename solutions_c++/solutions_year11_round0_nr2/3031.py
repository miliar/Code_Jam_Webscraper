#include <set>
#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int nperehod, nopposed, len;
map <string, char> MapPerehod;
set <char> SetOpposed[26];
char ans[150];
string a;

void solve(int id)
{                    	
	MapPerehod.clear();
	for (int i = 0; i < 26; i++) SetOpposed[i].clear();

	scanf("%d", &nperehod);
	for (int i = 0; i < nperehod; i++)
	{
		string t, s;
	 	cin >> t;
	 	s = t.substr(0, 2);
	 	MapPerehod[s] = t[2];
	 	swap(s[0], s[1]);
	 	MapPerehod[s] = t[2];
	}
	scanf("%d", &nopposed);
	for (int i = 0; i < nopposed; i++)
	{
	 	string t; 
	 	cin >> t;
	 	SetOpposed[t[0] - 'A'].insert(t[1]);
	 	SetOpposed[t[1] - 'A'].insert(t[0]);
	}
	scanf("%d ", &len);
	cin >> a;
	int lenans = 0;
	for (int i = 0; i < len; i++)
	{
	 	string s;
	 	if (i == 0) 
	 	{
	 	 	ans[lenans++] = a[i];
	 		goto end;
	 	}

	 	s = a.substr(i, 1);
	 	s += ans[lenans - 1];	
	 	if (MapPerehod.find(s) != MapPerehod.end())
	 	{
	 		ans[lenans - 1] = MapPerehod[s];
			goto end;
		}
		
		if (SetOpposed[a[i] - 'A'].empty())
		{
		 	ans[lenans++] = a[i];
		 	goto end;
		}
		for (int j = lenans - 1; j >= 0; j--)
			if (SetOpposed[a[i] - 'A'].find(ans[j]) != SetOpposed[a[i] - 'A'].end())
			{
				lenans = 0;
				goto end;
			}

		ans[lenans++] = a[i];
		end:{};
	}
	printf("Case #%d: [", id);
	if (lenans != 0) 
		printf("%c", ans[0]);
	for (int i = 1; i < lenans; i++)
		printf(", %c", ans[i]);
   	printf("]\n");
}                           

int main() 
{
 	freopen("ZZ.in", "r", stdin);
 	freopen("ZZ.out", "w", stdout);

	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++)
		solve(i);


 	return 0;
}
