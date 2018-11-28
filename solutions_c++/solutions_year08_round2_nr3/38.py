#include <cstdio>
using namespace std;
const int N = 1000*1000+10;
const int T = 1<<20;

int n;
int tree[2*T];
int s[N];

void init()
{
	for (int i=0; i<T; i++)
		tree[i+T]=1;
	for (int i=T-1; i>0; i--)
		tree[i]=tree[2*i]+tree[1+2*i];
}

void add(int a)
{
	a+=T;
	tree[a]=0;
	while (a>1)
	{
		a/=2;
		tree[a]=tree[2*a]+tree[1+2*a];
	}
}

int fnd(int x)
{
	int a = 1;
	while (a<T)
	{
		a=a*2;
		if (tree[a]<x)
		{
			x-=tree[a];
			a++;
		}
	}
	return a-T;
}

void show_tree()
{
	return;
	for (int i=1; i<T; i++)
		printf("%d ",tree[i]);
	printf("\n");
	for (int i=0; i<T; i++)
		printf("%d ",tree[T+i]);
	printf("\n");
}

int sum(int l, int r)
{
//	printf("sum %d %d\n",l,r);
	l+=T;r+=T;
	if (l==r) return tree[l];
	int ls,rs;
	ls = tree[l];
	rs = tree[r];
	while ((l/2)!=(r/2))
	{
		if ((l%2)==0) ls+=tree[l+1];
		if ((r%2)==1) rs+=tree[r-1];
		l/=2;r/=2;
	}
//	printf("%d\n",ls+rs);
	return ls+rs;
}

void obl()
{
	init();
	int last = 0;
	s[0]=0;
	add(0);
	last=0;
	for (int i=1; i<n; i++)
	{
	//	show_tree();
		int pos = i%(n-i);
		pos ++;
		int bef = sum(last,n-1);
//		printf("pos/bef = %d %d\n",pos,bef);
		if (bef>=pos)
			pos = fnd(sum(0,last)+pos);
		else
			pos = fnd(pos-bef);

		add(pos);
		s[pos]=i;
//		printf("s[%d]=%d\n",pos,i);
		last = pos;
	}

}

void func(int cas)
{
	scanf("%d",&n);
	obl();
	printf("Case #%d:",cas+1);
	scanf("%d",&n);
	while (n--)
	{
		int k;
		scanf("%d",&k);
		printf(" %d",1+s[k-1]);
	}
	printf("\n");
}

int main()
{
	int j;
	scanf("%d",&j);
	for (int i=0; i<j; i++)
		func(i);
	return 0;
}




