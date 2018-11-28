#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std ;

int integer_array[500] ;
int sum_total ;
int N ; 
bool integer_flag[500] ;
bool jisuan(int i, int sum)
{
    if( sum < 0  ) return false ;
    if( i == N ) 
    if( sum == 0 ) return true ;
    else return false ;
    if( integer_flag[i] ) 
        return jisuan(i+1,sum) ;
    if( jisuan(i+1,sum-integer_array[i]) )
    {
        cout << integer_array[i] << " " ;
        return true ;
    }
    return jisuan(i+1,sum) ;
}
bool cal(int i, int sum )
{
    if( i == N ) return false ;
    if( sum > sum_total ) return false ;
    
    if( sum && jisuan(0,sum) )
    {
        cout << endl ;
        return true ;
    }
    integer_flag[i] = true ;
    if( cal(i+1,sum+integer_array[i]) )
    {
        cout << integer_array[i] << " " ;
        return true ;
    }
    integer_flag[i] = false ;
    return  cal(i+1,sum) ;
}
int main()
{
    int T ; 
    cin >> T ; 
    for( int count_case = 0  ; count_case < T ; ++ count_case )
    {
        memset(integer_flag,false,sizeof(integer_flag));
        cin >> N ;
        sum_total = 0 ;
        for( int i = 0 ; i < N ; ++ i )
        {
            cin >> integer_array[i] ;
            sum_total += integer_array[i] ;
        }
        sum_total /= 2 ;
        printf("Case #%d:\n",count_case+1) ;
        if( !cal( 0, 0) ) cout << "Impossible" << endl ;
        else cout << endl ;
    }
    return 0 ;
}
