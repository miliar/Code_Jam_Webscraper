
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

int T, P;
int Ps[10001];
vector<int> q;
int taken[100];
int nq;
int curRes;
int curMin;
int ntaken;

bool nextPerm(vector<int>& q, int l)
{
	if (l==1)
	{
		int min = 0;
		for (int i = 1; i < q.size(); i++)
			if (q[i] < q[min] && q[i] > q[0])
				min = i;
		if (q[min]<=q[0])
			return false;
		swap(q[0], q[min]);
		sort(q.begin()+1,q.end());
		return true;
	}
	if (q[l-1] > q[l-2])
	{
		int min = l-1;
		for (int i = l; i < q.size(); i++)
			if (q[i] < q[min] && q[i] > q[l-2])
				min = i;
		swap(q[l-2], q[min]);
		sort(q.begin()+(l-1), q.end());
		return true;
	}
	return nextPerm(q, l - 1);
}

void calc(vector<int>& lst)
{
	for (int i=0;i<lst.size();i++)
	{
		int min, max;
		for (min=lst[i]; min>=0; min--)
			if (Ps[min]==1)
				break;
		if (min==-1 || Ps[min]==1)
			min++;
		for (max=lst[i]+1; max<P; max++)
			if (Ps[max]==1)
				break;
		Ps[lst[i]]=1;
		curRes += max-min-1;
	}
}

void test()
{
//	solve();
}

int main()
{
	test();
	ifstream f("C-small-attempt1.in");
	ofstream of("output.out");

	f >> T;
	for (int i = 0; i < T; i++)
	{
		int Q;
		f >> P >> Q;
		q.clear();
		for (int j = 0; j < Q; j++)
		{
			q.push_back(0);
			f >> q[j];
			q[j]--;
		}
		curRes=0;
		ntaken=0;
		curMin=2000000000;
		memset(Ps,0, sizeof(Ps));
		memset(taken, 0, sizeof(taken));
		sort(q.begin(), q.end());
		int ctr=0;
		do 
		{
			curRes = 0;
			calc(q);
			if (curRes < curMin)
				curMin = curRes;
			memset(Ps, 0 , P*sizeof(int));
			ctr++;
		}
		while (nextPerm(q, q.size()));
		printf("ctr: %d\n", ctr);
		of << "Case #" << i+1 << ": " << curMin << endl;
	}
}
