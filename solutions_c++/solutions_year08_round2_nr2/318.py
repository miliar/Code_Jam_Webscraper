#include <iostream>
#include <cmath>
using namespace std;

int A,B,P;

#define MAXN 2000

int p[MAXN], rank[MAXN], cntSet;

void make_set(int x) {
    p[x] = x;
    rank[x] = 0;
}

void link(int x, int y) {
    if (rank[x] > rank[y]) p[y] = x;
    else {
        p[x] = y;
        if (rank[x] == rank[y]) ++rank[y];
    }
}

int find_set(int x) {
    if (x != p[x]) p[x] = find_set(p[x]);
    return p[x];
}

void union_set(int x, int y) {
    x = find_set(x);
    y = find_set(y);
    if (x != y) {
        --cntSet;
        link(x, y);
    }
}

bool is_prime(int n)
{
	int q=(int)sqrt((double)n);
	for(int i=2;i<=q;++i)
		if(n%i==0) return false;
	return true;
}

void work()
{
	int res=0;
	int j,l;
	for(int i=0;i<2000;++i)
		make_set(i);
	for(int i=P;;++i)
	{
		if(!is_prime(i)) continue;
		if(2*i>B) break;
		for(j=i;j<A;j+=i);
		if(j>B) continue;
		l=j;
		for(j+=i;j<=B;j+=i)
		{
			union_set(l,j);
			l=j;
		}
	}
	for(int i=A;i<=B;++i)
	{
		if(find_set(i)==i) ++res;
	}
	printf("%d\n",res);
}

int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;++i)
	{
		scanf("%d%d%d",&A,&B,&P);
		printf("Case #%d: ",i+1);
		work();
	}
	return 0;
}