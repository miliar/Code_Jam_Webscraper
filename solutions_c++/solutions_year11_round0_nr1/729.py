#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

FILE *f1, *f2;

const int MAX = 300;
int seq[MAX][2], seqrob[2][MAX];
int n, cas, ans;

int myabs(int a)
{
	return a>0?a:-a;
}
int main()
{
	f1 = fopen("input.in", "r");
	f2 = fopen("out.in", "w");

	fscanf(f1, "%d", &cas);
	for(int c = 1; c <= cas; c ++)
	{
		fscanf(f1, "%d", &n);
		int num[2] = {0, 0};
		for(int i = 0; i < n; i ++)
		{
			char rob;
			fscanf(f1, " %c%d", &rob, &seq[i][1]);
			seq[i][0] = rob == 'O';
			if(rob == 'B') seqrob[0][num[0]++] = seq[i][1];
			else seqrob[1][num[1]++] = seq[i][1];
		}
		ans = 0;
		int curp[2] = {1, 1},pt[2] = {0, 0};
		for(int i = 0; i < n; i ++)
		{
			int rob = seq[i][0];
			int cost = myabs(curp[rob]-seq[i][1]) + 1;
			pt[rob] ++;
			curp[rob] = seq[i][1];
			if(pt[1-rob] < num[1-rob])
			{
				int des = seqrob[1-rob][pt[1-rob]];
				if(curp[1-rob] > des)
					if(curp[1-rob]-des >= cost)
						curp[1-rob] = curp[1-rob] - cost;
					else
						curp[1-rob] = des;
				else if(curp[1-rob] < des)
					if(des-curp[1-rob] >= cost)
						curp[1-rob] = curp[1-rob] + cost;
					else
						curp[1-rob] = des;
			}
			ans += cost;
		}
		fprintf(f2, "Case #%d: %d\n", c, ans);
	}
	fclose(f1);
	fclose(f2);

	return 0;
}