// Doing this brute force - my stochastic prof kills me!!!
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

//typedef struct pair {
class pair {
	public:
	int a;
	int b;
};

//bool compare(const pair * const p1, const pair * const p2) //const
bool compare(pair * p1, pair * p2) //const
{
	return ( p1->a == p2->a && p1->b == p2->b);
}

int main()
{
	// number of samples:
	int s;
	scanf("%d",&s);
	for (int j=1; j<=s; j++)
	{

	int k=0;
	int n,m;
	scanf("%d %d",&m,&n);
	std::vector<pair*> v;
	// no leading zeros
	
	int q0 = (int) pow(10,ceil(log(n)/log(10)));
	// leading zero specification somewhat unclear does pair 021 and 012 count or not ?
	// we exclude those cases (occuring if m < n/10)
	int l0 = (int) pow(10,floor(log(n)/log(10)));
//	printf("%d %d\n",q0,l0);
	for (int i=m; i<=n; i++)
	{
		int p=10;
		int q = q0/10;
		while (p < i)
		{
			int a = (i % p)*q;
			int b = i / p;
			int c = a + b;
//			printf("%d %d\n",c,i);
			if ( c > i && c <= n && c >= m && c/l0 > 0 && i/l0 > 0)
			{
//			printf("%d %d\n",c,i);
				
				k++;
				pair *p = new pair();
				p->a = i; p->b = c;
				v.push_back(p);
			}
			p *= 10;
			q /= 10;
		} // while
	} // for i

//	printf("%d\n",k);

	// remove spurious 1212 - 2121
//	printf("%d\n",v.size());
	std::vector<pair*>::iterator it = std::unique (v.begin(), v.end(), compare);
	v.resize(it - v.begin());
	printf("Case #%d: %d\n",j,v.size());
	} // for j
	return 0;
} // main

