#include <algorithm> 
#include <cassert>
#include <cctype> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <iostream>
#include <map> 
#include <set> 
#include <string> 
#include <sstream>
#include <queue> 
#include <vector> 
using namespace std;

int T, N, res;
vector <int> A,B;

void solve()
{
	res=0;
	for (int i=0; i<A.size(); i++)
		for (int j=i+1; j<A.size(); j++)
			if (((A[i]>A[j])&&(B[i]<B[j]))||((A[j]>A[i])&&(B[j]<B[i]))) res++;
}

void write(int i)
{
	printf("Case #%d: %d\n",i, res);


}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-lalge.out", "w", stdout);

/*	freopen("A-large.in", "w", stdout);
	printf("15\n");
	for (int i=0; i<15; i++)
	{
		printf("1000\n");
		for (int j=0; j<1000; j++)
			printf("%d %d\n", j,j);
	}
*/
	scanf("%d",&T);


	for (int i=0; i<T; i++)
	{
		scanf("%d", &N);
		int t,t1;
		A.clear();
		B.clear();
		for (int i=0; i<N; i++)
		{
			scanf("%d%d", &t, &t1);
			A.push_back(t);
			B.push_back(t1);
		}
		
		solve();
		write(i+1);
	}
	
	return 0;
}
