#include <iostream>
#include <cstring>
using namespace std;

char query [10000];

bool check (char str [])
{
    int index = 0;
    //unsigned int length = strlen (query);

    for ( unsigned int i = 0; i < strlen (str); i++ ) {
        if ( query [index] == '(' ) {
            index++;
            bool flag = false;
            while ( query [index] != ')' ) {
                if ( query [index] == str [i] )
                    flag = true;
                index++;
            }

            if ( !flag )
                return false;
        }

        else {
            if ( query [index] != str [i] )
                return false;
        }

        index++;
    }

    return true;
}

int main ()
{
    int l;
    int d;
    int n;
    int testCase = 0;

    cin >> l >> d >> n;

    char str [5002] [18];

    for ( int i = 0; i < d; i++ )
        cin >> str [i];

    while ( n-- ) {

        cin >> query;

        int count = 0;
        for ( int i = 0; i < d; i++ ) {
            if ( check (str [i]) )
                count++;
        }

        printf ("Case #%d: %d\n", ++testCase, count);

    }

    return 0;
}
