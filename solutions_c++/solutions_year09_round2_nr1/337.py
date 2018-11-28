# include <iostream>
# include <vector>

using namespace std;

int test;

struct node
{
    int left;
    int right;
    double num;
    string feature;

    node( int a = 0, int b = 0, double c = 0, string d = "" )
        : left( a ), right( b ), num( c ), feature( d ) { };
};

int l;
int line;

int nxt;
node tree[ 1000 ];

void get( int father )
{
    string str;
    int p, sz;
    bool ok = false;

    while ( line < l )
    {
        line++;
        getline( cin, str );

        p = 0;
        sz = str.size();

        while ( p < sz && !( str[ p ] >= '0' && str[ p ] <= '9' ) ) p++;

        if ( p < sz )
        {
            ok = true;
            break;
        }
    }

    if ( !ok )
        return;

    double num = str[ p ] - '0';
    double with = 10;
    p += 2;

    while ( p < sz && ( str[ p ] >= '0' && str[ p ] <= '9' ) )
    {
        num = num + ( str[ p ] - '0' ) / with;
        with *= 10;
        p++;
    }

    string feature = "";
    while ( p < sz && !( str[ p ] >= 'a' && str[ p ] <= 'z' ) ) p++;

    while ( p < sz && ( str[ p ] >= 'a' && str[ p ] <= 'z' ) )
        feature += str[ p++ ];

    if ( father > -1 )
    {
        if ( tree[ father ].left == 0 )
            tree[ father ].left = nxt;
        else
            tree[ father ].right = nxt;
    }

    int qwe = nxt;
    tree[ nxt ] = node( 0, 0, num, feature );
    nxt++;

    if ( feature == "" )
        return;

    get( qwe );
    get( qwe );
}

int main()
{
    scanf( "%d", &test );

    for ( int testnum = 1; testnum <= test; testnum++ )
    {
        nxt = 0;
        line = 0;
        scanf( "%d\n", &l );
        get( -1 );

        string qwert;
        for ( ; line < l; line++ )
            getline( cin, qwert );

        printf( "Case #%d:\n", testnum );

        scanf( "%d", &l );
        for ( int line = 0; line < l; line++ )
        {
            string animal;
            cin >> animal;
            vector< string > q;

            int d;
            scanf( "%d", &d );

            q.clear();
            for ( int i = 0; i < d; i++ )
            {
                string sqw;
                cin >> sqw;

                q.push_back( sqw );
            }

            double p = 1.0;
            int pos = 0;
            while ( 1 )
            {
                p *= tree[ pos ].num;

                if ( tree[ pos ].feature == "" )
                    break;

                bool f = false;
                for ( int j = 0; j < d && !f; j++ )
                    if ( tree[ pos ].feature == q[ j ] )
                        f = true;

                if ( !f )
                    pos = tree[ pos ].right;
                else
                    pos = tree[ pos ].left;
            }

            printf( "%.7lf\n", p );
        }
    }
}
