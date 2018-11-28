#include <stdio.h>
#include <string>

#define bmax 128
#define nmax 1024
#define inf 0x3f3f3f3f

using namespace std;

int T, S, Q, point, rez;
int a[nmax], dif, found, v[bmax], c[nmax];
char s[bmax][bmax], temp[bmax];

int main()
{
	freopen("a.in", "r", stdin);
	// freopen("a.out", "w", stdout);

	scanf("%d\n", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d\n", &S);
		for(int i = 1; i <= S; i++) 
			fgets(s[i], bmax, stdin);
		scanf("%d\n", &Q);
		memset(a, inf, sizeof(a));
		memset(v, 0, sizeof(v));
		a[0] = 0; point = 0; rez = 0; dif = 0;
		for(int i = 1; i <= Q; i++)
		{
			fgets(temp, bmax, stdin);
			found = 0;
			for(int j = 1; j <= S; j++) 
			{
				string s1 = temp; string s2 = s[j];
				if(s1 == s2) found = j;
			}
			c[i] = found;
			if(found)
			{
				v[found]++;
				if(v[found] == 1) dif++;
			}
			while(dif == S)
			{
				point++;
				if(point == i) 
				{
					rez = -1;
					break;
				}
				if(c[point] != 0)
				{
					v[c[point]]--;
					if(v[c[point]] == 0) dif--;
				}
			}
			a[i] = a[point] + 1;

			if(rez == -1) break;
		}

		if(Q == 0) a[Q] = 1;
		printf("Case #%d: %d\n", t, a[Q] - 1);
	}

	return 0;
}
