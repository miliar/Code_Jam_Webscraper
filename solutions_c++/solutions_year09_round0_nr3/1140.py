#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
using namespace std;

int main()
{
	FILE *fin = fopen("D:\\c.in", "r");
	FILE *fout = fopen("D:\\c.txt", "w");

	int N;
	char str[1000];
	string standard = "welcome to code jam";

	fscanf(fin, "%d\n", &N);
	for (int cs = 1; cs <= N; cs++)
	{
		vector<vector<int> > que;
		vector<int> ins;

		ins.clear();
		que.clear();
		string bf;
		bf.clear();
		for (int i = 0; i < standard.size(); i++)
			ins.push_back(0);

		fgets(str, 1000, fin);
		for (int i = 0; str[i] != '\0'; i++)
		{
			bf += str[i];
			que.push_back(ins);
		}
		
		for (int i = 0; i < bf.size(); i++)
			if (bf[i] == 'm')
			{
				que[i][standard.size()-1] = 1;
			}

		for (int i = standard.size()-2; i >= 0; i--)
		{
			for (int j = bf.size()-1; j >=0; j--)
			{
				int total = 0;
				if (bf[j] == standard[i])
				{
					for (int k = j + 1; k < bf.size(); k++)
						total = (total + que[k][i+1])%10000;
				}
				que[j][i] = total%10000;
			}
		}

		int ans = 0;
		for (int i = 0; i < bf.size(); i++)
			ans = (ans + que[i][0])%10000;
		if (ans >= 1000)
			fprintf(fout, "Case #%d: %d\n", cs, ans);
		else
			if (ans >= 100)
				fprintf(fout, "Case #%d: 0%d\n", cs, ans);
			else
				if (ans >= 10)
					fprintf(fout, "Case #%d: 00%d\n", cs, ans);
				else
					fprintf(fout, "Case #%d: 000%d\n", cs, ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
	
