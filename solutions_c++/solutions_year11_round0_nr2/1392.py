#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>

using namespace std;

#define sqr(a)		((a)*(a))
#define rep(i,a,b)	for(int i=(a);i<(int)(b);i++)
#define per(i,a,b)	for(int i=((a)-1);i>=(int)(b);i--)
#define PER(i,n)	per(i,n,0)
#define REP(i,n)	rep(i,0,n)
#define clr(a)		memset((a),0,sizeof (a))
#define SZ(a)		((int)((a).size()))
#define ALL(x)		x.begin(),x.end()
#define mabs(a)		((a)>0?(a):(-(a)))
#define inf			1000000001 
#define eps			1e-6

void swap(int* a,int* b)
{
	if (a != b)
	{
		*a ^= *b;
		*b ^= *a;
		*a ^= *b;
	}
}

int main()
{
	freopen("data1.in","r",stdin);
	freopen("data2.in","w",stdout);

	int T;
	scanf("%d",&T);

	REP(K,T)
	{
		int cob[26][26];
		int opp[26][26];
		REP(i,26)
		{
			REP(j,26)
			{
				cob[i][j] = -1;
			}
		}
		clr(opp);
		int n;
		scanf("%d",&n);
		REP(i,n)
		{
			char s[100];
			scanf("%s",s);
			cob[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
			cob[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		int m;
		scanf("%d",&m);
		REP(i,m)
		{
			char s[100];
			scanf("%s",s);
			opp[s[0] - 'A'][s[1] - 'A'] = 1;
			opp[s[1] - 'A'][s[0] - 'A'] = 1;
		}

		int len = -1;
		char str[200];
		char res[200] = "";
		int top = 0;
		scanf("%d",&len);
		scanf("%s",str);

		REP(i,len)
		{
			int j;
			int p = str[i] - 'A';
			int flag = 0;

			if (top != 0)
			{
				int q = res[top - 1] - 'A';
				if (cob[p][q] != -1)
				{
					res[top - 1] = cob[p][q] + 'A';
					flag = 1;
				}
			}
			for (j = top - 1;j >= 0 && !flag;j--)
			{
				int k = res[j] - 'A';
				if (opp[p][k] != 0)
				{
					top = 0;
					break;
				}
			}
			if (j < 0)
			{
				res[top++] = str[i];
			}
		}

		printf("Case #%d: [",K + 1);
		REP(i,top)
		{
			if (i != 0)
			{
				printf(", ");
			}
			printf("%c",res[i]);
		}
		printf("]\n");
	}

	fclose(stdin);
	fclose(stdout);
}

