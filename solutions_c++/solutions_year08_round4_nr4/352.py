#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define i64 __int64

i64 cases,caseno;
int k,n;
char a[50002],b[50002];

void input()
{
	scanf("%d %s",&k,a);
}

int compressRes()
{
	int i,k=0;
	char ch;

	for(i=0;i<n;)
	{
		ch=b[i];
		while(ch==b[i]) i++;
		k++;
	}
	return k;
}

void process()
{
	printf("Case #%I64d: ",++caseno);

	int X[20],i,mn=1000000,j,res;

	for(i=0;i<k;i++) X[i]=i;
	n=strlen(a);

	do
	{
		for(i=0;i<n;i+=k)
		{
			for(j=0;j<k;j++)
			{
				b[i+j]=a[X[j]+i];
			}
		}
		b[n]=0;
		/*for(i=0;i<k;i++) printf(" %d",X[i]);
		printf(" %s\n",b);*/
		res=compressRes();
		mn=min(mn,res);
	}while(next_permutation(X,X+k));
	printf("%d\n",mn);
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d1.ans","w",stdout);
		
	scanf("%I64d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}
