#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

double p[101000];
double mul[101000];

int main()
{
	//ifstream in("input.txt");
	//ofstream out("output.txt");

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testnum = 0;
	scanf("%d", &testnum);
	//in >> testnum;
	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		//in >> a >> b;
		for (int i = 1; i <= a; i++)
			scanf("%lf", &p[i]);
			//in >> p[i]; 

		mul[1] = p[1];
		for (int i = 2; i <= a; i++)
			mul[i] = mul[i-1]*p[i];


		double res = b + 2;
		for (int x = 0; x <= a; x ++)
		{
			double pr = 1;
			pr = mul[a-x];

			if ( (b-a+1 + x*2)*pr + (b-a+1 + x*2 + b + 1)*(1-pr) < res)
				res = (b-a+1 + x*2)*pr + (b-a+1 + x*2 + b + 1)*(1-pr);
		}

		//out << "Case #" << testcase << ": " << res << endl;
		printf("Case #%d: %.8lf\n", testcase, res);
	}

	return 0;
}
