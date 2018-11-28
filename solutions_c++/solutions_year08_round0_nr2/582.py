#include <iostream>
#include <stdlib.h>
using namespace std;

int n ,n_ , t , na , nb , i, j , train_a , ok , train_b , st,  k , auxi , ind_a , ind_b , next_t;
char aux;
int t_a[100] , t_b[100];
int hrs_a[100] , hrc_a[100] , hrs_b[100] , hrc_b[100] ;



void take_menor();
void prox_a ( int hora );
void prox_b ( int hora );


int main( int argc , char** argv )
{
    cin >> n ;
    for ( n_ = 1 ; n_ <= n ; n_++ )
    {
        memset ( (void*) t_a , 0 , 400 );
        memset ( (void*) t_b , 0 , 400 );
        cin >> t >> na >> nb;
        
        for ( i = 0 ; i < na ; i++ )
        {
            cin >> j >> aux >> k;
            hrs_a[i] = j*60 + k;
            cin >> j >> aux >> k;
            hrc_a[i] = j*60 + k;
        }

        for ( i = 0 ; i < nb ; i++ )
        {
            cin >> j >> aux >> k;
            hrs_b[i] = j*60 + k;
            cin >> j >> aux >> k;
            hrc_b[i] = j*60 + k;
        }

        for ( i = 0 ; i < na ; i++ )
        {
            k = i;
            for ( j = i+1 ; j < na ; j++ )
                if ( hrs_a[k] > hrs_a[j] )
                    k = j;
            
            //swap
            auxi = hrs_a[i];
            hrs_a[i] = hrs_a[k];
            hrs_a[k] = auxi;
            
            auxi = hrc_a[i];
            hrc_a[i] = hrc_a[k];
            hrc_a[k] = auxi;
        }

        for ( i = 0 ; i < nb ; i++ )
        {
            k = i;
            for ( j = i+1 ; j < nb ; j++ )
                if ( hrs_b[k] > hrs_b[j] )
                    k = j;
            
            //swap
            auxi = hrs_b[i];
            hrs_b[i] = hrs_b[k];
            hrs_b[k] = auxi;
            
            auxi = hrc_b[i];
            hrc_b[i] = hrc_b[k];
            hrc_b[k] = auxi;
        }

        train_a = train_b = 0;
        do {
            take_menor();

            if (( ind_a == na )||( ind_b == nb ))
            {
                if ( ind_a == na )
                    for ( i = 0 ; i < nb ; i++ )
                        if ( !t_b[i] )
                        {
                            train_b++;
                            t_b[i] = 1;
                        }

                if ( ind_b == nb )
                    for ( i = 0 ; i < na ; i++ )
                        if ( !t_a[i] )
                        {
                            train_a++;
                            t_a[i] = 1;
                        }
            }else {
                if ( hrs_a[ind_a] < hrs_b[ind_b] )
                {
                    train_a++;
                    t_a[ind_a] = 1;
                    prox_b( hrc_a[ind_a] + t );
                
                } else {
                    train_b++;
                    t_b[ind_b] = 1;
                
                    prox_a( hrc_b[ind_b] + t );
                }
            }
            
            
            ok = 1;
            for ( i = 0 ; i < na ; i++ )
                if ( !t_a[i] ) {
                    ok = 0;
                    break;
                }
            for ( i = 0 ; ( i < nb )&& ok ; i++ )
                if ( !t_b[i] ) {
                    ok = 0;
                    break;
                }
        } while ( !ok );


        cout << "Case #"<< n_ << ": " << train_a << " " << train_b << endl;
        
    }
    return 0;
}

void take_menor()
{
    ind_a = ind_b = 0;
    
    while (( t_a[ind_a] )&&( ind_a < na ))
        ind_a++;

    while (( t_b[ind_b] )&&( ind_b < nb ))
        ind_b++;

}

void prox_a ( int hora )
{
    ind_a = 0;
    while (( ind_a < na )&&(hrs_a[ind_a] < hora ))
        ind_a++;
    while (( t_a[ind_a] )&&( ind_a < na ))
        ind_a++;
    if ( ind_a < na )
    {
        t_a[ind_a] = 1;
        prox_b ( hrc_a[ind_a] + t );
    }
}
void prox_b ( int hora )
{
    ind_b = 0;
    while (( ind_b < nb )&&(hrs_b[ind_b] < hora ))
        ind_b++;
    while (( t_b[ind_b] )&&( ind_b < nb ))
        ind_b++;
    if ( ind_b < nb )
    {
        t_b[ind_b] = 1;
        prox_a ( hrc_b[ind_b] + t );
    }
}


