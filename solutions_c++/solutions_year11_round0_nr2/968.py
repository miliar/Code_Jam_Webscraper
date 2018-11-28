#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

struct CombineRule
{
	char base1, base2, result;
};

struct OppositeRule
{
	char base1, base2;
};

char temp[40];

CombineRule ScanCombineRule()
{
	scanf("%s", temp);
	CombineRule res;
	res.base1 = temp[0];
	res.base2 = temp[1];
	res.result = temp[2];
	return res;
}

OppositeRule ScanOppositeRule()
{
	scanf("%s", temp);
	OppositeRule res;
	res.base1 = temp[0];
	res.base2 = temp[1];
	return res;
}

const int N = 200;
const int K = 50;
int listLength;
char list[N];
int combineRuleCount;
int oppositeRuleCount;
CombineRule combineRule[K];
OppositeRule oppositeRule[K];


void Scan()
{
	scanf("%d", &combineRuleCount);
	for (int i = 0; i < combineRuleCount; i++)
		combineRule[i] = ScanCombineRule();
	scanf("%d", &oppositeRuleCount);
	for (int i = 0; i < oppositeRuleCount; i++)
		oppositeRule[i] = ScanOppositeRule();
	scanf("%d%s", &listLength, list);	
}

vector<char> result;

bool Opposite(char c1, char c2)
{
	for (int i = 0; i < oppositeRuleCount; i++)
		if ((oppositeRule[i].base1 == c1 && oppositeRule[i].base2 == c2) ||
			(oppositeRule[i].base1 == c2 && oppositeRule[i].base2 == c1))
			return true;
	return false;
}

char Combine(char c1, char c2)
{
	for (int i = 0; i < combineRuleCount; i++)
		if ((combineRule[i].base1 == c1 && combineRule[i].base2 == c2) ||
			(combineRule[i].base1 == c2 && combineRule[i].base2 == c1))
			return combineRule[i].result;
	return 0;
}

void ClearResult()
{
	while (result.size() > 0)
		result.pop_back();
}

void Solve()
{
	ClearResult();
	for (int i = 0; i < listLength; i++)
	{
		result.push_back(list[i]);
		int sz = result.size();
		if (sz > 1)
		{
			char comb = Combine(result[sz-1],result[sz-2]);
			if (comb != 0)
			{
				result.pop_back();
				result.pop_back();
				result.push_back(comb);
				continue;
			}
		}
		for (int j1 = 0; j1 < result.size(); j1++)
		for (int j2 = j1+1; j2 < result.size(); j2++)
			if (Opposite(result[j1], result[j2]))
			{
				ClearResult();
			}
	}
	printf("[");
	for (int i = 0; i < result.size(); i++)
	{
		printf("%c", result[i]);
		if (i+1 != result.size())
			printf(", ");
	}
	printf("]\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Scan();
		printf("Case #%d: ", i+1);
		Solve();
	}
	return 0;
}