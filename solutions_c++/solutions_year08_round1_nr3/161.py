#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))

int a[40];

int main()
{
    int i, j, cas, T, n;

a[2]=27;
a[3]=143;
a[4]=751;
a[5]=935;
a[6]=607;
a[7]=903;
a[8]=991;
a[9]=335;
a[10]=47;
a[11]=943;
a[12]=471;
a[13]=55;
a[14]=447;
a[15]=463;
a[16]=991;
a[17]=95;
a[18]=607;
a[19]=263;
a[20]=151;
a[21]=855;
a[22]=527;
a[23]=743;
a[24]=351;
a[25]=135;
a[26]=407;
a[27]=903;
a[28]=791;
a[29]=135;
a[30]=647;

    scanf( "%d", &T );
    for ( cas = 1 ; cas <= T ; cas++ )
    {
        scanf( "%d", &n );
        printf( "Case #%d: %03d\n", cas, a[n] );
    }

    return 0;
}
