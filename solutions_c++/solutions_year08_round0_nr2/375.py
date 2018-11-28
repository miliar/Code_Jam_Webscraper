#include <stdio.h>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

struct triple
{
	int a, b, c;
	triple(int A, int B, int C) { a=A; b=B; c=C; }
	bool operator <(const triple &t)
	{
		if (a != t.a)
			return a < t.a;
		return b < t.b;
	}
};

void go()
{
	int t, na, nb;
	scanf("%d%d%d", &t, &na, &nb);
	vector<triple> z;
	for (int i = 0; i < na + nb; ++i){
		int h1, h2, m1, m2;
		scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
		z.push_back(triple(h1 * 60 + m1, h2 * 60 + m2 + t, i >= na));
	}
	sort(z.begin(), z.end());
	int ret[2];
	ret[0] = ret[1] = 0;
	while (z.size())
	{
		++ret[z[0].c];
		triple h = z[0];
		z.erase(z.begin());
		for (int i = 0; i < z.size(); ) 
			if(z[i].c + h.c == 1 && z[i].a >= h.b) {
				h = z[i];
				z.erase(z.begin() + i);
			}
			else
				++i;
	}
	printf("%d %d", ret[0], ret[1]);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf ("%d", &n);
	for (int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		go();
		printf("\n");
	}
}