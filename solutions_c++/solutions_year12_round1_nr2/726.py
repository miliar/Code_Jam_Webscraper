//#include <iostream>
//#include <fstream>
#include <stdio.h>

//using namespace std;

void qsort(int *a , int *b, int lo , int hi)
{
	int t;
	int l,h;
	l = lo; h = hi;
	int x;
	x = a[ (l+h)/2 ];
	do{
		while (a[l]<x) l++;
		while (a[h]>x) h--;
		if (l<=h)
		{
			t = a[l]; a[l] = a[h]; a[h] = t;
			t = b[l]; b[l] = b[h]; b[h] = t;
			l++; h--;
		}
	}while (l<=h);
	if (l<hi) {qsort(a , b, l,hi);};
	if (h>lo) {qsort(a , b, lo,h);};
}

int a[1100], b[1100], och[1100];
bool p[1100], pa[1100];

int main()
{
	//ifstream in("input.txt");
	//ofstream out("output.txt");

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testnum = 0;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		int n, sum = 0;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			scanf("%d%d", &a[i], &b[i]);
		sum = 2*n;


		bool found = true;
		int now = 0, res = 0;
		for (int i = 1; i <= n; i++)
		{
			p[i] = true;
			pa[i] = true;
		}

		while (found && now < sum)
		{
			int min = 20000000, indMin = 0;
			for (int i = 1; i <= n; i++)
				if (b[i] < min && b[i] <= now && p[i])
				{
					min = och[i]; indMin = i;
				}

			if (indMin != 0)
			{
				res++;
				
				if (pa[indMin])
					now += 2;
				else
					now++;

				p[indMin] = false;
				pa[indMin] = false;
			}
			else
			{
				int ind = 0, mina = 100000000, maxb = -10;
				for (int i = 1; i <= n; i++)
					if (a[i] <= now && pa[i])
					{
						if (b[i] > maxb)
						{
							maxb = b[i];
							ind = i;
						}
						else
						if (b[i] == maxb && a[i] < mina)
						{
							mina = a[i];
							ind = i;
						}
					}

				if (ind == 0)
					found = false;
				else
				{
					pa[ind] = false;
					res++;
					now++;
				}
			}	
		}


		if (found)
			printf("Case #%d: %d\n", testcase, res);
		else
			printf("Case #%d: Too Bad\n", testcase);
	}

	return 0;
}
