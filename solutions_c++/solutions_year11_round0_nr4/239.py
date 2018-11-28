#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int T;
int N;
vector<int> p;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		cin >> N;
		int pos;
		p.clear();
		for (int j=0; j<N; j++)
		{
			cin >> pos;
			p.push_back(pos);
		}
		double ret = 0;
		for (int j=0; j<N; j++)
			if (p[j] != j+1)
				ret++;
		printf("Case #%d: %0.6lf\n", i, ret);
	}
}