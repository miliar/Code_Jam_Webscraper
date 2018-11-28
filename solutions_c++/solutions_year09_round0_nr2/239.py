#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int dmax=105;
int a[dmax][dmax];			// altitude
char b[dmax][dmax];			// basin labels
char nextLabel;
const int dr[4] = {-1,0,0,1}, dc[4] = {0,-1,1,0}; // directions for North, West, East, South

char find(int r,int c)
{
    if(b[r][c])
    {
	//printf("%d %d\n",r,c);
	return b[r][c];
    }
    
    int dir=-1, amin=a[r][c];
    for(int i=0;i<4;i++)
	if(a[r+dr[i]][c+dc[i]] < amin)
	{
	    dir=i;
	    amin=a[r+dr[i]][c+dc[i]];
	}
    
    if(dir==-1)
    {
	// the cell is a sink
	if(!b[r][c])
	    b[r][c]=nextLabel++;
    }
    else
	b[r][c]=find(r+dr[dir],c+dc[dir]);
    
    // printf("%d %d: %c\n",r,c,b[r][c]);
    return b[r][c];
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	int R,C;
	scanf("%d%d",&R,&C);
	for(int r=0;r<=R+1;r++)
	    for(int c=0;c<=C+1;c++)
		if(r<1 || c<1 || r>R || c>C)
		    a[r][c]=numeric_limits<int>::max();
		else
		    scanf("%d",&a[r][c]);

	nextLabel='a';
	memset(b,0,sizeof(b));

	printf("Case #%d:\n",test_case);
	
	for(int r=1;r<=R;r++)
	    for(int c=1;c<=C;c++)
	    {
		find(r,c);
		//printf("\n");
	    }
	
	for(int r=1;r<=R;r++)
	{
	    for(int c=1;c<=C;c++)
		printf("%c ",b[r][c]);
	    printf("\n");
	}
    }
    return 0;
}
