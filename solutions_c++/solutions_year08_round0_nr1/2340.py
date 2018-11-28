#include <stdio.h>
#include <memory.h>
#include <map>

using namespace std;

struct Engine
{
	char name[101];

	Engine()
	{
		memset(name, sizeof(name), 0);
	}

	void Read()
	{
		gets(name);
	}

	bool operator == (Engine value)
	{
		return (strcmp(this->name, value.name) == 0);
	}
};

int n, s, q, rez, pointer;
Engine engines[100];
Engine query[1000];
Engine current;
map <int, Engine> appearence;
map <int, Engine>::iterator iter;

void Init()
{
	appearence.clear();
	for (int i = 0; i < s; i++)
		engines[i] = Engine();
	for (int i = 0; i < q; i++)
		query[i] = Engine();
	current = Engine();
	s = 0;
	q = 0;
	rez = 0;
	pointer = 0;
}

void Calculate()
{
	int tmp = q;
	appearence.clear();
	for (int i = 0; i < s; i++)
		for (int j = pointer; j < q; j++)
		{
			if (engines[i] == query[j])
			{
				appearence[j] = engines[i];
				break;
			}

			if (j == q - 1)
			{
				appearence[tmp++] = engines[i];
			}
		}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		Init();

		scanf("%d\n", &s);
		for (int j = 0; j < s; j++)
		{
			engines[j].Read();
			appearence[j] = engines[j];
		}

		scanf("%d\n", &q);
		for (int j = 0; j < q; j++)
			query[j].Read();

		while(pointer < q)
		{
			Calculate();
			iter = appearence.end();
			iter--;
			if (iter->second == current)
				iter--;
			current = iter->second;
			rez++;
			pointer = iter->first;
		}
		if (rez == 0)
			rez++;
		printf("Case #%d: %d\n", i + 1, rez - 1);
	}
	return 0;
}