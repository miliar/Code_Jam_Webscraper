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

        int Op = 1 ; //�ϴ�O��λ��
        int Ot = 0 ; //�ϴ�O��ʱ��
        int Bp = 1 ; //�ϴ�B��λ��
        int Bt = 0 ; //�ϴ�B��ʱ��

        int lastR = 0 ; //lastR = 0��ʾstart״̬��lastR = 'O' ��ʾ�ϴ���O��lastR = 'B'��ʾ�ϴ���B��
        int time = 0 ;  //��ʱ��

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

            //��ʱ��
            if( lastR == 0 )
            {//start״̬
                time += P ;
            }
            else if( R == lastR )
            {//���ϴ�״̬��ͬ
                time += ab( P, p ) + 1 ;
            }
            else
            {//���ϴ�״̬��ͬ

                if(ab(P , p)<=(time - t))
                {
                    time += 1 ;
                }
                else
                {
                    time += ( ab(P , p) - time + t + 1) ;
                }
            }

            //����״̬lastR������
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
