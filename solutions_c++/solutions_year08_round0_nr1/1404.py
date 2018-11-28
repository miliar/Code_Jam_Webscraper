#include <iostream>
#include <string>
#include <map>
using namespace std;


map<string, int> name2id;
int res = 0, hostNum = 0;
void InputData()
{
	name2id.clear();
	string name = "";
	int n = 0;
	char line[1024], ch;

	scanf("%d%c", &n, &ch);
	hostNum = n;
	for(int i = 0; i < n; i++)
	{
		gets(line);
		int len = strlen(line);
		name = "";
		for(int j = 0; j < len; j++)
		{
			name += line[j];
		}
		name2id[name] = i;
	}
}
void Process()
{
	res = 0;
	string name = "";
	int n = 0;
	int visit[100] = {0}, num = 0;
	char line[1024], ch;

	scanf("%d%c", &n, &ch);
	for(int i = 0; i < n; i++)
	{
		gets(line);
		int len = strlen(line);
		name = "";
		for(int j = 0; j < len; j++)
		{
			name += line[j];
		}
		if(name2id.find(name) != name2id.end())
		{
			int id = name2id[name];
			if(visit[id] == 0)
			{
				visit[id] = 1;
				num++;
				if(num == hostNum)
				{
					res++;
					num = 1;
					memset(visit, 0, sizeof(visit));
					visit[id] = 1;
				}
			}
		}
	}
}
int main()
{
	int t = 0;

	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		InputData();
		Process();
		printf("Case #%d: %d\n", i, res);		
	}
	
	return 0;
}