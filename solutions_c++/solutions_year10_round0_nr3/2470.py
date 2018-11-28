#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <ctype.h>  // isdigit(), isalnum(), isalpha()
#include <vector>
using namespace std;

bool dbg = false;

#define DBG if( dbg )
// "3 4 5" ->  { 3, 4, 5 }
// returns the array size
// size should be big enough
template <class T>
int line2arr( char* line, T* arr, int max_size )
{
    int n = 0;
    if ( line != NULL ) {
        istringstream s(line);
        T v;
        while ( s >> v ) {
            arr[n++] = v;
        }
    }
    return n;
}

template <class T>
void init_arr( T arr, int size )
{
    for( int i = 0; i < size; i++ )
    {
        arr[i] = (T) 0;
    }
}

void chomp( char *line )
{
    if ( line != 0 )
        while ( strlen(line) > 0 && line[strlen(line)-1] == '\n' )
            line[strlen(line)-1] = 0;
}

void show_arr( char* msg, int*arr, int size )
{
    if( !dbg ) return;

    printf( "%s = [ ", msg );
    for( int i = 0; i < size; i++ )
    {
    	printf( "%d ", arr[i] );
    }
    printf( "]\n" );
}

int main( int argc, char* argv[] )
{
    // freopen("sample.txt","r",stdin);
    freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
    // freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
    // freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);

    if( argc != 1 ) dbg = true;

    char line[1000];
    fgets(line,1000,stdin);
    int ncases = atoi(line);
    DBG printf( "ncases = %d\n", ncases );

    for( int iCase = 0; iCase < ncases; iCase++ )
    {
        fgets(line,1000,stdin);
        chomp(line);
        DBG printf( "Lei line. %s\n", line );
        long int arr[3];
        int n = line2arr( line, arr, 3 );
        long int R, k;
        int N;
        DBG printf( "Array has %d elements\n", n );
        R = arr[0];
        k = arr[1];
        N = (int) arr[2];

        DBG printf( "R:%ld k:%ld N:%d\n", R, k, N );
        fgets(line,1000,stdin);
        chomp(line);
        int groups[10];
        n = line2arr( line, groups, 10 );
        DBG printf( "Array has %d elements\n", n );
        if( n != N )
          printf( "Cuec!" );

        show_arr( "groups", groups, n );

        int next[10];
        int money[10];
        int sum = 0;
        for( int i = 0; i < N; i++ )
        {
            sum = groups[i];
            int j = i;

            int count = 0;
            while( count < N && sum <= k )
            {
                j++;
                if( j >= N )
                    j = 0;
                money[i] = sum;
                sum += groups[j];
                count++;
            }
            next[i] = j;
        }

        show_arr( "next  ", next, N );
        show_arr( "money ", money, N );

        // discover loop, if any
        bool visited[10] ;
        init_arr( visited, 10 );

        int loop_start = -1;
        int curr_idx = 0;

        for( int i = 0; i < N+1; i++ )
        {
            if( visited[curr_idx] == true )
            {
                loop_start = curr_idx;
                DBG printf( "Loop starts at %d\n", curr_idx );
                break;
            }
            visited[curr_idx] = true;
            curr_idx = next[curr_idx];
        }

        int loop_length = 0;
        int loop_value = 0;
        if( loop_start != -1 )
        {
            loop_length = 1;
            loop_value += money[loop_start];
            curr_idx = next[loop_start];
            while( curr_idx != loop_start )
            {
                loop_length++;
                loop_value += money[curr_idx];
                curr_idx = next[curr_idx];
            }
        }
        DBG printf("loop_length: %d\n", loop_length );
        DBG printf("loop_value: %d\n", loop_value );

        long int money_tot = 0;
        int pos = 0;
        while( R > 0 )
        {
            DBG printf( "Looping in R: %ld -- pos:%d -- money_tot:%ld\n", R, pos, money_tot );
            if( pos == loop_start )
            {
                if( R >= loop_length )
                {
                    long int times = R / loop_length;
                    money_tot += times * loop_value;
                    R %= loop_length;
                }
                else
                {
                    money_tot += money[pos];
                    R--;
                    pos = next[pos];
                }
            }
            else {
                money_tot += money[pos];
                R--;
                pos = next[pos];
            }
        }

        printf( "Case #%d: ", iCase+1 );
        printf( "%ld", money_tot );
        printf( "\n" );
    }

    return 0;
}
