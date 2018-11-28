#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

const int maxN = 1000;

struct Wire
{
	int x,y, start;
};

int N;
Wire w[maxN];

inline bool compX(const Wire& left, const Wire& right)
{
	return left.x <= right.x;
}

int inversions()
{
	sort(&w[0], &w[N], compX);

	/*
	for (int i = 0; i<N; ++i)
	{
		cout << w[i].x << " "<< w[i].y << " " << w[i].start << " "<<endl;
	}
	*/

	int inversions = 0;

	for (int i = 1; i < N; ++i)
	{
		int j = i;
		while (w[j].y < w[j-1].y && j>0)
		{
			swap(w[j-1], w[j]);
			--j;
			++inversions;
		}
	}

	return inversions;
}


int main(void)
{
	int T;

	cin >> T;
	for (int case_nr = 1; case_nr <= T; case_nr++)
	{
		cin >> N;

		for (int i = 0; i < N; ++i)
		{
			cin >> w[i].x >> w[i].y;
			w[i].start = i;
		}

		int I = inversions();

		cout << "Case #" << case_nr << ": " << I << endl;

	}

	return 0;
}

