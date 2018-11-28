/*
 * Google Code Jam template :-)
 */

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
//#include <ctype.h>
//#include <assert.h>
//#include <math.h>
//#include <set>
//#include <map>

using namespace std;

typedef unsigned idx;

#define GMAX 100
bool grid[GMAX][GMAX];

void clearG(void)
{
    for (idx i=0; i<GMAX; ++i)
    for (idx j=0; j<GMAX; ++j)
	grid[i][j] = false;
}

idx oneStep(idx total)
{
    for (idx i=GMAX-1; i>0; --i)
    for (idx j=GMAX-1; j>0; --j)
    {
	if(grid[i][j])
	{
	    if(!grid[i-1][j] && !grid[i][j-1])
	    {
		grid[i][j] = false;
		--total;
	    }
	}
	else
	{
	    if(grid[i-1][j] && grid[i][j-1])
	    {
		grid[i][j] = true;
		++total;
	    }
	}
    }
    for (idx i=GMAX-1; i>0; --i)
    {
	if (grid[i][0])
	{
	    if (!grid[i-1][0])
	    {
		grid[i][0] = false;
		--total;
	    }
	}
	if (grid[0][i])
	{
	    if (!grid[0][i-1])
	    {
		grid[0][i] = false;
		--total;
	    }
	}
    }
    if (grid[0][0])
    {
	grid[0][0]=0;
	--total;
    }
    return total;
}

void solve(const idx t)
{
    idx tim=0;
    idx R;
    idx total=0;

    cin >> R;
    for (idx c=1; c<=R; ++c)
    {
	idx xa, xb, ya, yb;
	cin >> xa >> ya >> xb >> yb;
	for (idx i=xa-1; i<xb; ++i)
	    for (idx j=ya-1; j<yb; ++j)
	    {
		if(!grid[i][j]) ++total;
		grid[i][j] = true;
	    }
    }
    while(total>0)
    {
	++tim;
	total = oneStep(total);
//	cerr << tim << "=tim, total=" << total << endl;
    }
    cout << "Case #" << t << ": " << tim << endl;
}

int main(void)
{
    idx T;

    cin >> T;
    for(idx t=1; t<=T; ++t) solve(t);

    return 0;
}
