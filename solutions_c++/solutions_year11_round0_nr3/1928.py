#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

struct node
{
	char a, b, c;
};

int main()
{
	FILE* in = fopen("in3", "r");
	FILE* out = fopen("out.txt","w+");

	int n, m;

	fscanf(in, "%d", &n);
	
	for (int cas = 1; cas <= n; cas++)
	{
		fscanf(in, "%d", &m);
		int min = INT_MAX, tem, ans=0, sum = 0;
		for (int i = 0; i < m; i++)
		{
			fscanf(in, "%d", &tem);
			ans ^= tem;
			sum += tem;
			min = min > tem ? tem : min;
		}
		fprintf(out, "Case #%d: ", cas);
		if (ans == 0)
		{
			fprintf(out, "%d\n", sum - min);
		}
		else
			fprintf(out, "NO\n");
	}

	fclose(out);
	fclose(in);

	system("pause");

	return 0;
}