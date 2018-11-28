#include <iostream>
#include <vector>
#include <utility>
#include <list>
#include <string>
#include <map>

using namespace std;

inline int base(char c)
{
    int res = -1;
    switch(c)
    {
        case 'Q': res = 1; break;
        case 'W': res = 2; break;
        case 'E': res = 3; break;
        case 'R': res = 5; break;
        case 'A': res = 7; break;
        case 'S': res = 11; break;
        case 'D': res = 13; break;
        case 'F': res = 17; break;
        default: res = -1;
    }
    return res;
}

void do_it() ;

int
main()
{
    int T = 0;
    cin >> T ;
    for(int trial = 0; trial < T; ++trial)
    {
        cout << "Case #" << trial + 1 << ": " ;
        do_it();
    }
}

typedef pair<char, char> two_chars ;
void
do_it()
{
    char combine[290] ;
    bool oppose[290] ;
    for(int i = 0; i < 290; ++i){ combine[i] = 0; oppose[i] = false; }
    int C = 0, D = 0, N = 0 ;
    string input;
    char res[101] ;
    int pos = -1;

    cin >> C ;
    for(int i =0; i < C; ++i)
    {
        string s ;
        cin >> s ;
        combine[base(s[0])*base(s[1])] = s[2] ;
    }
    cin >> D ;
    for(int i =0; i < D; ++i)
    {
        string s ;
        cin >> s ;
        oppose[base(s[0])*base(s[1])] = true ;
    }
    cin >> N >> input ;
    for (int i = 0; i < N; ++i)
    {
        if ( pos < 0 )
        {
            res[++pos] = input[i] ;
        }
        else
        {
            int opposed = 0;
            // Combine
            int v = base(res[pos])*base(input[i]) ;
            if ( v > 0 )
            {
                if ( combine[v] )
                {
                    res[pos] = combine[v] ;
                    continue ;
                }
            }
            
            // Destroy
            for( int j = pos; j >= 0; --j )
            {
                int v = base(res[j])*base(input[i]) ;
                if ( v > 0)
                {
                    if (oppose[v])
                    {
                        pos = - 1;
                        opposed = 1;
                        break ;
                    }
                }
            }
            
            if (!opposed)
            {
                res[++pos] = input[i] ;
            }
        }
    }
    res[pos+1] = '\0' ;
    cout << "[" ;
    for (int i = 0; i < pos; ++i)
        cout << res[i] << ", ";
    if (pos < 0)
        cout << "]\n" ;
    else
        cout << res[pos] << "]\n";
}

