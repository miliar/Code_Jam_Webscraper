#include <stdio.h>

int tc;
int n, pd, pg;

int main()
{

	
	freopen("input.a.txt", "r", stdin);
	freopen("output.a.txt", "w", stdout);

	scanf("%d", &tc);

	for ( int t=1; t<=tc; t++ ){
		scanf("%d %d %d", &n, &pd, &pg);

		if ( n > 100 || n <= 0 ) n = 100;

		bool ok = true;

		if ( n < 100 ) {			
			int d;
			for ( d=1; d<=n; d++ )
				if ( (d*pd)%100 == 0 ) break;
			if ( d>n ) ok = false;
		}
		

		if ( ok ) {			
			if ( ( pg == 100 && pd < 100 ) || ( pg == 0 && pd > 0 ) ) ok = false;			
		}

		
		if ( ok ) 
			printf("Case #%d: Possible\n", t);
		else
			printf("Case #%d: Broken\n", t);
	}

	fclose(stdout);
	fclose(stdin);	

	return 0;
}