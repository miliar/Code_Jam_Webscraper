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

int vals[55];
int N,M;
char buf[555];

void test()
{
	int i,j,k;

	scanf("%d",&N);

	FIN
	{
		scanf("%s",buf);
		M=strlen(buf);
		vals[i]=0;
		FJM if(buf[j]=='1') vals[i]=j;
	}

	int cnt=0;

	FIN if(vals[i]>i)
	{
		j=i+1;
		while(vals[j]>i) j++;

		while(j>i)
		{
			swap(vals[j],vals[j-1]);
			cnt++;
			j--;
		}
	}

	printf("%d\n",cnt);
		
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