#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#define MAXN 200

using namespace std;

struct node
{
	long long c;
	int id;
}A[MAXN+10],B[MAXN+10];

int N,M;

long long maxDfs(int i, int j)
{
	if (i == N || j == M) return 0;
	if (A[i].id == B[j].id)
	{
		long long Min = A[i].c;
		bool flag = false;
		if (Min > B[j].c)
		{
			flag = true;
			Min = B[j].c;
		}
		A[i].c -= Min;
		B[j].c -= Min;
		long long Max = 0;
		if (flag) Max = maxDfs(i,j+1) + Min;
		else Max = maxDfs(i+1,j) + Min;
		A[i].c += Min;
		B[j].c += Min;
		return Max;
	}
	long long Max1 = maxDfs(i,j+1);
	long long Max2 = maxDfs(i+1,j);
	return  Max1 > Max2 ? Max1 : Max2;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for (int i = 1;i <= T;++i)
	{
	    printf("Case #%d: ",i);
		scanf("%d%d",&N,&M);
        node temp;
        for (int i = 0;i < N;++i)
        {
            scanf("%lld%d",&A[i].c,&A[i].id);
        }
        for (int i = 0;i < M;++i)
        {
            scanf("%lld%d",&B[i].c,&B[i].id);
        }
        printf("%lld\n",maxDfs(0,0));
	}
}
