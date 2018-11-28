#include <cstdio>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

int ans;
vector <string> name;
vector < vector <int> > index;

char comp[100][110], cnt;

void init()
{
	vector<int> temp;
	ans = 0;
	name.clear();
	name.push_back("");
	index.clear();
	index.push_back(temp);
}

void analyse(char inp[])
{
	int i, j, k, len;
	char temp[110];

	cnt = 0;
	len = strlen(inp);
	i = j = 1;
	while(i < len)
	{
		while(j < len)
		{
			j++;
			if(j >= len || inp[j] == '/') break;
		}
		for(k = i; k < j; k++)
			temp[k-i] = inp[k];
		temp[k-i] = '\0';
		strcpy(comp[cnt++], temp);
		
		i = j+1;
	}
}

int find(char str[], int par)
{
	int i, len;

	len = index.at(par).size();
	for(i = 0; i < len; i++)
	{
		//printf("(%s,%s)", str, name.at(index.at(par).at(i)).c_str());
		if(!strcmp(str, name.at(index.at(par).at(i)).c_str()))
		{
			return index.at(par).at(i);
		}
	}
	return -1;
}

void mkdir(char str[], int par)
{
	int num;
	vector<int> temp;

	name.push_back(str);
	num = name.size() - 1;
	index.at(par).push_back(num);
	index.push_back(temp);
}

void enroll(char inp[])
{
	int i, p = 0, child;

	analyse(inp);
	for(i = 0; i < cnt; i++)
	{
		child = find(comp[i], p);
		if(child < 0) mkdir(comp[i], p);
		p = child;
		if(p < 0) p = name.size() - 1;
	}
}

void make(char inp[])
{
	int i, p = 0, child;

	analyse(inp);
	for(i = 0; i < cnt; i++)
	{
		//printf("%s %d\n", comp[i], p);
		child = find(comp[i], p);
		//printf("child : %d", child);
		if(child < 0)
		{
			ans++;
			mkdir(comp[i], p);
		}
		
		p = child;
		if(p < 0) p = name.size() - 1;
	}
}

int main()
{
	int t, n, m, i, z = 1;
	char inp[110];

	scanf("%d", &t);

	while(t > 0)
	{
		init();
		scanf("%d %d", &n, &m);
		for(i = 0; i < n; i++)
		{
			scanf("%s", inp);
			enroll(inp);
		}
		for(i = 0; i < m; i++)
		{
			scanf("%s", inp);
			make(inp);
		}

		printf("Case #%d: %d\n", z++, ans);
		t--;
	}

	return 0;
}