#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

int memo[10][1<<10];
bool done[10][1<<10];

int n;
vector <long long> V1, V2;

/*
int f(int a, int mask)
{
	if(a==n) return 0;

	if(done[a][mask]) return memo[a][mask];

	int minN = 1<<30;
	for(int i=0; i<n; i++)
	{
		if((mask&(1<<i))==0)
		{
			minN = min(minN, V1[a]*V2[i] + f(a+1, mask^(1<<i)));
		}
	}
	done[a][mask] = 1;
	memo[a][mask] = minN;
	return minN;
}
*/

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out2.txt", "w", stdout);

	int N;
	cin>>N;
	
	for(int caso=0; caso<N; caso++)
	{
		cin>>n;
		
		vector <long long> aux(n);
		V1 = aux;
		V2 = aux;
		
		for(int i=0; i<n; i++)
			cin>>V1[i];
		for(int i=0; i<n; i++)
			cin>>V2[i];
		
		sort(all(V1));
		sort(rall(V2));
		
		long long y = 0;
		for(int i=0; i<n; i++)
			y += V1[i]*V2[i];
		
		/*
		memset(done, 0, sizeof(done));
		*/

		//int x = f(0, 0);
		
		cout<<"Case #"<<caso+1<<": "<<y<<endl;
	}
	return 0;
}
