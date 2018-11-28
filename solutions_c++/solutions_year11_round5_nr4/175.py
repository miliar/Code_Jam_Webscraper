#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define S(X) ((X)*(X))
#define ABS(X) ((X)>0?(X):(-(X)))
#define SZ(X) (int)(X.size())
typedef pair<int,int> PII;
typedef __int64 LL;

int len;

void PRINT(LL a)
{
	LL i;

	for(i=len-1;i>=0;i--)
		if(a & (1<<i)) printf("1");
		else printf("0");
	printf("\n");
}

int mysqrt(LL a)
{
	LL x = sqrt(a),y;
	int i;

	for(i=-2;i<=2;i++)
	{
		y = x+ i;

		if(y>=0 && y*y==a)
		{
			PRINT(a);
			return 1;
		}
	}

	return 0;
}

int main()
{
//	freopen("D-small-attempt0.in","r",stdin); freopen("D-small-output0.out","w",stdout);
	freopen("D-small-attempt1.in","r",stdin); freopen("D-small-output1.out","w",stdout);
//	freopen("D-small-attempt2.in","r",stdin); freopen("D-small-output2.out","w",stdout);
//	freopen("D-large.in","r",stdin); freopen("D-large.out","w",stdout);

	int T, ks;
	LL now;
	char word[100];
	int i,cnt;
	int lim;
	int t,j;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);

		scanf("%s",word);

		len = strlen(word);
	
		cnt=0;
		for(i=0;i<len;i++)
			cnt+=word[i]=='?';

		lim = 1<<cnt;
		for(i=0;i<lim;i++)
		{
			now = 0;
			t=0;
			for(j=0;j<len;j++)
			{
				now<<=1;

				if(word[j]=='1') now=now|1;
				else if(word[j]=='0') now=now;
				else
				{
					if(i&(1<<t)) now=now|1;
					t++;
				}
			}

			if(mysqrt(now))
			{
				break;
			}
		}
	}

	return 0;
}