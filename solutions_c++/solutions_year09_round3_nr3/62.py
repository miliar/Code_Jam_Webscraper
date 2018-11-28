#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <vector>
#define abs(x) ((x>=0)?(x):(-(x)))

using namespace std;
vector<int> list;

int buffer[10010][10010];

int bribe(int begin, int end)
{
	if (begin > end)
		return 0;
	if (buffer[begin][end] != -1)
		return buffer[begin][end];
	int cut = -1;
	int d = -1;
	int min = 100000;
	for (int i=0; i<list.size(); ++i) {
		if (!(list[i] < begin || list[i] > end)) {
			//if ((cut == -1)
			//    || abs(2*list[i] - begin - end) < d) {
				cut = list[i];
				//d = abs(2*list[i] - begin - end);
				int sum = 0;
				sum += cut - begin;
				sum += end - cut;
				sum += bribe(begin, cut-1);
				sum += bribe(cut+1, end);
				if (min > sum)
					min = sum;
			//}
		}
	}
	if (cut == -1)
		return 0;
	//printf("%d ", cut);

	buffer[begin][end] = min;
	return min;
}

int main()
{
	int N_;
	scanf("%d\n", &N_);
	for (int n_=1; n_<=N_; ++n_) {
		list.clear();
		memset(buffer, -1, sizeof(buffer));
		int P, Q;
		scanf("%d %d", &P, &Q);
		for (int i=0; i<Q; ++i) {
			int x;
			scanf("%d", &x);
			list.push_back(x);
		}
		int ans = bribe(1, P);
		printf("Case #%d: %d\n", n_, ans);
	}
	return 0;
}

