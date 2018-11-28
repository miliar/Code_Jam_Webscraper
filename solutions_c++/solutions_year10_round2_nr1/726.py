#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

int nt;

int n, m;

char s[1001];

int nd;

struct Dir
{
	string name;

	vector<int> subdirs;

};

Dir dirs[20000];

int add(int x, char *s)
{
		if (!*s) return 0;

		s++; // skip '/'

		string a = "";

		while(*s && *s != '/')
		{
			a += *s;
			s++;
		}

		//printf("at %s, s = %s\n", dirs[x].name.c_str(), a.c_str());

		for(int i = 0; i < dirs[x].subdirs.size(); i++)
		{
		    //printf("   cmp to %s...\n", dirs[dirs[x].subdirs[i]].name.c_str());
			if (dirs[dirs[x].subdirs[i]].name == a)
				return add(dirs[x].subdirs[i], s);
		}


		int id = nd++;

		dirs[x].subdirs.push_back(id);

		dirs[id].name = a;
		dirs[id].subdirs.clear();

		//puts("added!");

        return add(id, s) + 1;
}

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
	    nd = 1;
	    dirs[0].name = "/";
	    dirs[0].subdirs.clear();
		
		printf("Case #%d: ", tt);

		scanf("%d %d", &m, &n);

		for(int i = 0; i < m; i++)
		{
			scanf("%s", s);
			add(0, s);			
		}

		int res = 0;

		for(int i = 0; i < n; i++)
		{
			scanf("%s", s);
			res += add(0, s);
		}

		printf("%d\n", res);
	}

	return 0;	
}