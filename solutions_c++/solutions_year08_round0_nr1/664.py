#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cctype>
#include <sstream>
#include <ostream>
#include <iterator>
#include <algorithm>
#include <set>

#define DEBUG							0
#define __SEARCH_ENGINES					128

using namespace std;

struct SEngine
{
    char Name[1024];
    unsigned int *CPTR;
};

struct ltstr
{
  bool operator()(SEngine f, SEngine s) const
  {
    return strcmp(f.Name, s.Name) < 0;
  }
};

int DO_TEST()
{
    int i,j,k,l,s,q,r,u;

    SEngine SEA[__SEARCH_ENGINES], SE, LAST_SE;
    unsigned int Count[__SEARCH_ENGINES];

    set<SEngine>::iterator iter;

    /* init */
    r = 0;
    u = 0;
    /* end of init */

    for( scanf("%d", &s), i=0; i < s; i++ )
    {
	fgets(SEA[i].Name, sizeof(SEA[i].Name), stdin);
	if( SEA[i].Name[0] == '\n' ) { i--; continue; }

	Count[i] = 0;
	SEA[i].CPTR = &Count[i];
    }

    set<SEngine, ltstr> A(SEA, SEA + s);

    for( scanf("%d", &q), i=j=0; i < q; i++ )
    {
	fgets(SE.Name, sizeof(SE.Name), stdin);
	if( SE.Name[0] == '\n' ) { i--; continue; }

	if( !A.count(SE) ) { continue; }
	if( j && !strcmp(LAST_SE.Name, SE.Name) ) { continue; }
	
	j++;
	strncpy(LAST_SE.Name, SE.Name, sizeof(LAST_SE.Name));
	
	iter = A.find(SE);
	if( *iter->CPTR ) { continue; }

	(*iter->CPTR) = 1;
	u++;

	if( u == s )
	{
	    u = 1;
	    r++;

	    (*iter->CPTR) = !(*iter->CPTR);

	    for( iter = A.begin(); iter != A.end(); iter++ ) {
		(*iter->CPTR) = !(*iter->CPTR);
	    }
	}
    }

    if(DEBUG) cout << "Set A: " << endl;

    for( i=0, iter = A.begin(); iter != A.end(); iter++, i++ ) {
	if(DEBUG) printf("   (%u) %s", *(iter->CPTR), iter->Name);
    }

    if(DEBUG) cout << endl;

    return r;
}

int main()
{
    int i,j,k,l,n;

    scanf("%d", &n);

    for( i=0; i < n; i++ ) {
	j = DO_TEST();
	printf("Case #%d: %d\n", i+1, j);
    }

    return 0;
}

