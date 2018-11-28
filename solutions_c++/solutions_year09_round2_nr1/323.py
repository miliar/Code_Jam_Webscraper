#include <algorithm>
#include <stdio.h>
#include <string>
#include <map>

#define MAX 128

using namespace std;

class tree
{
public:
	double val, fii;
	string feat;

	tree *st, *dr;
} *radArb;
int testCases, poz;
char buffIn[1000000];
map <string, int> mapAre;

inline void citesteSubArb(tree* &nod)
{
	nod = new tree;
	poz++;
	double nr = 0, b10 = 1;
	if (buffIn[poz] == '1')
	{
		nod->val = 1;
		for (; (buffIn[poz] >= '0' && buffIn[poz] <= '9') || buffIn[poz] == '.'; poz++);
	}
	else
	{
		for (poz += 2; buffIn[poz] >= '0' && buffIn[poz] <= '9'; poz++)
		{
			b10 *= 10;
			nr = nr + (buffIn[poz] - '0') / b10;
		}
		
		nod->val = nr;
	}

	if (buffIn[poz] != ')')
	{
		nod->fii = 1;
		for (; buffIn[poz] >= 'a' && buffIn[poz] <= 'z'; poz++)
			nod->feat = nod->feat + buffIn[poz];

		citesteSubArb(nod->st);
		citesteSubArb(nod->dr);
	}
	else nod->fii = 0;
	
	poz++;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &testCases);

	for (int test = 1; test <= testCases; test++)
	{
		delete radArb;

		printf("Case #%d:\n", test);

		int l;
		scanf("%d\n", &l);
		memset(buffIn, 0, sizeof(buffIn));

		for (int i = 1; i <= l; i++)
		{
			char str[128];
			fgets(str, 128, stdin);

			for (int sz = strlen(buffIn), i = 0, szS = strlen(str); i < szS; i++)
				buffIn[sz + i] = str[i];
		}

		int dif = 0;
		for (int i = 0, sz = strlen(buffIn); i + dif <= sz; i++)
		{
			for (; ; dif++)
				if (buffIn[i + dif] != ' ' && buffIn[i + dif] != '\n')
					break;

			buffIn[i] = buffIn[i + dif];
		}
		for (int i = strlen(buffIn); i < 1000000; i++)
			buffIn[i] = 0;
		
		poz = 0;
		citesteSubArb(radArb);

		int a;
		scanf("%d\n", &a);

		for (scanf("%d\n", &a); a; a--)
		{
			mapAre.clear();
			char nume[128];
			int fe;
			scanf("%s %d", &nume, &fe);

			for (int i = 1; i <= fe; i++)
			{
				char strFe[128];
				scanf("%s ", &strFe);
				string strAux = strFe;
	
				mapAre[strAux] = 1;
			}

			double sol = 1;

			for (tree *nod = radArb; ; )
			{
				sol *= nod->val;

				if (nod->fii)
					if (mapAre[nod->feat])
						nod = nod->st;
					else nod = nod->dr;
				else break;
			}

			printf("%.7lf\n", sol);
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
