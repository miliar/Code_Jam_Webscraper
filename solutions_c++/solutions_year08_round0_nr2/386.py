#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <stdio.h>


using namespace std;

const int MYMAX = 25 * 60;
struct Comp 
{
	bool operator()(int a, int b)
	{
		return a > b;
	}
};

int conv(int h, int m)
{
	return h * 60 + m;
}

int getAns(vector<int> v1, vector<int> v2)
{
	int S1 = v1.size();

	v2.push_back(MYMAX);
	int S2 = v2.size();

	int p1 = 0;
	int p2 = 0;

	int ret = 0;

	while (p1 < S1)
	{
		if (v1[p1] >= v2[p2])
			p2++;
		else
			ret++;

		p1++;
	}

	return ret;
}

void printa(vector<int> v)
{
	vector<int>::iterator it = v.begin();

	while (it != v.end())
	{
		cout << *it << "   ";
		++it;
	}
	cout << endl;


}
int main()
{

	int N;
	scanf("%d\n", &N);

	for (int i = 1; i <= N; ++i)
	{
		vector<int> va1, va2, vb1, vb2;

		int T;
		scanf("%d\n", &T);

		int NA, NB;

		scanf("%d %d", &NA, &NB);

		for (int j = 1; j <= NA; ++j)
		{
			int h, m;
			int start, end;

			scanf("%d:%d", &h, &m);
			start = conv(h, m);

			scanf("%d:%d", &h, &m);
			end = conv(h, m);

			va1.push_back(start);
			va2.push_back(end + T);

		}

		for (int j = 1; j <= NB; ++j)
		{
			int h, m;
			int start, end;

			scanf("%d:%d", &h, &m);
			start = conv(h, m);

			scanf("%d:%d", &h, &m);
			end = conv(h, m);

			vb1.push_back(start);
			vb2.push_back(end + T);
		}

		sort(va1.begin(), va1.end());
		sort(va2.begin(), va2.end());
		sort(vb1.begin(), vb1.end());
		sort(vb2.begin(), vb2.end());




		int aa = getAns(va1, vb2);


		int bb = getAns(vb1, va2);

		printf("Case #%d: %d %d\n", i, aa, bb);

	}


	return 0;
}


