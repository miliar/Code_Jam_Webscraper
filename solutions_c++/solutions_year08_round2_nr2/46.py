#include <iostream>

using namespace std;

const int MAXN = 10000;

int a, b, p, s;
int root[MAXN];

void init()
{
	scanf("%d%d%d", &a, &b, &p);		
}

int find(int x)
{
	if (root[x]<=0) return x; else
	{
		root[x]=find(root[x]);
		return root[x];	
	}	
}

void merge(int x, int y)
{
	x=find(x);
	y=find(y);
	if (x!=y){
		s--;
		root[y]+=root[x];	
		root[x]=y;
	}
}

bool prime(int x)
{
	int i;
	for (i=2; i*i<=x; i++)
		if (x%i==0) return false;
	return true;	
}

void work()
{
	int i, j;
	
	memset(root, 0xFF, sizeof(root));
	s=(b-a+1);
	for (i=p; i<=b; i++)
		if (prime(i)){
			j=i;
			while (j<a) j=j+i;
			while (j<=b){
				if (j-i>=a)
					merge(j-i, j);	
				j+=i;
			}	
		}	
	printf("%d\n", s);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas=0, t;
	scanf("%d", &t);
	while (t--){
		cas++;
		printf("Case #%d: ", cas);
		init();
		work();
	}
	
	return 0;
}
