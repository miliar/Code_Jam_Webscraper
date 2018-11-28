#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 1000
using namespace std;
#define min(a,b) (((a) < (b)) ? (a) : (b))
int n;
int candy[MAX+1];
__int64 result; // 

void readdata()
{	
	int i;
	scanf("%d", &n);
	for (i=0; i<n; ++i){
		scanf("%d", &candy[i]);
	}
		
}

void solve()
{
	__int64 sum=0;
	int tmp=0;
	int i;
	int m_min=0x7ffffff;
	for (i=0; i<n; ++i){
		if (candy[i] < m_min)
			m_min = candy[i];
		sum += candy[i];
		tmp ^= candy[i];
	}

	if (tmp != 0)
		result = 0;
	else
		result = sum - m_min;
}
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		readdata();
		solve();

		if (result)
			printf("Case #%d: %d\n",it,result);
		else
			printf("Case #%d: NO\n",it);
	
	}
	return 0;
}