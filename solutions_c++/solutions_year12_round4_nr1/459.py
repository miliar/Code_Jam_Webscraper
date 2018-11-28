#include <iostream>
#include <sstream>

#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>

#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define MAXN 10000

struct vine {
	int d, l ;
	int p;
};




int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.in.out","w",stdout);
	int nCase=1, T;
	cin >> T;
	while ( T-- ) {
            int N, D;
            vine v[MAXN];
			cin >> N ;
            for ( int i=0;i<N;++i ) {
            cin >> v[i].d >> v[i].l ;
                v[i].p = 0 ;
            }
            bool solv = false;
            cin >> D ;
			v[0].p = v[0].d ;
            for ( int i=0;i<N;++i ) {
            int limit = v[i].d + v[i].p ;
            if ( limit >= D ) solv = true;
            for ( int j=i+1;v[j].d<=limit; ++j ) {
                int dd = v[j].d-v[i].d;
                int newpower = (v[j].l>=dd?dd:v[j].l);
                if ( newpower > v[j].p ) v[j].p = newpower ;
                }
            }
            printf ( "Case #%d: %s\n", nCase++, (solv?"YES":"NO") )  ;
	}

	return 0;
}
