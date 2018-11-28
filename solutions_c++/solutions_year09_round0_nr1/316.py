#include <set>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
#define ONLINEJUDGE
#define MAXN 5500

vector<string> word;
int L, N, D;
int iBuf;
int main()
{
#ifdef ONLINEJUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	int iNum, i, j, k, cnt, iRet, m;
	bool mark;
	string str, str1;
	vector<string> Elem;
	set<char> s;

	word.clear();
	scanf("%d%d%d", &L, &D, &N);
	for(i = 0; i < D; i++)
	{
		cin >> str;
		word.push_back(str);
	}
	for(i = 0; i < N; i++)
	{
		cin >> str;
		Elem.clear();
		iRet = 0;
		for(j = 0; j < str.length(); j++)
		{
			if(str[j] == '(')
			{
				str1 = "";
				j++;
				while(str[j] != ')')
				{
					str1 += str[j++];
				}
				Elem.push_back(str1);
			}
			else
			{
				str1 = "";
				str1 += str[j];
				Elem.push_back(str1);
			}
		}
		for(k = 0; k < D; k++)
		{
			mark = true;
			for(j = 0; j < Elem.size(); j++)
			{
				if(Elem[j].find(word[k][j]) == string::npos)
				{
					mark = false;
					break;
				}
			}
			if(mark) iRet++;
		}
		printf("Case #%d: %d\n", i + 1, iRet);
	}

	return 0;
}