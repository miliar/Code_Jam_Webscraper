#include <fstream>
#include <iostream>
using namespace std;

struct point
{
	int And, C;
};

point A[10000];

int mind(int a, int b)
{
	if(a < 0) return b;
	if(b < 0) return a;
	if(a <= b) return a;
	else return b;
}

int find(int i)
{
	switch(A[i].And)
	{
	case -1: 
		if(A[i].C) return 0;
		else return -1;

	case 0: return mind(find(2 * i + 1), find(2 * i + 2));

	case 1:
		int a = find(2 * i + 1);
		int b = find(2 * i + 2);
		int c = mind(a, b);
		if(!A[i].C)
			if((a < 0) || (b < 0)) return -1;
			else return a + b;
		if(c >= 0) ++c;
		if((a < 0) || (b < 0)) return c;
		else return mind(a + b, c);
	}
}

int main()
{
	ifstream f("A.in");
	ofstream ff("A.out");

	int T, iT;

	f >> T;
	for(iT = 1; iT <= T; ++iT)
	{
		bool V, b;
		int i, M;
		f >> M >> V;

		for(i = 0; i < (M - 1) / 2; ++i)
		{
			f >> b;
			if(V) A[i].And = b;
			else A[i].And = !b;
			f >> A[i].C;
		}
		for(; i < M; ++i)
		{
			A[i].And = -1;
			f >> b;
			if(V) A[i].C = b;
			else A[i].C = !b;
		}

		int a = find(0);

		ff << "Case #" << iT << ": ";
		if(a < 0) ff << "IMPOSSIBLE" << endl;
		else ff << a << endl;
	}

	f.close();
	ff.close();
	return 0;
}