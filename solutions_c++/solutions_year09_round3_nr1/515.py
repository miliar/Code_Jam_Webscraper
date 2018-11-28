#include <vector>
#include <queue>
#include <string>
#include <stdio.h>

using namespace std;

int ind(char c)
{
	if (c>='0' && c<='9') return c-'0';
	return 10 + (c-'a');
}

int main()
{
	int i,l,k,j;
	int T;
	string s;
	char c;
	
	int x, y;

	scanf("%d", &T);
	scanf("%c", &c);
	for (k=0; k<T; k++)
	{

		vector <int> v(70, 0);
		vector <int> vn(70, 0);
		vector <bool> used(70, false);
		
		s = "";
		while (1)
		{
			if (scanf("%c", &c) == EOF) break;
			if (c == '\n') break;
			s += c;

			v[ind(c)]++;

		}

		int il = 0;
		for (i=0; i<70; i++) if (v[i] > 0) il++;

		char c;
		int val = 2;

		// pierwszy znak za 1
		c = s[0];
		//printf("znak = %c\n", c);
		used[ind(c)] = true;
		for (i=0; i<s.size(); i++) if (s[i] == c) vn[i] = 1;

		int p = 1;
		while (p<s.size() && s[p] == c) p++; // szukamy drugiego znaku

		if (p < s.size())
		{
			c = s[p];
			//printf("znak = %c\n", c);
			used[ind(c)] = true;
			for (i=0; i<s.size(); i++) if (s[i] == c) vn[i] = 0;
			p++;

			for (i=p; i<s.size(); i++)
			{
				char c = s[i];
				if (!used[ ind(c) ]) // nowy znak
				{
					//printf("znak = %c\n", c);
					used[ ind(c) ] = true;
					for (l=i; l<s.size(); l++) if (s[l] == c) vn[l] = val;
					val++;
				}
			}
		}

		if (il < 2) il = 2;
		long b = (long)il;
		long long re = 0L;
		long long pot = 1L;
		for (i=s.size()-1; i>=0; i--)
		{
			re += pot * vn[i];
			pot *= b;
		}

		printf("Case #%d: %lld\n", k+1, re);
		//for (i=0; i<H; i++) printf("%c", 'a'+comp[i][0]);

	}

	scanf("%c", &c);
	return 0;
}
