#ifdef O_O
#include "a.h"
#else
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#endif

using namespace std;

#define PB push_back
#define MP make_pair
typedef __int64 LL;
#define ALL(x)x.begin(),x.end()
#define FOR(a,b)for(int a=0;a<b;a++)
#define FORR(a,b,c)for(int a=b;a<=c;a++)
#define FOR1(a,b)for(int a=1;a<=b;a++)
#define CLR(a,b)memset(a,b,sizeof(a))
#define CPY(a,b)memcpy(a,b,sizeof(a))
#define tr(i,c)for(typeof((c).begin())i=(c).begin();i!=(c).end();i++)


template <class T> inline bool do_max(T&a,T b) {
	if(a<b) { a=b; return true; } else return false;
}

template <class T> inline bool do_min(T&a,T b) {
	if(b<a) { a=b; return true; } else return false;
}

template <class T> ostream&operator , (ostream &r,T t) {
	r << ' ' << t ;
	return r;
}

using namespace std;

char a[128][128];
bool canrow[128],cancol[128];

bool diff(char a,char b) {
    if(a==' ' || b==' ') return  false;
    return a!=b;
}

int main()
{
//    freopen("c:/gcj/a.1","rt",stdin);
	int tests;
	scanf("%d\n",&tests);
	FORR(testno,1,tests) {
		cout << "Case #"<< testno << ": ";

		int k;
		scanf("%d",&k);

		int s = 2*k-1;

        // Formatted input sucks.
/*		FOR(i,s) {
			gets(a[i]);
            FOR(iii,s) a[i][iii]=' ';
            scanf("%[^\n]s",a[i]+ abs(i-k) );
			for(int l = strlen(a[i]) ; l<s ; l++) a[i][l]=' ';
		}
*/
    if(testno==4) {
        int i=0;
    }
        FOR(i,s) {
            FOR(iii,s) a[i][iii]=' ';
            int p = abs((k-1)-i), kk=k-p,t;
            while(kk-->0) {
                scanf("%d",&t);
                a[i][p]=t+'0';
                p+=2;
            }
        }

		FOR(i,s) { canrow[i]=cancol[i]=true; }

		FOR(i,s) {
			FOR(j,s) {
				int ll=j, rr=j;
				while(--ll>=0 && ++rr<s)
					if(diff(a[i][ll],a[i][rr])) { cancol[j]=false; goto bad1; }

				bad1: ;
			}
		}

		FOR(i,s) {
			FOR(j,s) {
				int ll=j, rr=j;
				while(--ll>=0 && ++rr<s)
					if(diff(a[ll][i],a[rr][i])) { canrow[j]=false; goto bad2; }

				bad2: ;
			}
		}

		int ans=3*k;

/*        puts("");
        for(int i=0;i<s;i++, puts("")) {
            for(int j=0;j<s;j++)
                printf("%d ",cancol[j] && canrow[i]);
        }*/
		FOR(i,s)
			FOR(j,s) 
				if(cancol[i] && canrow[j]) {
					int ns =k + abs(i-k+1) + abs(j-k+1);
					do_min(ans,ns);
				}
				

		cout << ans*ans-k*k << endl;
	}

	return 0;
}