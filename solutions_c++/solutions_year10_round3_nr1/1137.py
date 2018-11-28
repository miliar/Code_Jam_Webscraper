#include <cstdio>

using namespace std;

struct line
{
	int y1;
	int y2;
};
typedef struct point point;
line lne[1000];

bool check(int a, int b)
{
	if(lne[a].y1 > lne[b].y1)
	{
		return lne[a].y2 < lne[b].y2;
	}
	else if(lne[a].y1 < lne[b].y1)
	{
		return lne[a].y2 > lne[b].y2;
	}
	else
		return false;
}
int main()
{
	int ans, n, ln, k;
	FILE* inf  = fopen("input.txt", "r");
	FILE* outf = fopen("output.txt","w");

	fscanf(inf, "%d", &n);
	for(int i = 0;i < n;i++)
	{
		ans = 0;
		fscanf(inf, "%d", &ln);
		for(int j=0;j<ln;j++)
		{
			fscanf(inf, "%d %d", &lne[j].y1, &lne[j].y2);
		}
		for(int j=0;j<ln;j++)
		{
			for(k=j+1;k<ln;k++)
			{
				if(check(j, k))
					ans++;
			}
		}
		fprintf(outf, "Case #%d: %d\n", i+1, ans);

	}
	return 0;
}