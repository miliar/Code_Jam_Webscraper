#include<iostream>
#include<string>

using namespace std;

int main(void){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    bool ok[ 101 ][2];
    int trp[101];
    int cannotbesup[ 101 ];
    int T,S,N,P;
    scanf("%d",&T);
    for( int c = 1; c <= T; c++ ){
        scanf("%d%d%d",&N, &S, &P );
        
        fill( cannotbesup, cannotbesup+101, 0 );
        for( int j = 1; j <= N; j++ ){
            scanf("%d",&trp[j]);
            
            
            switch( trp[j] % 3 ){
                case 0:
                    if( trp[j] == 0 ){
                        cannotbesup[j] = 1;
                        ok[j][0] = (0 >= P);
                        ok[j][1] = (0 >= P);
                    }else{
                        int temp = trp[j]/3+1;
                        ok[j][0] = (temp >= P );
                        ok[j][1] = (temp-1>=P );
                    }
                    break;
                case 1:
                    if( trp[j] == 1 ){
                        cannotbesup[j] = 1;
                        ok[j][0] = (1 >= P);
                        ok[j][1] = (1 >= P);
                    }else{
                        int temp = trp[j]/3+1;
                        ok[j][0] = (temp >= P );
                        ok[j][1] = (temp >= P );
                    }
                    break;
                case 2:{
                    int temp = trp[j]/3+2;
                    ok[j][0] = ( temp >= P );
                    ok[j][1] = ( temp-1>=P );
                    break;}
                default: break;
            }
        }
        //for( int j = 1; j <= N; j++ )
          //  cout << ok[j][0] << ' ' << ok[j][1] << endl;
        int cnt = 0;
        for( int j = 1; j <= N ; j++ ){
            if( cannotbesup[j] ){
                if( ok[j][1] ) cnt++;
                continue;
            }
            if( ok[j][0] && ok[j][1] ) cnt++;
            if( ok[j][0] == true && ok[j][1] == false && S > 0)
                cnt++,S--;
            
        } 
        printf("Case #%d: %d\n", c, cnt );
    }
    //system("pause");
    return 0;
}
