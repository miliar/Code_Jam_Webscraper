#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int hash[300];

char example[][400] = {
    "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv",
    "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"
};

char str[200];

int main() {
    memset ( hash, -1, sizeof ( hash ) );
    hash['z'] = 'q';
	hash['q'] = 'z';
    for ( int i = 0;example[0][i];++i ) {
        char a = example[0][i];
        char b = example[1][i];
        if ( hash[a] == -1 )
            hash[a] = b;
        else if ( hash[a] != b ) {
            printf ( "Error\n" );
            exit ( -1 );
        }
    }
    int T;
    scanf ( "%d", &T );
    gets ( str );
    for ( int t = 1; t <= T;++t ) {
        gets ( str );
        printf ( "Case #%d: ", t );
        for ( int i = 0;str[i];++i ) {
            if ( str[i] >= 'a' && str[i] <= 'z' )
                printf ( "%c", hash[str[i]] );
            else
                printf ( "%c", str[i] );
        }
        printf ( "\n" );
    }
    return 0;
}