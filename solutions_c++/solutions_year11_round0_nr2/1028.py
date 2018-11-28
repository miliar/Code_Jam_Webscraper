#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int n;
int nt;
int C, D;

char comb[256][256];
bool oppo[256][256];

char s[1000];

vector<int> a;

int main()
{
	scanf("%d", &nt);
	
	for(int tt = 1; tt <= nt; tt++)
	{	
		printf("Case #%d: ", tt);
		
		for(int i = 0; i < 256; i++) for(int j = 0; j < 256; j++) comb[i][j] = oppo[i][j] = 0;
		
		scanf("%d", &C);
				
		for(int i = 0; i < C; i++)
		{
			scanf("%s", s);
			comb[s[0]][s[1]] = s[2];
			comb[s[1]][s[0]] = s[2];
		}
		
		scanf("%d", &D);
		
		for(int i = 0; i < D; i++)
		{
			scanf("%s", s);
			oppo[s[0]][s[1]] = true;
			oppo[s[1]][s[0]] = true;
		}
		
		scanf("%d %s", &n, s);
		a.clear();
		
		for(int i = 0; i < n; i++)
		{
			a.push_back(s[i]);
			int len = a.size();
			if (len > 1)
			{
				if (comb[a[len - 1]][a[len - 2]])
				{
					char ch = comb[a[len - 1]][a[len - 2]];
					a.pop_back();
					a.pop_back();
					a.push_back(ch);
				}
				else
				{
					for(int i = 0; i < len - 1; i++)
					if (oppo[a[len - 1]][a[i]])
					{
						a.clear();
					}
				}				
			}			
		}
		
		printf("[");
		for(int i = 0; i < a.size(); i++)
		{
			if (i) printf(", ");
			printf("%c", (char)a[i]);
		}
		puts("]");
	}
	
	return 0;
}
