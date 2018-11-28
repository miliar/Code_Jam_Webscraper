// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#define S 300
#define N 110
using namespace std;
char cmb[S][S];
bool opp[S][S];
char lst[N];
int main()
{
	int t,cas=0;
	int c,d,n,m,i;
	char x,y,z;
	scanf("%d",&t);
	while ( t-- ) {
		memset(cmb,0,sizeof(cmb));
		memset(opp,0,sizeof(opp));
		scanf("%d",&c);
		while ( c-- ) {
			scanf(" %c%c%c",&x,&y,&z);
			cmb[(int)x][(int)y]=cmb[(int)y][(int)x]=z;
		}
		scanf("%d",&d);
		while ( d-- ) {
			scanf(" %c%c",&x,&y);
			opp[(int)x][(int)y]=opp[(int)y][(int)x]=1;
		}
		m=0;
		scanf("%d",&n);
		while ( n-- ) {
			scanf(" %c",lst+m); m++;
			while ( m>=2 && cmb[(int)lst[m-1]][(int)lst[m-2]] ) {
				lst[m-2]=cmb[(int)lst[m-1]][(int)lst[m-2]];
				m--;
			}
			for ( i=0; i<m; i++ )
				if ( opp[(int)lst[i]][(int)lst[m-1]] ) m=0;
		}
		printf("Case #%d: ",++cas);
		if ( m==0 ) { puts("[]"); continue; }
		putchar('[');
		for ( i=0; i<m; i++ )
			printf("%c%s",lst[i],i==m-1?"]\n":", ");
	}
	return 0;
}
