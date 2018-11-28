#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

const int MAXN = 30;

int trans[MAXN][MAXN];
bool conf[MAXN][MAXN];

vector <int> sv;

int Push_back(int x)
{
	if (sv.size() > 0 && trans[sv[sv.size()-1]][x] >= 0)
	{
		x = trans[sv[sv.size()-1]][x];
		sv.pop_back();   
		return Push_back(x);
	}
	for (int i = 0; i < sv.size(); i ++)
		if (conf[sv[i]][x])
		{
			sv.clear();
			return 0;
		}
	sv.push_back(x);
	return 0;
}

int work(int nCase)
{
	char sb[5];
	memset(trans, 0xff, sizeof(trans));
	memset(conf, false, sizeof(conf));
	sv.clear();

	int c, x, y, z;   char ch;
	scanf("%d", &c);
	for (int i = 0; i < c; i ++)
	{
		scanf("%s", sb);
		x = sb[0] - 65;   y = sb[1] - 65;  z = sb[2] - 65;
		trans[x][y] = trans[y][x] = z;
	}
	scanf("%d", &c);
	for (int i = 0; i < c; i ++)
	{
		scanf("%s", sb);
		x = sb[0] - 65;   y = sb[1] - 65;
		conf[x][y] = conf[y][x] = true;
	}

	scanf("%d%c", &c, &ch);
	for (int i = 0; i < c; i ++)
	{
		scanf("%c", &ch);
		x = ch - 65;
		Push_back(x);
	}
	scanf("\n");

	printf("Case #%d: [", nCase);
	if (sv.size() > 0)  printf("%c", (char)(sv[0] + 65));
	for (int i = 1; i < sv.size(); i ++)
		printf(", %c", (char)(sv[i] + 65));
	printf("]\n");
	return 0;
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k ++)
		work(k);
//	fclose(stdin);
//	fclose(stdout);
	return 0;
}