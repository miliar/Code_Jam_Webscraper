#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <stack>

using namespace std;

int main(int argc, char **argv)
{
	int T;
	freopen("A-large.in", "rb", stdin);
	freopen("A-large.out", "wb", stdout);

	scanf("%d", &T);
	for(int t = 0; t < T; t++)
	{
		printf("Case #%d:\n", t + 1);

		int R, C;
		vector< string > picture;
		scanf("%d %d", &R, &C);
		picture.assign(R, string(C, ' '));

		for(int i = 0; i < R; i++)
		{
			scanf("%s", picture[i].c_str());
		}

		bool ok = true;

		for(int i = 0; ok && i < R - 1; i++)
		{
			for(int j = 0; ok && j < C - 1; j++)
			{
				if(picture[i][j] == '#')
				{
					if(picture[i + 1][j] == '#' &&
						picture[i][j + 1] == '#' &&
						picture[i + 1][j + 1] == '#')
					{
						picture[i][j] = '/';
						picture[i][j + 1] = '\\';
						picture[i + 1][j] = '\\';
						picture[i + 1][j + 1] = '/';
					}
					else
					{
						ok = false;
					}
				}
			}
		}

		for(int i = 0; i < R; i++)
		{
			ok = ok && picture[i][C - 1] != '#';
		}

		for(int j = 0; j < C; j++)
		{
			ok = ok && picture[R - 1][j] != '#';
		}

		if(!ok)
		{
			printf("Impossible\n");
		}
		else
		{
			for(int i = 0; i < R; i++)
			{
				printf("%s\n", picture[i].c_str());
			}
		}
	}

	fclose(stdin);
	fclose(stdout);
}