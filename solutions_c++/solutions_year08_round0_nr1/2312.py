#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>

struct string
{
    char data[128];

    string ()
    {
    }

    string ( const string& pattern )
    {
        memcpy ( data, pattern.data, 128 );
    }

    void get_from_file ( FILE * fp )
    {
        fgets ( data, 112, fp );
    }
};

int compute_min_jumps ( int * queries, int nqueries, int nengines, int * dist )
{
    if ( nqueries == 0 )
        return 0;

    int jumps = 0;
    for ( int i = 0; i < nengines; i++ )
        dist[i] = 100000; //! Maximal value

    for ( int i = 0; i < nqueries; i++ )
    {
        if ( dist[queries[i]] == 100000 )
            dist[queries[i]] = i;
    }

    int max = dist[0];
    for ( int i = 1; i < nengines; i++ )
    {
        if ( max < dist[i] )
            max = dist[i];
    }

    if ( max == 100000 )
        jumps = 0;
    else
        jumps = 1 + compute_min_jumps ( queries + max, nqueries-max, nengines, dist );

    return jumps;
}


int main ( int argc, char * argv[] )
{
    if (argc < 2)
    {
//        print_usage ();
        return 0;
    }

    FILE * fp = fopen ( argv[1], "r" );
    if ( fp == NULL )
    {
//        print_error ( FILE_OPEN );
        return 0;
    }
    FILE * fo = fopen ( "output.txt", "w" );

    string str;

    str.get_from_file (fp);
    int total_tests = 0;
    sscanf ( str.data, "%d", &total_tests );


    for ( int test = 0; test < total_tests; test++ )
    {
        int nengines = 0;

        str.get_from_file (fp);
        sscanf ( str.data, "%d", &nengines );

        string * engines = new string [nengines];
        for ( int i = 0; i < nengines; i++ )
        {
            engines[i].get_from_file (fp);
        }

        int nqueries = 0;
        str.get_from_file(fp);
        sscanf(str.data, "%d", &nqueries);

        int * queries = new int [nqueries];
        for ( int i = 0; i < nqueries; i++ )
        {
            str.get_from_file(fp);
            int index = 0;
            for ( ; index < nengines; index++ )
            {
                if ( ! strcmp ( str.data, engines[index].data ) )
                    break;
            }
            queries[i] = index;
        }

        int * dist = new int [nengines];
        int jumps = compute_min_jumps ( queries, nqueries, nengines, dist );
        delete [] dist;
        fprintf ( fo, "Case #%d: %d\n", test+1, jumps );

        delete [] engines; delete [] queries;
    }

    fclose (fp);
    fclose (fo);

    return 0;
};
