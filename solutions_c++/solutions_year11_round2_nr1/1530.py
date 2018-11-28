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
		int N;
		scanf("%d", &N);

		int k = 0;

		printf("Case #%d:\n", t + 1);

		vector< vector< pair<int, int> > > op(N);

		for(int i = 0; i < N; i++)
		{
			char buffer[200];
			scanf("%s", buffer);
			for(int j = 0; j < N; j++)
			{
				if(buffer[j] == '.')
				{
					continue;
				}

				op[i].push_back(pair<int, int>(j, buffer[j] == '1'));
			}
		}
		
		vector<double> wp(N), owp(N), oowp(N);

		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < op[i].size(); j++)
			{
				wp[i] += op[i][j].second;
			}

			wp[i] /= op[i].size();
		}

		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < op[i].size(); j++)
			{
				owp[i] += (wp[op[i][j].first] * op[op[i][j].first].size() - (op[i][j].second == 0)) / (op[op[i][j].first].size() - 1);
			}

			owp[i] /= op[i].size();
		}

		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < op[i].size(); j++)
			{
				oowp[i] += owp[op[i][j].first];
			}

			oowp[i] /= op[i].size();
		}

		for(int i = 0; i < N; i++)
		{
			printf("%0.12f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}

	}

	fclose(stdin);
	fclose(stdout);
}