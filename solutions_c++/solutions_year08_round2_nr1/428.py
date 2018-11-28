#include <fstream>
#include <iostream>
using namespace std;

struct point
{
	int x, y, dx, dy;
};

point P[100000];

int compare(const void * i, const void * j)
{
	//point ** i = &I, * j = J;
	if(((point *)i)->x != ((point *)j)->x) return ((point *)i)->x - ((point *)j)->x;
	else
		if((((point *)i)->y != ((point *)j)->y)) return ((point *)i)->y - ((point *)j)->y;
		else
			if((((point *)i)->dx != ((point *)j)->dx)) return ((point *)i)->dx - ((point *)j)->dx;
			else
				return ((point *)i)->dy - ((point *)j)->dy;
}

bool eq(int i, int j)
{
	if(i < 0) return 0;
	if((P[i].x == P[j].x) && (P[i].y == P[j].y) && (P[i].dx == P[j].dx) && (P[i].dy == P[j].dy)) return 1;
	else return 0;
}

int main()
{
	ifstream f("A.in");
	ofstream ff("A.out");

	int T, iT;

	f >> T;
	for(iT = 1; iT <= T; ++iT)
	{
		int nP, A, B, C, D, M, i;
		long long x, y;
		f >> nP >> A >> B >> C >> D >> x >> y >> M;
		for(i = 0; i < nP; ++i)
		{
			P[i].x = x % 3;
			P[i].y = y % 3;
			P[i].dx = x / 3;
			P[i].dy = y / 3;
			x = (x * A + B) % M;
			y = (y * C + D) % M;
		}

		qsort(P, nP, sizeof(point), compare);
		long long n11 = 0, n12 = 0, n13 = 0, n21 = 0, n22 = 0, n23 = 0, n31 = 0, n32 = 0, n33 = 0;
		for(i = 0; (i < nP) && (!P[i].x) && (!P[i].y); ++i) if(!eq(i - 1, i)) ++n11;
		for(; (i < nP) && (!P[i].x) && (P[i].y == 1); ++i) if(!eq(i - 1, i)) ++n12;
		for(; (i < nP) && (!P[i].x) && (P[i].y == 2); ++i) if(!eq(i - 1, i)) ++n13;
		for(; (i < nP) && (P[i].x == 1) && (!P[i].y); ++i) if(!eq(i - 1, i)) ++n21;
		for(; (i < nP) && (P[i].x == 1) && (P[i].y == 1); ++i) if(!eq(i - 1, i)) ++n22;
		for(; (i < nP) && (P[i].x == 1) && (P[i].y == 2); ++i) if(!eq(i - 1, i)) ++n23;
		for(; (i < nP) && (P[i].x == 2) && (!P[i].y); ++i) if(!eq(i - 1, i)) ++n31;
		for(; (i < nP) && (P[i].x == 2) && (P[i].y == 1); ++i) if(!eq(i - 1, i)) ++n32;
		for(; (i < nP) && (P[i].x == 2) && (P[i].y == 2); ++i) if(!eq(i - 1, i)) ++n33;

		long long n = 0;
		if(n11 >= 3) n += n11 * (n11 - 1) * (n11 - 2) / 6;
		if(n12 >= 3) n += n12 * (n12 - 1) * (n12 - 2) / 6;
		if(n13 >= 3) n += n13 * (n13 - 1) * (n13 - 2) / 6;
		if(n21 >= 3) n += n21 * (n21 - 1) * (n21 - 2) / 6;
		if(n22 >= 3) n += n22 * (n22 - 1) * (n22 - 2) / 6;
		if(n23 >= 3) n += n23 * (n23 - 1) * (n23 - 2) / 6;
		if(n31 >= 3) n += n31 * (n31 - 1) * (n31 - 2) / 6;
		if(n32 >= 3) n += n32 * (n32 - 1) * (n32 - 2) / 6;
		if(n33 >= 3) n += n33 * (n33 - 1) * (n33 - 2) / 6;
		n += n11 * n12 * n13;
		n += n21 * n22 * n23;
		n += n31 * n32 * n33;
		n += n11 * n21 * n31;
		n += n12 * n22 * n32;
		n += n13 * n23 * n33;
		n += n11 * n22 * n33;
		n += n11 * n23 * n32;
		n += n12 * n21 * n33;
		n += n12 * n23 * n31;
		n += n13 * n21 * n32;
		n += n13 * n22 * n31;

		ff << "Case #" << iT << ": " << n << endl;
	}

	f.close();
	ff.close();
	return 0;
}