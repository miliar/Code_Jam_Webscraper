#include <iostream>
#include <vector>
#include <string>


using namespace std;


string s;
vector<char> v;
bool annihilate[146][146];
char transit[146][146];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int _ = 0; _ < t; _++)
	{
		memset(transit, 0, sizeof(transit));
		memset(annihilate, false, sizeof(annihilate));
		int c;
		scanf("%d", &c);
		for(int i = 0; i < c; i++)
		{
			cin >> s;
			transit[s[0]][s[1]] = transit[s[1]][s[0]] = s[2];
		}
		scanf("%d", &c);
		for(int i = 0; i < c; i++)
		{
			cin >> s;
			annihilate[s[0]][s[1]] = annihilate[s[1]][s[0]] = true;
		}
		int n;
		cin >> n >> s;
		v.clear();
		for(int i = 0; i < n; i++)
		{
			v.push_back(s[i]);
			if(v.size() > 1)
			{
				if(transit[v[v.size() - 1]][v[v.size() - 2]] != 0)
				{
					char c = transit[v[v.size() - 1]][v[v.size() - 2]];
					v.pop_back();
					v.pop_back();
					v.push_back(c);
				}
				else
				{
					for(int i = 0; i < v.size(); i++)
						if(annihilate[v[i]][v.back()])
						{
							v.clear();
							break;
						}
				}
			}
		}
		printf("Case #%d: [", _ + 1);
		for(int i = 0; i < v.size(); i++)
		{
			printf("%c", v[i]);
			if(i != v.size() - 1)
				printf(", ");
		}
		printf("]\n");
	}
}