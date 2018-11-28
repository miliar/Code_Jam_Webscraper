#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std ;

int ab(int x , int y)
{
    if( x > y)
        return x - y ;
    else
        return y - x ;
}


int main()
{
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout) ;

    int T ;
    cin >> T ;
    for ( int r = 1 ; r <= T ; ++ r)
    {
        int N ;
        cin >> N ;

        int Op = 1 ; //上次O的位置
        int Ot = 0 ; //上次O的时刻
        int Bp = 1 ; //上次B的位置
        int Bt = 0 ; //上次B的时刻

        int lastR = 0 ; //lastR = 0表示start状态；lastR = 'O' 表示上次是O，lastR = 'B'表示上次是B。
        int time = 0 ;  //总时间

        while ( N -- )
        {

            char R ;
            int P ;
            cin >> R ;
            cin >> P ;

            int p , t ;
            if ( R == 'O')
            {
                p = Op ;
                t = Ot ;
            }
            else
            {
                p = Bp ;
                t = Bt ;
            }

            //求时间
            if( lastR == 0 )
            {//start状态
                time += P ;
            }
            else if( R == lastR )
            {//与上次状态相同
                time += ab( P, p ) + 1 ;
            }
            else
            {//与上次状态不同

                if(ab(P , p)<=(time - t))
                {
                    time += 1 ;
                }
                else
                {
                    time += ( ab(P , p) - time + t + 1) ;
                }
            }

            //更新状态lastR、参数
            lastR = R ;
            if ( R == 'O')
            {
                Op = P ;
                Ot = time ;
            }
            else
            {
                Bp = P ;
                Bt = time ;
            }

        }
        cout << "Case #" << r << ": " << time << endl ;
    }
    return 0 ;
}
