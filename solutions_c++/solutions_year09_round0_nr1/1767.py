#include <stdio.h>
#include <vector>

using namespace std;

int index[15][26][5001];    // [loc][char] -> posting list
int result[5000];
char line[15 * 28 + 1];

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int L,D,N,ans;
    scanf("%d%d%d", &L,&D,&N);
    int i, j, k, sz, doci;
    for (k=0; k<D; ++k) {
        // read doc
        scanf("%s", line);
        for( i=0; i< L; ++i) {
            // insert to index
            j = int(line[i] - 'a');
            index[i][j][0] ++;
            index[i][j][ index[i][j][0] ] = k;
        }
    }

/*
    printf("=============== index =============\n");
    for (i=0; i<L; i++) {
        printf("loc = %d\n", i);
        for (j=0; j<4; j++) {
            printf("char = %c =>", j+'a');
            for (k=0; k< index[i][j]
        }
    }
    printf("=============== index =============\n");
*/

    for (k=0; k<N; ++k) {
        // read query
        scanf("%s", line);
        // reset result
        for(i=0; i<D; ++i) result[i] = 0;
        // get each item
        char* p = line;
        i = 0;
        while ( (*p) !='\0') {
            if ( (*p) != '(' ) {
                // and query
                j = int( (*p) - 'a' );
                sz = index[i][j][0];
                // printf("i,j,sz = %d,%c,%d\n", i, *p, sz);
                for (doci = 0; doci < sz; ++doci) {
                    // printf(" == hit docid = %d\n", index[i][j][ doci+1 ]);
                    result[ index[i][j][ doci+1 ] ] ++;
                }
            }
            else if ( (*p) == '(' ) {
                // or query
                p++;
                while( (*p) != ')' ) {

                    j = int( (*p) - 'a' );
                    sz = index[i][j][0];
                    // printf("i,j,sz = %d,%c,%d\n", i, *p, sz);
                    for (doci = 0; doci < sz; ++doci) {
                        // printf(" == hit docid = %d\n", index[i][j][ doci+1 ]);
                        result[ index[i][j][ doci+1 ] ] ++;
                    }
                   
                    p++;
                }
            }
            i++;
            p++;
        }
        // count result
        ans = 0;
        for (i=0; i<D; ++i) {
            // printf(" == docid, hit = %d, %d\n", i, result[i]);
            if (result[i] == L) {
                // printf("hit docid = %d\n", i);
                ans++;
            }
        }
        printf("Case #%d: %d\n", k+1, ans);
    }
    

    return 0;
}

