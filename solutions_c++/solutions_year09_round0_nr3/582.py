#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;
#define MOD 10000
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

int n,l;
int ans;
const int L = 19;
char str[501];
int f[19][501];
const char st[20] = "welcome to code jam";

void init()
{
	scanf("%d\n",&n);
}

void solve()
{
	for(int i = 0; i < n; i++)
	{
		ans = 0;
		gets(str);
		l = strlen(str);
		memset(f,0,sizeof(f));
		for(int j = 0; j < l; j++)
			if(str[j]==st[0])
				f[0][j] = 1;
		for(int j = 1; j < L; j++)
			for(int k = 0; k < l; k++)
				if(str[k]==st[j])
					for(int m = 0; m < k; m++)
						f[j][k] = (f[j][k]+f[j-1][m])%MOD;
		for(int j = 0; j < l; j++)
			ans = (ans+f[L-1][j])%MOD;
		if(ans>=1000)
			printf("Case #%d: %d\n",i+1,ans);
		else if(ans>=100)
			printf("Case #%d: 0%d\n",i+1,ans);
		else if(ans>=10)
			printf("Case #%d: 00%d\n",i+1,ans);
		else
			printf("Case #%d: 000%d\n",i+1,ans);
	}
}

void print()
{
}

int main(void)
{
    init();
    solve();
    print();
    return 0;
}

