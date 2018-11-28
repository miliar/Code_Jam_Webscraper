#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int N, K;
char tbl[105][105];
char res[105][105];

inline void Swap( char &a, char &b ) {
    char tmp = a;
    a = b;
    b = tmp;
}

int main() {
    int t, casN, i, j, prev, cnt;
    bool red, blue;
    
    scanf("%d", &t);
    
    for ( casN=1; casN<=t; casN++ ) {
    
        scanf("%d%d", &N, &K);
        
        for ( i=0; i<N; i++ ) {
            scanf("%s", tbl[i] );
        }
        
        for ( i=0; i<N; i++ ) {
            for ( j=0; j<N; j++ ) {
                res[j][N-1-i] = tbl[i][j];
            }
        }
        
        for ( i=0; i<N; i++ ) {//for every column
            j = N - 1;
            while ( j >= 0 && res[j][i] != '.' ) j--;
            if ( j < 0 ) continue;//full column
            prev = j;
            for ( j--; j>=0; j-- ) {
                if ( res[j][i] != '.' ) {
                    Swap( res[j][i], res[prev][i] );
                    prev--;
                }
            }
        }
        
        red = blue = false;
        
        for ( i=0; i<N; i++ ) {//check rows for 'R'
            for ( j=cnt=0; j<N; j++ ) {
                if ( res[i][j] == 'R' ) {
                    cnt++;
                    if ( cnt == K ) red = true;
                } else {
                    cnt = 0;
                }
            }
        }
        for ( i=0; i<N; i++ ) {//check rows for 'B'
            for ( j=cnt=0; j<N; j++ ) {
                if ( res[i][j] == 'B' ) {
                    cnt++;
                    if ( cnt == K ) blue = true;
                } else {
                    cnt = 0;
                }
            }
        }
        
        for ( i=0; i<N; i++ ) {//check columns for 'R'
            for ( j=cnt=0; j<N; j++ ) {
                if ( res[j][i] == 'R' ) {
                    cnt++;
                    if ( cnt == K ) red = true;
                } else {
                    cnt = 0;
                }
            }
        }
        for ( i=0; i<N; i++ ) {//check columns for 'B'
            for ( j=cnt=0; j<N; j++ ) {
                if ( res[j][i] == 'B' ) {
                    cnt++;
                    if ( cnt == K ) blue = true;
                } else {
                    cnt = 0;
                }
            }
        }
        
        for ( i=cnt=0; i<N; i++ ) {//check diagnals for 'R'
            if ( res[i][i] == 'R' ) {
                cnt++;
                if ( cnt == K ) red = true;
            } else {
                cnt = 0;
            }
        }
        for ( i=1; i<N; i++ ) {
            for ( j=cnt=0; i+j<N; j++ ) {
                if ( res[i+j][j] == 'R' ) {
                    cnt++;
                    if ( cnt == K ) red = true;
                } else {
                    cnt = 0;
                }
            }
        }
        for ( i=1; i<N; i++ ) {
            for ( j=cnt=0; i+j<N; j++ ) {
                if ( res[j][i+j] == 'R' ) {
                    cnt++;
                    if ( cnt == K ) red = true;
                } else {
                    cnt = 0;
                }
            }
        }
        for ( i=cnt=0; i<N; i++ ) {//check diagnals for 'B'
            if ( res[i][i] == 'B' ) {
                cnt++;
                if ( cnt == K ) blue = true;
            } else {
                cnt = 0;
            }
        }
        for ( i=1; i<N; i++ ) {
            for ( j=cnt=0; i+j<N; j++ ) {
                if ( res[i+j][j] == 'B' ) {
                    cnt++;
                    if ( cnt == K ) blue = true;
                } else {
                    cnt = 0;
                }
            }
        }
        for ( i=1; i<N; i++ ) {
            for ( j=cnt=0; i+j<N; j++ ) {
                if ( res[j][i+j] == 'B' ) {
                    cnt++;
                    if ( cnt == K ) blue = true;
                } else {
                    cnt = 0;
                }
            }
        }
        
        for ( i=cnt=0; i<N; i++ ) {//check reversed diagnals for 'R'
            if ( res[i][N-i-1] == 'R' ) {
                cnt++;
                if ( cnt == K ) red = true;
            } else {
                cnt = 0;
            }
        }
        for ( i=1; i<N; i++ ) {
            for ( j=cnt=0; i+j<N; j++ ) {
                if ( res[i+j][N-1-j] == 'R' ) {
                    cnt++;
                    if ( cnt == K ) red = true;
                } else {
                    cnt = 0;
                }
            }
        }
        for ( i=1; i<N; i++ ) {
            for ( j=cnt=0; i+j<N; j++ ) {
                if ( res[j][N-1-i-j] == 'R' ) {
                    cnt++;
                    if ( cnt == K ) red = true;
                } else {
                    cnt = 0;
                }
            }
        }
        for ( i=cnt=0; i<N; i++ ) {//check reversed diagnals for 'B'
            if ( res[i][N-i-1] == 'B' ) {
                cnt++;
                if ( cnt == K ) blue = true;
            } else {
                cnt = 0;
            }
        }
        for ( i=1; i<N; i++ ) {
            for ( j=cnt=0; i+j<N; j++ ) {
                if ( res[i+j][N-1-j] == 'B' ) {
                    cnt++;
                    if ( cnt == K ) blue = true;
                } else {
                    cnt = 0;
                }
            }
        }
        for ( i=1; i<N; i++ ) {
            for ( j=cnt=0; i+j<N; j++ ) {
                if ( res[j][N-1-i-j] == 'B' ) {
                    cnt++;
                    if ( cnt == K ) blue = true;
                } else {
                    cnt = 0;
                }
            }
        }
        
        printf("Case #%d: ", casN);
        if ( red && blue ) puts("Both");
        else if ( red ) puts("Red");
        else if ( blue ) puts("Blue");
        else puts("Neither");
        
    }
    
    //system("Pause");
    return 0;
}
