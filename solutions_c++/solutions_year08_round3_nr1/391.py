#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

const int L=1000;
const int K=1000;
int n;
int letters[L+1];
int used[K+1];
int k, p, l;

int degrade(const void *e1, const void *e2)
{
	return *((int *)e2) - *((int *)e1);
}

int main()
{
	int tt;
	long long ans;
	int i, j;
	cin >> n;
	tt=1;
	while(tt<=n)
	{
		cin >> p >> k >> l;
		memset(letters, 0, sizeof(letters));
		memset(used, 0, sizeof(used));
		for(i=0; i<l; i++)
			cin >> letters[i];
		qsort(letters, l, sizeof(int), degrade);
		for(i=0; i<k; i++)
		{
			used[i] = 0;
		}
		j=0;
		ans=0;
		for(i=0; i<l; i++)
		{
			while(used[j]+1>p) j = (j+1)%k;
			used[j]++;
			ans += (long long)used[j]*(long long)letters[i];	
			j = (j+1)%k;
		}
		
		printf("Case #%d: %I64d\n", tt, ans);
		//cout << "Case #" << tt <<": " << ans << endl;
		tt++;
	}
	return 0;
}