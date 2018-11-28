#include <stdio.h>
#include <string.h>
#include <string>
#include <map>
using namespace std;

map< pair< int , int > , bool > m;

int main ()
{
    FILE *in = fopen ("C.in","r");
    FILE *out = fopen ("C.out","w");

    int t;
    int k = 1;
    int a,b;

    fscanf (in,"%d",&t);

    while( t -- )
    {
        int ret = 0 , num;
        char c[10];
        string s;
        m.clear();

        fscanf (in,"%d %d",&a,&b);

        for (int i=a; i<=b; i++)
        {
            sprintf (c,"%d",i);
            s = c;

            for (int j=0; j<s.size(); j++)
            {
                if (s.size() == 1)
                    break;

                string s1 = s.substr( 0,j+1 );
                string s2 = s.substr( j+1 );
                string f = s2 + s1;

                if (s2[0] == '0' || s1.size() == 0 || s2.size() == 0)
                    continue;

                sscanf (f.c_str(),"%d",&num);

                if (num < a || num > b || num == i)
                    continue;

                int A = min( num , i );
                int B = max( num , i );

                bool r = m[ make_pair( A,B ) ];

                if (r == 0)
                {
                    m[ make_pair( A,B ) ] = 1;
                    ret ++;
                }
            }
        }

        fprintf (out,"Case #%d: %d\n",k,ret);
        k ++;
    }
}
