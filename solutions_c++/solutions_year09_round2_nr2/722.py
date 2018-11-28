#include <vector>
#include <queue>
#include <string>
#include <stdio.h>
#include <algorithm>

using namespace std;

void print(vector <int> v)
{
	int i;
	printf("v: ");
	for (i=0; i<v.size(); i++) printf("%d ", v[i]);
	printf("\n");
}

int main()
{
	int i,l,k,j;
	int T, n, s = 0;
	char c;

	scanf("%d", &T);
	scanf("%c", &c);
	for (k=0; k<T; k++)
	{
		vector <int> v;

		while (1)
		{
			if (scanf("%c", &c) == EOF) break;
			if (c>='0' && c<='9') v.push_back(c-'0');
			else break;
		}

		if (next_permutation(v.begin(), v.end()))
		{
			// ok, mamy rozwiazanie
		}
		else 
		{
			int zer = 1;
			for (i=0; i<v.size(); i++) if (v[i]==0) zer++; 
			for (i=v.size()-1; i>=0; i--) if (v[i]==0) v.erase(v.begin()+i);

			sort(v.begin(), v.end());
			
			for (i=0; i<zer; i++) v.insert(v.begin()+1, 0);
		}
		
		printf("Case #%d: ", k+1);
		for (i=0; i<v.size(); i++) printf("%d", v[i]);
		printf("\n");
	}

	scanf("%c", &c);
	return 0;
}



/*
int main()
{
	int i,l,k,j;
	int T, n, s;

	scanf("%d", &T);
	for (k=0; k<T; k++)
	{
		scanf("%d", &n);
		vector <int> v(12, 0);
		j = n;
		while (j)
		{
			v[j%10]++;
			j /= 10;
		}

		vector <int> vt(12, 0);
		s = n + 1;
		while (1)
		{
			j = s;
			for (i=0; i<=9; i++) vt[i] = 0;
			while (j)
			{
				vt[j%10]++;
				j /= 10;
			}

			bool ok = true;
			for (i=1; i<=9; i++) if (vt[i]!=v[i]) ok = false;
			if (ok) break;

			s++;
		}
		
		printf("Case #%d: %d\n", k+1, s);
	}

	char c;
	scanf("%c", &c);
	return 0;
}
*/