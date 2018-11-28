#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const int N = 1111;

vector<int> F[N];

void sito()
{
	for (int i = 2; i<N; i++)
		if (F[i].empty())
		{
			for (int j=i; j<N; j+=i)
				F[j].push_back(i);
		}
}

int p[N];

int findset(int a)
{
	if (p[a]==a) return a;
	p[a]=findset(p[a]);
	return p[a];
}

void join(int a, int b)
{
	p[findset(a)]=findset(b);
}

bool is_ok(int x, int y, int P)
{
	for (int i=0; i<F[x].size(); i++)
	for (int j=0; j<F[y].size(); j++)
		if (F[x][i]==F[y][j]&&F[x][i]>=P) return 1;
	return 0;
}

void func(int cas)
{
	int a,b,P;
	scanf("%d%d%d",&a,&b,&P);
	for (int i=a; i<=b; i++)
		p[i]=i;
	for (int i=a; i<=b; i++)
	for (int j=i+1; j<=b; j++)
		if (is_ok(i,j,P)) join(i,j);
	int tab[N];
	for (int i=a; i<=b; i++)
		tab[i]=findset(i);
	sort(tab+a,tab+b+1);
	int val = unique(tab+a,tab+b+1)-(tab+a);
	printf("Case #%d: %d\n",cas,val);
}

int main()
{
	sito();
	int n;
	scanf("%d",&n);
	for (int i=0; i<n; i++)
		func(i+1);
	return 0;
}


