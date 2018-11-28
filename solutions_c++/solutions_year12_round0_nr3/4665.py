#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

int a , b;
vector<int> v;

int used[2000005];

void read (){

    scanf ( "%d%d" , &a , &b );
}

int fun ( int x ){
    v.clear();
    int cur = x;
    int ret =0 , k;
    while ( x ) {
        v.push_back(x%10);
        x/=10;
    }
    for ( int i = 0; i <v.size()-1; ++i ) {
        k = 0;
        for ( int j = i; j >= 0; --j ) k= k*10+v[j];
        for ( int j = v.size()-1; j > i; --j ) k= k*10+v[j];
        //printf ( "%d %d\n" , cur , k );
        if ( k > cur && k <= b && used[k] == 0  ) {
            ret++;
            used[k] ++;
        }
    }
    return ret;

}

void solve (){
    int ans = 0;
    for ( int i = a ; i<=b; ++i) {
         memset ( used , 0 , sizeof ( used) ) ;
        ans+=fun(i);
    }
    printf ( "%d\n" , ans );
}

int main (){
    int i  , t;
    scanf ( "%d" , &t );
    i = 1;

    while ( i <= t) {
            read ();if ( i <= t ) printf ( "Case #%d: " , i ) ;
            solve ();
           i++;

    }
    return 0;
}
