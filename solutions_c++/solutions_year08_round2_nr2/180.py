#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<algorithm>

using namespace std;

typedef __int64 LL;

int p[2000],rank[2000];
int prime[2000],flag[2000],done[2000];


void make_set(int x) 
{
  p[x] = x;
  rank[x] = 0;
}

void link(int x,int y) 
{
  if (rank[x] > rank[y])
    p[y] = x;
  else {
    p[x] = y;
    if (rank[x] == rank[y])
      rank[y] = rank[y] + 1;
  }
}

int find_set(int x) 
{
  if (x != p[x])
    p[x] = find_set(p[x]);
  return p[x];
}



int main()
{
	int tests,cs=0,i,j,k;

	prime[2]=1;
	for(i=3;i<1000;i+=2)
	{
		int isprime=1;
		for(j=3;isprime && j*j<=i;j+=2)
			if(i%j==0) isprime=0;
		prime[i]=isprime;
	}


	freopen("C:\\Bsmall.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		int A,B,P;

		scanf("%d %d %d",&A,&B,&P);

		for(i=1;i<=1000;i++)
			make_set(i);

		memset(flag,0,sizeof(flag));
		memset(done,0,sizeof(done));
	
		for(i=A;i<=B;i++)
		{

			for(j=P;j<=i;j++)
			{
				if(prime[j]==0 || i%j) continue;
				link(find_set(i),find_set(j));
				
			}

		}

		int ans=0;

		for(i=A;i<=B;i++)
			done[find_set(i)]=1;

		for(i=1;i<=1000;i++)
			if(done[i]) ans++;
			
		printf("Case #%d: %d\n",++cs,ans);

	}

	return 0;
}