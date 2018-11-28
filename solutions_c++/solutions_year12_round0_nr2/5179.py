#include <iostream>
#include <algorithm>

#include <stdio.h>

using namespace std;

int main(int argc, char *argv[])
{
    int testcases, cases, i, j, start_comp_from = 0;
    scanf("%d", &testcases);
    
    for( cases = 1; cases <= testcases; cases++ )
    {
	int no_googlers, surprising, best, *googlers, have_best = 0;
	googlers = new int[no_googlers];
	
	scanf("%d %d %d", &no_googlers, &surprising, &best);
	for( i = 0; i < no_googlers; i++ )
	{
	    scanf("%d", &googlers[i]);
	}
	
	sort(googlers, googlers + no_googlers );
	
	for( i = no_googlers - 1; i >= 0; i--)
	{
	    for( j = start_comp_from; (3 * j) <= googlers[i]; j++ )
		;
	    j--;
	    
	    if( j >= best )
	    {
		have_best++;
	    }
	    else if( ( ( googlers[i] - (3 * j) ) == 0 ) && ( (best - j) == 1 ) && ( surprising != 0 ) && ( ( j - 1 ) >= 0 ) )
	    {
		surprising--;
		have_best++;
	    }
	    else if( ( ( googlers[i] - (3 * j) ) == 1 ) && ( (best - j) == 1 ) )
	    {
		have_best++;
	    }
	    else if( ( ( googlers[i] - (3 * j) ) == 2 ) && ( (best - j) == 1 ) )
	    {
		have_best++;
	    }
	    else if( ( ( googlers[i] - (3 * j) ) == 2 ) && ( (best - j) == 2 ) && ( surprising != 0 ) )
	    {
		surprising--;
		have_best++;
	    }
	}
	printf("Case #%d: %d\n", cases, have_best);
    }
    
    return 0;
}