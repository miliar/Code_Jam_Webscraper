
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int T;
char N[30];
long long R;
char nS[25];

int min(char *s, int l, int n)
{
	int r=-1;
	for (int i=0;i<l;i++)
		if ((r==-1) || (s[r]>s[i] && s[i] > n))
			r = i;
	return r;
}
int makeSmallest(char *s, int l, int k, int minD)
{
	if (l == 1)
	{
		string ss(s);
		int m = min(s, k, '0');
		if (ss[m]!='0')
			swap(ss[0], ss[m]);
		ss.insert(1, "0");
		strcpy(s, ss.c_str());
		sort(s+2, s+k+1);
		return 1;
	}
	if (s[l-1] > s[l-2])
	{
		int m = min(s+(l-2)+1, k-(l-2)-1, s[l-2]);
		swap(s[l-2], s[l-2+1+m]);
		sort(s + (l-1), s + k);
		return 1;
	}
	return makeSmallest(s, l-1, k, minD);
}

void solve()
{
	strcpy(nS, N);
	int l = strlen(nS);
	makeSmallest(nS, l, l, l-1);
}

void test()
{
//	N=1051;
	solve();
}

int main()
{
//	test();
	ifstream f("B-large.in");
	ofstream of("output.out");

	f >> T;
	for (int i = 0; i < T; i++)
	{
		f >> N;
		solve();
		of << "Case #" << i+1 << ": " << nS << endl;
	}
}

	/*	else
		{
			int i = -1;
			int j;
			for (j=0;j<ss.length();j++)
				if (((i==-1) || (ss[i]>ss[j])) && ss[j]!='0')
					i=j;
			int d=0;
			swap(ss[0], ss[i]);
		}*/