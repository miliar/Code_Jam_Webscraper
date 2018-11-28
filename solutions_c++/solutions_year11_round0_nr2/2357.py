using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )
#define rrep( i, a, b ) for( __typeof(b) i = ( a ); i >= ( b ); --i )
#define xrep( i, a, b ) _rep( i, a, b, 1 )

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

typedef vector <int> vi;

char in[5];
char comm[105];
char C[255][255];
char D[255][255];
char lst[105];
int ptr;
int main()
{
	#ifdef Local
		freopen("/home/wasi/Desktop/input.txt", "r", stdin);
		freopen("/home/wasi/Desktop/output.txt", "w", stdout);
	#endif

	int tt, c, d, n;
	scanf("%d", &tt);
	xrep(tc,1,tt)
	{
	    ms(C,0); ms(D,0);
        scanf("%d", &c);
        rep(i,c)
        {
            scanf("%s", in);
            C[in[0]][in[1]] = C[in[1]][in[0]] = in[2];
        }

        scanf("%d", &d);
        rep(i,d)
        {
            scanf("%s", in);
            D[in[0]][in[1]] = D[in[1]][in[0]] = 'X';
        }
        scanf("%d", &n);
        scanf("%s", comm);
        //cout << "OK" << endl;
        ptr = 0;
        char a, b;
        rep(i,n)
        {
            lst[ptr++] = comm[i];
            if (ptr == 1) continue;
            a = lst[ptr-1]; b = lst[ptr-2];
            if (C[a][b])
            {
                ptr--;
                lst[ptr-1] = C[a][b];
                continue;
            }
            a = lst[ptr-1];
            rep(j,ptr-1)
            {
                b = lst[j];
                if (D[a][b])
                {
                    ptr = 0;
                    break;
                }
            }

        }

        printf("Case #%d: [", tc);
        rep(i,ptr)
        {
            printf("%c", lst[i]);
            if (i < ptr-1) printf(", ");
        }
        printf("]\n");


	}

	return 0;
}
