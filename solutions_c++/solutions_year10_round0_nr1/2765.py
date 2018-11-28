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

//#define SZ 1100000000
using namespace std;

int T, N,K;
bool res;


bool solve2()
{
	int k=K+1;
	int n=1;
	for (int i=0; i<N; i++)
		n*=2;
	return (k%n==0);
}

void write(int i)
{
	printf("Case #%d: ",i+1);
	if (res) printf("ON");
	else printf("OFF");
	if (i!=T-1) printf("\n");
}
int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);




	scanf("%d",&T);
	for (int i=0; i<T; i++)
	{
		scanf("%d%d", &N,&K);
		res = solve2();
		write(i);
	}

	return 0;
}
