#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }

struct Time
{
    string s_time;
    int hour, minute;

    bool operator == ( const Time & T ) const { return ( this->hour == T.hour && this->minute == T.minute ); }
    bool operator != ( const Time & T ) const { return !( *this == T ); }
    bool operator < ( const Time & T ) const
    {
        if ( this->hour != T.hour ) return ( this->hour < T.hour );
        return ( this->minute < T.minute );
    }
    bool operator <= ( const Time & T ) const
    {
        if ( this->hour != T.hour ) return ( this->hour < T.hour );
        return ( this->minute <= T.minute );
    }
    Time operator + ( int T )
    {
        Time res = *this;
        res.hour += (res.minute + T) / 60;
        res.minute = (res.minute + T) % 60;
        if ( res.hour < 10 ) res.s_time = "0" + a2s(res.hour) + ":";
        else res.s_time = a2s(res.hour) + ":";
        if ( res.minute < 10 ) res.s_time += "0" + a2s(res.minute);
        else res.s_time += a2s(res.minute);
        return res;
    }

    Time( string s ) : s_time(s) { sscanf( s.c_str(), "%d:%d", &hour, &minute ); }
};

struct Trip
{
    char init;
    Time begin, end;

    bool operator < ( const Trip & T ) const
    {
        if ( this->begin == T.begin ) return ( this->end < T.end );
        return ( this->begin < T.begin );
    }

    Trip( char c, string s, string t ) : init(c), begin(s), end(t) {}
};

int main()
{
    char c;
    int N, T, NA, NB, A, B, asw;
    string s, t;

    cin >> N;

    for ( int n = 1; n <= N; n++ )
    {
        vector<Trip> v;
        c = 'A';
        A = B = 0;

        cin >> T;
        cin >> NA >> NB;

        for ( int i = 0; i < NA + NB; i++ )
        {
            if ( i >= NA ) c = 'B';
            cin >> s >> t;
            Trip trip( c, s, t );
            v.push_back(trip);
        }

        sort( v.begin(), v.end() );

        vector<Time> va, vb;

        for ( unsigned int i = 0; i < v.size(); i++ )
        {
            c = v[i].init;

            if ( c == 'A' )
            {
                if ( va.empty() ) { A++; }
                else if ( va[0] <= v[i].begin ) { va.erase(va.begin()); }
                else { A++; }
                vb.push_back(v[i].end + T);
            }
            else if ( c == 'B' )
            {
                if ( vb.empty() ) { B++; }
                else if ( vb[0] <= v[i].begin ) { vb.erase(vb.begin()); }
                else { B++; }
                va.push_back(v[i].end + T);
            }

            sort( va.begin(), va.end() );
            sort( vb.begin(), vb.end() );
        }
        cout << "Case #" << n << ": " << A << " " << B << endl;
    }

    return 0;
}
