#include <iostream.h>

int main()
{
	// file streams
//	freopen("A-small-attempt0.in","r",stdin); freopen("A-small.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

	// inputs
	int t;
	int n, k;		
	
	// outputs
	int x;
	bool y;
	
	// algorithm
	scanf("%d", &t);
	for (int x=1; x<=t; x++)
	{	
		// read inputs
		scanf("%d %d", &n, &k);
		
		// process
		y = (k == 0) ? false :(((k+1) % (1<<n) == 0) ? true : false);
		
		// write outputs
		printf("Case #%d: %s\n", x, y?"ON":"OFF");
	}
	
	// end
	return 0;
}