#include<algorithm>
#include<cstdio>
#include<string>
#include<set>
#include<vector>
using namespace std;

#define fore(i,n) for(int i = 0; i < (n); i++)
#define fort(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

#define err(...) fprintf(stderr, __VA_ARGS__)

int res,n,m;
char path[111];
set<string> S;

void create(string x)
{
	if(S.find(x) != S.end()) return;
	res++;
	S.insert(x);
	int pos = x.size()-1;
	while(x[pos] != '/') pos--;
	if(pos == 0) return;
	create(x.substr(0,pos));
}

void test()
{
	res = 0;
	S.clear();
	scanf("%d%d", &n, &m);
	fore(i,n)
	{
		scanf("%s", path);
		S.insert(path);
	}
	fore(i,m)
	{
		scanf("%s", path);
		create(path);
	}
	printf("%d\n", res);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		test();
	}
}
