#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#include <boost/bind.hpp>

using namespace std;


struct pattern
{
    static const size_t A = 26;

    pattern(string const s)
        : v(s.size() * A, 0)
    {
        int k = 0;
        for ( size_t i = 0; i != s.size(); ++i, ++k )
            if ( s[i] != '(' )
            {
                set(k, s[i]);
            }
            else
            {
                while (s[++i] != ')')
                {
                    set(k, s[i]);
                }
            }
    }

    bool match(string const& s) const
    {
        for ( int i = 0; i < s.size(); ++i )
            if (!get(i, s[i]))
                return false;

        return true;        
    }

    void set( size_t i, char c )        { v[i * A + (c - 'a')]         = 1; }
    bool get( size_t i, char c ) const  { return v[i * A + (c - 'a')] == 1; }

    std::vector<int> v;
};

int main()
{
    int L, D, N;
    cin >> L >> D >> N; 

    vector<string> v(D);

    for (int i = 0; i < D; ++i)
        cin >> v[i];

    for (int i = 0; i < N; ++i)
    {
        string s;
        cin >> s;

        pattern p(s);

        size_t k = count_if(v.begin(), v.end(), boost::bind(&pattern::match, &p, _1));
        
        cout << "Case #" << (i + 1) << ": " << k << "\n";
        
    }   
}

