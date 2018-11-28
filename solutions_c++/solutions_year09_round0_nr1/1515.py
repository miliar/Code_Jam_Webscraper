#include <iostream>
#include <vector>

bool match( const std::string &reg, const std::string &word );

int main()
{
    freopen("in", "r", stdin );
    freopen("out", "w", stdout );
    int l, d, n;
    scanf("%d%d%d", &l, &d, &n );
    std::vector< std::string > words( d );
    std::string reg_exp;
    for( int i = 0; i < d; ++i )
        std::cin >> words[i];
    for( int i = 0; i < n; ++i )
    {
        std::cin >> reg_exp;
        int counter = 0;
        for( int j = 0; j < d; ++j )
            if( match( reg_exp, words[j] ) )
                ++counter;
        printf("Case #%d: %d\n", i+1, counter);
    }
    return 0;
}

/* tells if word match with reg */
bool match( const std::string &reg, const std::string &word )
{
    for( int i = 0, j = 0; i < word.size(); ++i )
    {
        if( reg[j] == '(' ) /* search for any between ( and ) */
        {
            bool did = false;
            while( reg[j] != ')' )
            {
                if( !did && reg[j] == word[i] )
                    did = true;
                ++j;
            }
            if( !did )
                return false;
        }
        else if( reg[j] != word[i] ) /* must match the character */
            return false;
        ++j;
    }
    return true;
}
