#include <iostream>
#include <cstring>
#include <sstream>
#include <cmath>
using namespace std;
#define MAXN 1000000
#define MAX(a,b) ((a)>(b)?(a):(b))

int number[100];
int t,L;
int base;
long long ans;
char word[100];
bool hash[256];
int link[256];

void pre()
{
	for(int i = 0; i < 100; i++)
		number[i] = i;
	number[0] = 1, number[1] = 0;
}

void init()
{
	base = 0;
	scanf("%s",word);
	L = strlen(word);
	memset(hash,0,sizeof(hash));
	for(int i = 0; i < L; i++)
		if(!hash[word[i]])
			link[word[i]] = number[base++], hash[word[i]] = true;
}

void solve()
{
	if(base==1)
		base=2;
	ans = 0;
	long long p = 1;
	for(int i = L-1; i >= 0; i--)
		ans += p*link[word[i]], p *= base;
}

void print()
{
	printf("Case #%d: %I64d\n",t+1,ans);
}

int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int T;
	pre();
	scanf("%d\n",&T);
	for(t = 0; t < T; t++)
	{
		init();
		solve();
		print();
	}
    return 0;
}
