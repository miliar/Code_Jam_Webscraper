#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS

vector<long> fr;

int main() {
	freopen("1.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	fr.clear();

	int t;
	scanf("%d", &t);

	for(int i=0;i<t;i++)
	{
		long sum=0;
		int p, k, l;
		scanf("%d%d%d", &p, &k, &l);

		int x=1, count=k;

		if(p*k<l)
		{
			printf("Case #%d: Impossible\n", i+1);
			break;
		}
		else
		{
			fr.resize(l);
			for(int j=0;j<l;j++)
			{
				scanf("%ld", &fr[j]);
			}
			sort(fr.begin(), fr.end());

			for(int j2=l-1;j2>=0;j2--)
			{
				sum+=fr[j2]*x;
				count--;
				if(count==0)
				{
					x++;
					count=k;
				}
			}

			printf("Case #%d: %ld\n", i+1, sum);
		}
	}

	return 0;
}