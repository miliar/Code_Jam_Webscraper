#include <iostream>

using namespace std;
const int maxn = 60;

char m[maxn][maxn];
char r[maxn][maxn], s[maxn][maxn];
int n, K;
int move[ 4 ][ 2 ] ={ {-1, -1}, {-1, 0}, {-1, 1}, {0, 1} };
void Debug( char a[][maxn] )
{
    for(int i=0; i<n; i++ ){
        for(int j=0; j<n; j++ )
            printf("%c", a[i][j]);
        cout<<endl;
    }
    cout<<"----------"<<endl;
}

bool Can( int x, int y, char ch )
{
    int cont = 0;
    for(int k=0; k<4; k++ ){
        cont = 0;
        for(int J=0; J<n; J++ ){
            int xx, yy;
            xx = x + J*move[k][0];
            yy = y + J*move[k][1];
            if( xx >=0 && xx<n && yy >=0 && yy < n ){
                if( m[xx][yy] == ch ) cont ++;
                else break;
            }
            else break;
        }
        if( cont >=K ){
//            printf("%d %d k%d has %d\n", x,y,k, cont );
//            system("pause ");
             return 1;
        }
    }

    return 0;
}

int check( )
{
    bool use[ 2 ]={};
    for(int i=0; i<n; i++ )
        for(int J=0; J<n; J++ ){
            if(  m[i][J] == 'B' && Can(i, J, 'B') )
                use[ 0 ] = 1;
            if( m[i][J] == 'R' && Can(i, J, 'R') )
                use[ 1 ] =1;

        }
    if( use[0] && use[1] ) return 2;
    if( use[0] && use[1] == 0 )  return 0;
    if( use[1]  && use[0] == 0 ) return 1;
    return 3;

}


void Rotate()
{
    memset(r, '.', sizeof(r) );
    memset(s, '.', sizeof(s) );
    for(int i= n-1; i>=0; i-- ){
        int J = n - 1 - i;
        for( int k = 0; k<n; k++ ){
            r[ k ][ J ] = m[ i ][ k ];
        }
    }

//    Debug( r );
    for(int J=0; J<n;  J++ ){
        int sno = 0;
        for( int i=n-1; i>=0; i-- ){
            if( r[i][J]!='.'  ){
                s[n-1-sno][J] = r[i][J];
                sno++;
            }
        }
    }
//    Debug(s);
    memcpy( m, s, sizeof(s) );
}
void solve( int no )
{
    Rotate();
//    Debug( m );
    int tmp = check();
    if( tmp == 0 ){
        printf("Case #%d: Blue\n", no);
    }
    else if( tmp == 1){
        printf("Case #%d: Red\n", no);
    }
    else if( tmp == 2)
        printf("Case #%d: Both\n", no);
    else
        printf("Case #%d: Neither\n", no );
}

int main()
{
    freopen("in.txt", "r", stdin );
    freopen("out.txt","w", stdout );
    int cnt;
    cin>>cnt;
    int no = 0;
    while( cnt -- ){
        memset(m, '.', sizeof(m) );
        scanf("%d %d", &n, &K );
        for(int i=0; i<n; i++ )
            scanf("%s", m[i] );
//        Debug( m );
        solve(++no );
    }
    return 0;
}
