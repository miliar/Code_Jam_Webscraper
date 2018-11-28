#include <stdio.h>
#include <string.h>

const int N = 100;
const int A = 26;

class Magicka
{
	public:
		int mapC[A][A*A];
		int mapD[A][A];
		int count[A];
		int now;
		char stack[N];
		void clear()
		{
			for (int i=0;i<A;i++)
				for (int j=0;j<A*A;j++)
					mapC[i][j] = 0;
			for (int i=0;i<A;i++)
				for (int j=0;j<A;j++)
					mapD[i][j] = 0;
			for (int i=0;i<A;i++)
				count[i] = 0;
			now = 0;
		}
		void addC(char *c)
		{
			mapC[c[2]-'A'][(c[0]-'A')*A+(c[1]-'A')] = 1;
			mapC[c[2]-'A'][(c[1]-'A')*A+(c[0]-'A')] = 1;
		}
		void addD(char *d)
		{
			mapD[d[0]-'A'][d[1]-'A'] = 1;
			mapD[d[1]-'A'][d[0]-'A'] = 1;
		}
		void put(char p)
		{
			int v;
			stack[now++] = p;
			count[p-'A']++;
			if (now>=2)
			{
				v = (stack[now-2]-'A')*A+(stack[now-1]-'A');
				for (int j=0;j<A;j++)
					if (mapC[j][v])
					{
						count[stack[--now]-'A']--;
						count[stack[--now]-'A']--;
						stack[now++] = j+'A';
						count[j]++;
						return;
					}
				for (int j=0;j<A;j++)
					if (count[j] && mapD[p-'A'][j])
					{
						now = 0;
						for (int i=0;i<A;i++)
							count[i] = 0;
						return;
					}
			}
		}
		void put(char *p)
		{
			int l = strlen(p);
			for (int i=0;i<l;i++)
				put(p[i]);
		}
		void print()
		{
			printf("[");
			for (int i=0;i<now;i++)
				printf("%s%c", i?", ":"", stack[i]);
			printf("]");
		}
};

int main()
{
	int t, c, d, n;
	char get[N+1];
	Magicka magicka;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		magicka.clear();
		scanf("%d", &c);
		for (int j=0;j<c;j++)
		{
			scanf("%s", &get[0]);
			magicka.addC(get);
		}
		scanf("%d", &d);
		for (int j=0;j<d;j++)
		{
			scanf("%s", &get[0]);
			magicka.addD(get);
		}
		scanf("%d%s", &n, &get[0]);
		magicka.put(get);
		printf("Case #%d: ", i);
		magicka.print();
		printf("\n");
	}
	return 0;
}
