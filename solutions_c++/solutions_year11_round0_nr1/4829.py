#include <cstdio>
#include <vector>
#define mod(x) (((x)<0)?(-(x)):(x))
#define max(x,y) ((x)>(y)?(x):(y))
using namespace std;

char robot[100];
int move[100];
int omove[100];
int bmove[100];

int main() {
    int T;
    scanf( "%d", &T );
    for( int ii=1; ii<=T; ii++ ) {
        int m, pos[] = { 1,1 } , total=0, o=0,b=0, num;
        char ch[2];
        scanf( "%d", &m );
        for(int i=0; i<m; i++ ) {
            scanf( "%s%d", ch, &num );
            robot[i] = ch[0];
            move[i] = num;
            if( ch[0] == 'O' ) omove[o++] = num;
            else bmove[b++] = num;
        }
        int i=0,oo=0,bb=0,flag=0,movedo=0,movedb=0;
        while( i<m ) {

            //printf( "O= %d\tB=%d\n",pos[1],pos[0] );

            // process orange
            if(omove[oo]) {
                if(pos[1]==omove[oo]) {
                    movedo=1;
                }
                else if(pos[1]>omove[oo]){
                    pos[1]--;
                }
                else
                    pos[1]++;
            }

            // process blue
            if( bmove[bb] ) {
                if(pos[0]==bmove[bb]) {
                    movedb=1;
                }
                else if(pos[0]>bmove[bb]) {
                    pos[0]--;
                }
                else
                    pos[0]++;
            }

            if( movedo || movedb ) {
                flag=0;
                if( movedo && robot[i]=='O' ) {
                    oo++;
                    movedo = 0;
                    flag++;
                }
                if( movedb && robot[i]=='B' ) {
                    bb++;
                    movedb = 0;
                    flag++;
                }
                if(flag) i++;

                if( flag==2 && omove[oo-1]==bmove[bb-1] )
                    total++;
            }

            total++;
        }
        printf( "Case #%d: %d\n", ii, total );
    }
    return 0;
}
