#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
int T;
int N,K;
int main()
{
	freopen("..\\A.in","r",stdin);
	freopen("..\\A_large.out","w",stdout);
	scanf("%d",&T);
	for(int i = 1;i <= T;i++)
	{
		scanf("%d %d",&N, &K);
		int all = 1 << N;
		int t_mod = K % all;
		if((K + 1) % all == 0)
			printf("Case #%d: ON\n" ,i);
		else
			printf("Case #%d: OFF\n" ,i);
	}
	return 0;
}