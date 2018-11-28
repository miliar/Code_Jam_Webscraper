#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int resp;

class n
{
	public:
	string name;
	//vector<n> c;
	int nl;
	n(string);
	n * c[100];
};

n::n(string name)
{
	this->name = name;
	nl = 0;
}

vector<string> ParsePath(char *path, int len)
{
	int i = 0, j;
	char str[100001];

	strcpy(str, path);

	vector<string> v;

	j = 1;
	for (i = 1 ; i < len ; i++)
	{
		if (str[i] == '/')
		{
			str[i] = 0;
			string hlp(&str[j]);
			j = i + 1;
			v.push_back(hlp);
		}
	}

	if (i != j)
	{
		string hlp(&str[j]);
		v.push_back(hlp);
	}

	return v;
}

void f(vector<string> v, n * N, int l)
{
	int i;
	bool is = false;

	if (v.size() > l)
	{
		for (i = 0 ; i < N->nl ; i++)
		{
			if (N->c[i]->name.compare(v[l]) == 0)
			{
				is = true;

					f(v, N->c[i], l + 1);
			}
		}
	}

	if (!is)
	{
		if (v.size() > l )
		{
			n * nNew = new n(v[l]);
			N->c[N->nl++] = nNew;
		
			f(v, nNew, l + 1);
			resp++;
		}
	}
}

int main()
{
	int T, N, M;
	int i, j;
	char str[100001];
	n nM(string(" "));

	//ParsePath("/home/gcj/finals", strlen("/home/gcj/finals"));

	scanf("%d", &T);
	for (i = 1 ; i <= T ; i++)
	{
		n nM(string(" "));

		scanf("%d", &N);
		scanf("%d", &M);

		for (j = 0 ; j < N ; j++)
		{
			scanf("%s", str);
			vector<string> v = ParsePath(str, strlen(str));
			f(v, &nM, 0);
		}

		resp = 0;
		for (j = 0 ; j < M ; j++)
		{
			vector<string> v;
			scanf("%s", str);
			v = ParsePath(str, strlen(str));
			f(v, &nM, 0);
		}

		//Case #1: 4
		printf("Case #%d: %d\n", i, resp);
	}

	return 0;
}
