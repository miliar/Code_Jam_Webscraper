/*
ID: brook.t1
PROG: dancing
LANG: C++
*/

#define FOR(st, lim, inc) for(int i = st; i < lim; i += inc)
#define forzo(lim) for(int i = 0; i < lim; i++)
#define forzos(lim) for(int j = 0; j < lim; j++)
#define couter(x) cout << #x << "= " << x << endl
#define couterl(x) cout << #x << "= " << x
#define coutarr(x, n) cout << #x << ": \n";\
			forzo(n) cout << x[i] << " ";\
			cout << "\n";
#define coutarrv(x, n) forzo(n) couterl(x[i]) << " ";\
			cout << "\n";

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;

int minposs(int gl, bool b) // true means unsurprising
{
	int r;
	if(b)
	{
		r = 3*gl - 2;
	} else {
		r = 3*gl - 4;
	}
	if(r > 0)
	{
		return r;
	} else {
		return 0;
	}
}

int main()
{
	FILE * input = fopen("dancing.in", "r");
	FILE * output = fopen("dancing.out", "w");

	int t, n, s, p, cn=0;
	fscanf(input, "%d", &t);
forzos(t)
{
	fscanf(input, "%d", &n);
	fscanf(input, "%d", &s);
	fscanf(input, "%d", &p);
	int surp = minposs(p, 0);
	int norm = minposs(p, 1);
	cn = 0;

	vector<int> googs(n);
	forzo(n)
		fscanf(input, "%d", &googs[i]);

	vector<bool> unsur(n);
	forzo(n)
	{
		bool b = googs[i] >= norm;
		if(b) cn++;
		unsur[i] = b;
	}
	int iter = 0;
	while(s > 0 && iter < n)
	{
		if(!unsur[iter])
		{
			bool snext = googs[iter] >= surp;
			if(snext && googs[iter] > 0)
			{
				s--;
				cn++;
			}
		}
		iter++;
	}
	fprintf(output, "Case #%d: %d\n", j+1, cn);
}

	fclose(input);
	fclose(output);
	return 0;
}
