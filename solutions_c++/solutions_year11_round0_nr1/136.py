// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
	int t,cas=0;
	int n,t1,t2,p1,p2,x;
	char clr;
	scanf("%d",&t);
	while ( t-- ) {
		t1=t2=0;
		p1=p2=1;
		scanf("%d",&n);
		while ( n-- ) {
			scanf(" %c %d",&clr,&x);
			if ( clr=='B' ) {
				t1+=abs(p1-x);
				if ( t1<t2 ) t1=t2;
				t1++;
				p1=x;
			} else if ( clr=='O' ) {
				t2+=abs(p2-x);
				if ( t2<t1 ) t2=t1;
				t2++;
				p2=x;
			} else puts("QQ");
		}
		printf("Case #%d: %d\n",++cas,max(t1,t2));
	}
	return 0;
}
