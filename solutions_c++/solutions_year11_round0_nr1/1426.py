#include<cstdio>
#include<algorithm>
using namespace std;

int main() {
	int n,t;
	scanf("%d",&t);
	for (int i=1; i<=t; i++)
	{
		int os,bs,p,result,op,bp;
		char r;
		result = 0;
		os = bs = 0;
		op = bp = 1;
		scanf("%d ",&n);
		while(n--)
		{
			scanf("%c %d ",&r,&p);
			if (r == 'B')
			{
				int tmp = abs(p-bp);
				if (tmp <= bs) {
					result++;
					bs = 0;
					os ++;
				} else {
					tmp -= bs;
					bs = 0;
					result += tmp+1;
					os += tmp+1;
				}
				bp = p;
			}
			else 
			{
				int tmp = abs(p-op);
				if (tmp <= os) {
					result++;
					os = 0;
					bs++;
				} else {
					tmp -= os;
					os = 0;
					result += tmp+1;
					bs += tmp+1;
				}
				op = p;
			}
		}
		printf("Case #%d: %d\n",i,result);
	}
}
