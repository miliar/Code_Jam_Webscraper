#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

ifstream fin("as.in");
ofstream fout("as.out");
typedef struct 
{
	int time;
	int button;
}status;


int gcd(int a, int b)
{
	int t;
	while(b != 0)
	{
		t = b;
		b = a % b;
		a = t;
	}
	return a;
}

int abs(int a)
{
	return a > 0 ? a : -a;
}

int main()
{
	int N, pd, pg, j, x, y, t1, t2, T, i, m;
	double d, g;
	bool flag = false;

	fin >> T;
	printf("%d", T);
	for(i = 1; i <= T; i ++)
	{
		fin >> N >> pd >> pg;
		if(pg == 0)
		{
			if(pd == 0)
			fout << "Case #" << i << ": Possible" <<  endl;
			else
			fout << "Case #" << i << ": Broken" <<  endl;
			continue;
		}
		m = gcd(pd, 100);
		m = 100 / m;

		if(N < m)
		{
			fout << "Case #" << i << ": Broken" <<  endl;
			continue;
		}
		

		for(j = 1; j <= N; j ++)
		{
			flag = false;
			t1 = 100 - pg;
			t2 = j * (pg - pd);

			if(t1 == 0 && t2 == 0)
				flag = true;

			if(t1 > 0 && t2 <= 0)
				flag = true;

			if(t1 > 0 && t2 > 0)
				flag = true;

			if(flag)
			{
				fout << "Case #" << i << ": Possible" <<  endl;
				break;
			}
		}

		if(!flag)
		{
			fout << "Case #" << i << ": Broken" <<  endl;
		}
	}
	return 0;
}
