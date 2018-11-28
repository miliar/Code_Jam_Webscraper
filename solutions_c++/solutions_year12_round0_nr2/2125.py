#include <cstdio>
#include <cstring>

using namespace std;

int main () {

		freopen ("input_b.in","r",stdin);
		freopen ("output_b.out","w",stdout);
		
		int TC,n,s,p,nc,sc,in,y;
		scanf ("%d",&TC);

		for (int k=0;k<TC;k++) {
				scanf ("%d %d %d",&n,&s,&p);
				nc=3*p-2;
				sc=3*p-4;
				y=0;
				for (int i=0;i<n;i++) {
							scanf ("%d",&in);
							if (!in && p!=0) continue;
							if (in >= nc )
									y++;
							else if (in >= sc && s ) {
									y++;
									s--;
							}
				}

				printf ("Case #%d: %d\n",k+1,y);
		}
}

							

				
							
				/*			if (q >= p )
									y++;
							else if ( r > 0  && q == p-1)
									y++;
							else if ( r == 2 && q == p-2 && s > 0) {
									s--;
									y++;
							}

							
				 */





