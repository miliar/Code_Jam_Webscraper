#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int L,D,N;

char buf[10000];
vector<string> words;

int pat[510][20];

inline int getBit(char c)
{
	return 1<<(c-'a');
}

void insertPat(int pos, string mes)
{
	int pos2 = 0;
	for (int i=0; i<mes.size(); i++)
	{
		if (mes[i]=='(')
		{
			int val = 0;
			for (i=i+1; mes[i]!=')'; i++)
			{
				val |= getBit(mes[i]);
			}
			pat[pos][pos2] = val;
			pos2++;
			continue;
		}
		pat[pos][pos2] = getBit(mes[i]);
		pos2++;
	}
}

bool can(int patId, int wId)
{
	for (int i=0; i<L; i++)
	{
		if ((pat[patId][i] & getBit(words[wId][i])) == 0)
			return false;
	}
	return true;
}

int main()
{
	scanf("%d%d%d", &L, &D, &N);
	for (int i=0; i<D; i++)
	{
		scanf("%s", buf);
		words.push_back(buf);
	}
	for (int i=0;i<N; i++)
	{
		scanf("%s", buf);
		insertPat(i, buf);
	}

	for (int i=0; i<N; i++)
	{
		int res = 0;
		for (int j=0; j<D; j++)
		{
			if (can(i,j))
				res++;
		}
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}