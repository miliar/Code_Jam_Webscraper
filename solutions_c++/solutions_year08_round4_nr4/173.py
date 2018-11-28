#include <iostream>
#include <string>
using namespace std;

const int MAXK = 5;

int k;
string s;
int ans;
int perm[MAXK];
bool footmark[MAXK];

int calc()
{
	string ts(s);
	for(int i=0; i<s.size()/k; i++)
	{
		for(int j=0; j<k; j++)
			ts[i*k+j] = s[i*k+perm[j]];
	}
	int res = 0;
	for(int i=0; i<ts.size(); i++)
		if (!(i && ts[i] == ts[i-1]))
			res++;
	return res;
}

void search(int p)
{
	if (p >= k)
	{
		ans = min(ans, calc());
		return;
	}
	for(int i=0; i<k; i++)
		if (!footmark[i])
		{
			perm[p] = i;
			footmark[i] = true;
			search(p+1);
			footmark[i] = false;
		}
}

void work()
{
	cin >> k >> s;
	ans = s.size();
	memset(footmark, false, sizeof(footmark));
	search(0);
	cout << ans << endl;
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int nOfTest;
	cin >> nOfTest;
	for(int testCase=0; testCase<nOfTest; testCase++)
	{
		printf("Case #%d: ", testCase+1);
		work();
	}
}
