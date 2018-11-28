#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int Test,Case,n,m,p;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	for (scanf("%d",&Test);Test;--Test) {
		scanf("%d%d",&n,&m);p=1;
		for (int i=0;i<n;i++)
			p<<=1;
		printf("Case #%d: ",++Case);
		if (m%p!=p-1) printf("OFF\n");
			else printf("ON\n");
	}
	return 0;
}
