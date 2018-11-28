#include <algorithm>
#include <cstdlib>
#include <cstdio>

struct Googler
{
	int bPoint_notSurp;
	int bPoint_surp;
};

const int MAX_GOOGLERS = 100;
Googler v[MAX_GOOGLERS];
int v_size;

/*
inline bool operator<(const Googler& x, const Googler& y)
{
	return (x.bPoint_notSurp > y.bPoint_notSurp || (x.bPoint_notSurp == y.bPoint_notSurp && x.bPoint_surp > y.bPoint_surp));
}
*/


int solve(FILE* in) 
{
	int TS, surp, th;
	fscanf(in, "%d%d%d", &v_size, &surp, &th);
	for (int i = 0; i < v_size; i++)
	{
		int rho, mu;
		fscanf(in, "%d", &TS);
		rho = TS / 3; 
		mu = TS % 3;
		// Unico caso particolare, per TS=1 o 2, vale ramo generale
		if (TS == 0) {
			v[i].bPoint_notSurp = 0;
			v[i].bPoint_surp = 0;
		}
		else {
			if (mu == 0) {
				v[i].bPoint_notSurp = rho;
				v[i].bPoint_surp = rho + 1;
			}
			else if (mu == 1) {
				v[i].bPoint_notSurp = rho + 1;
				v[i].bPoint_surp = rho + 1;
			}
			else if (mu == 2) {
				v[i].bPoint_notSurp = rho + 1;
				v[i].bPoint_surp = rho + 2;
			}
		}
	}
	
//	std::sort(v, v+v_size);
	int count = 0;
	for (int i = 0; i < v_size; i++)
	{
//		printf("%d, %d\n", v[i].bPoint_notSurp, v[i].bPoint_surp);
		if (v[i].bPoint_notSurp >= th) 
			count++;
		else if (surp > 0 && v[i].bPoint_surp >= th)
		{
			count++;
			surp--;
		}
	}
	return count;
}

int main() 
{
	int cases;
	
	scanf("%d", &cases);
	for (int c = 1; c <= cases; c++)
	{
		int r = solve(stdin);
		printf("Case #%d: %d\n", c, r);
	}
	return 0;
}

