#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int L, D, N;

char s[100000];

vector<string> words;

bool match(const char *s, const char *p)
{
	for(int i = 0; i < L; i++)
		if (*p == '(')
		{
			p++;
			bool ok = false;

			while(*p != ')')
			{
				if (*p == *s) ok = true;
				p++;
			}

			p++;
			s++;

			if (!ok) return false;
		}
		else
		{
			if (*p != *s) return false;
			p++;
			s++;
		}

   return true;

}

int main()
{
	scanf("%d %d %d", &L, &D, &N);

	for(int i = 0; i < D; i++)
	{
		scanf("%s", s);
		words.push_back(s);
	}

	for(int i = 1; i <= N; i++)
	{
		scanf("%s", s);

		printf("Case #%d: ", i);

		int res = 0;

		for(int j = 0; j < D; j++) if (match(words[j].c_str(), s)) res++;

		printf("%d\n", res);
	}

	return 0;
}