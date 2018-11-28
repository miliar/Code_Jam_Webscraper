#include <cstdio>
#include <algorithm>
#define MAX 110

using namespace std;

char diamond[MAX][MAX];
int ncases, n;

int v_sim()
{
	bool valid;
	int axis, best=n-1;
	for(axis=1; axis<n*2-2; axis++)
	{
		valid=true;
		for(int row=0; row<n*2-1 && valid; row++)
			for(int coloffset=1; axis-coloffset>=0 && axis+coloffset<n*2-1 && valid; coloffset++)
				if(diamond[row][axis-coloffset]!=' ' && diamond[row][axis+coloffset]!='\n' && diamond[row][axis+coloffset]!='\0' && diamond[row][axis-coloffset]!=diamond[row][axis+coloffset])
					valid=false;
		
		int tempaxis=axis;
		if(axis>(n*2-2)/2)
			tempaxis=n*2-2-axis;
		if(valid)
			best=min(best, n-1-tempaxis);
	}
	
	return best;
}

int h_sim()
{
	bool valid;
	int axis, best=n-1;
	for(axis=1; axis<n*2-2; axis++)
	{
		valid=true;		
		for(int col=0; col<n*2-1 && valid; col++)
			for(int rowoffset=1; axis-rowoffset>=0 && axis+rowoffset<n*2-1 && valid; rowoffset++)
				if(diamond[col][axis-rowoffset]!=' ' && diamond[col][axis+rowoffset]!='\n' && diamond[col][axis+rowoffset]!='\0' && diamond[axis-rowoffset][col]!=diamond[axis+rowoffset][col])
					valid=false;
	
		int tempaxis=axis;
		if(axis>(n*2-2)/2)
			tempaxis=n*2-2-axis;
		if(valid)
			best=min(best, n-1-tempaxis);
	}
	
	return best;
}

int main()
{
	scanf("%d", &ncases);
	for(int t=0; t<ncases; t++)
	{
		memset(diamond, 0, sizeof(diamond));
		scanf("%d", &n);
		getchar();
		for(int i=0; i<2*n-1; i++)
		{
			fgets(diamond[i], 10000, stdin);
		}
		int h=h_sim(), v=v_sim();
		printf("Case #%d: %d\n", t+1, (v+h+n)*(v+h+n) - (n*n));
	}
	return 0;
}
