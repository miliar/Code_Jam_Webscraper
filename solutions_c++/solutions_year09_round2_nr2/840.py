#include <iostream>

using namespace std;

string s;
int t;
int a[22];
int size;


int char_to_int(char ch)
{
    if ( ch == '0' ) return 0;
    else if ( ch == '1' ) return 1;
    else if ( ch == '2' ) return 2;
    else if ( ch == '3' ) return 3;
    else if ( ch == '4' ) return 4;
    else if ( ch == '5' ) return 5;
    else if ( ch == '6' ) return 6;
    else if ( ch == '7' ) return 7;
    else if ( ch == '8' ) return 8;
    else return 9;
}

/*
char int_to_char(int k)
{
    if ( k == 0 ) return '0';
    else if ( k == 1 ) return '1';
    else if ( k == 2 ) return '2';
    else if ( k == 3 ) return '3';
    else if ( k == 4 ) return '4';
    else if ( k == 5 ) return '5';
    else if ( k == 6 ) return '6';
    else if ( k == 7 ) return '7';
    else if ( k == 8 ) return '8';
    else return '9';
}
*/

void process(int k)
{
    size = s.length();
    for ( int i = 0 ; i < size ; i ++ )
        a[i] = char_to_int(s[i]);
        
    int vt = size-1;
    while ( vt > 0 && a[vt] <= a[vt-1] ) vt--;
    
    // add 0
    if ( vt == 0 ){
        a[size++] = 0;
        for ( int i = 0 ; i < size ; i ++ )
            for ( int j = i + 1 ; j < size ; j ++ ){
                if ( a[i] > a[j] ){
                    int temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        int u = 0;
        while ( a[u] == 0 ) u ++ ;
        int temp = a[0];
        a[0] = a[u];
        a[u] = temp;
        cout <<  "Case #" << k << ": ";
        for ( int i = 0 ; i < size ; i ++ ) cout << a[i];
        cout << endl;
    }
    
    else{
        vt--;
        int u = size - 1;
        while ( a[u] <= a[vt] ) u --;
        int temp = a[u];
        a[u] = a[vt];
        a[vt] = temp;
        cout <<  "Case #" << k << ": ";
        for ( int i = 0 ; i <= vt ; i ++ ) cout << a[i];
        for ( int i = size-1 ; i > vt ; i -- ) cout << a[i];
        cout << endl;
    }    
}


void load()
{
    cin >> t;
    for ( int i = 0 ; i < t ; i ++ ){
        cin >> s;
        process(i+1);
    }
}

int main()
{
    load();
    return 0;
}
