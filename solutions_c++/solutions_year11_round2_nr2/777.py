#include <iostream>
#include <stdio.h>
#include <fstream>
#include <algorithm>
using namespace std;

struct node{
	int a;
	int b;
};

bool cmp(node a, node b)
{
	return a.a < b.a;
}

int main()
{
	FILE* in = fopen("in.txt", "r");
	FILE* out = fopen("out.txt", "w+");

	int t;
	node data[205];
	//int dist[205];
	
	fscanf(in, "%d", &t);
	for (int cas = 1; cas <= t; cas++)
	{
		int n, k, num = 0;
		int max = INT_MIN;
		int min = INT_MAX;
		fscanf(in, "%d %d", &n, &k);
		for (int i = 0; i < n; i++)
		{
			fscanf(in, "%d %d", &data[i].a, &data[i].b);
			num += data[i].b;
		}
		//sort(data, data+n, cmp);
		int cnt = 0;
		int point = data[0].a;
		double ans = 0;
		double tem;
		for (int i = 0; i < n; i++)
		{
			if (data[i].a > point + cnt*k)
			{
				tem = ((double)max - min) / 2;
				ans = ans < tem ? tem : ans;
				cnt = 0;
				point = data[i].a;
				max = INT_MIN;
				min = INT_MAX;
			}
			for (int j = 0; j < data[i].b; j++)
			{	
				int sum = data[i].a - k*cnt;
				cnt++;
				max = max < sum ? sum : max;
				min = min > sum ? sum : min;
			}
		}
		tem = ((double)max - min) / 2;
		ans = ans < tem ? tem : ans;

		fprintf(out, "Case #%d: %.6lf\n", cas, ans);
		//fprintf(out, "%.6f\n", (0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]));
	}
	
	fclose(in);
	fclose(out);

	printf("sefse\n");
	return 0;
}