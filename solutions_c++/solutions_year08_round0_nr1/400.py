#include <string>
#include <map>
#include <set>
#include <cstdio>
using namespace std;

char str[1000];
map<string, int> mp;
set<string> st;

int main()
{
    int T, s, q, i;

    scanf( "%d\n", &T );
    for ( int cas = 1 ; cas <= T ; cas++ )
    {
        scanf( "%d\n", &s );
//        mp.clear();
        for ( i = 0 ; i < s ; i++ )
        {
            gets(str);
//            mp[str] = i;
        }

        int res = 0;

        scanf( "%d\n", &q );
        st.clear();
        for ( i = 0 ; i < q ; i++ )
        {
            gets(str);
            st.insert(str);
            if ( st.size() == s )
            {
                st.clear();
                st.insert(str);
                res++;
            }
        }

        printf( "Case #%d: %d\n", cas, res );
    }
    return 0;
}