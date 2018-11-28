#include <cstdio>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int K;
int N;

int p[20];
char buf[51000];
char rbuf[51000];

void comp()
{
	int blocks = N/K;
	for (int b=0; b<blocks; b++)
	{
		int bSt = b*K;
		for (int i=0; i<K; i++)
		{
			rbuf[bSt+i] = buf[bSt+p[i]];
		}
	}
}
int calcSize()
{
	int res = 0;
	char last = 0;
	for (int i=0; i<N; i++)
	{
		if (rbuf[i] != last)
		{
			res++;
			last = rbuf[i];
		}
	}
	return res;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		cerr<<tt<<endl;
		scanf("%d", &K);
		scanf("%s", buf);
		N = strlen(buf);
		for (int i=0; i<20; i++)
			p[i] = i;
		int res =  N+1;
		while (true)
		{
			comp();
			int locres = calcSize();
			if (locres < res)
				res = locres;
			if (next_permutation(p,p+K) == false)
				break;
		}
		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}