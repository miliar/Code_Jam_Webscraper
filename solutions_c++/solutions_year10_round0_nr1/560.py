#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <sstream>
#include <cctype>

#define FIN for(i=0;i<N;i++)
#define FIM for(i=0;i<M;i++)
#define FJN for(j=0;j<N;j++)
#define FJM for(j=0;j<M;j++)
#define FOR(i,N) for(i=0;i<N;i++)
#define FAB(i,A,B) for(i=A;i<=B;i++)
using namespace std;

int N,K;

void test()
{
	scanf("%d%d",&N,&K);

	int cnt=0;

	while(K%2)
	{
		cnt++;
		K/=2;
	}

	if(cnt>=N) printf("ON\n");
	else printf("OFF\n");
		
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int t=0,T;

	scanf("%d",&T);

	for(t=0;t<T;t++)
	{
		printf("Case #%d: ",t+1);
		test();
	}
}