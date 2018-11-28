#include <iostream>
#include <vector>
//#include <map>
//#include <set>
#include <string>

using namespace std;

long long read_n( istream& is )
{
        long long n;
        is >> n;
        string s;
        getline( is, s);
        return n;
}

long long doit( const string& s, const vector<long long>& v )
{
        long long n = s.length();
#if 0
        for( long long i = 0 ; i < n ; i++ ) {
                cerr << long long(s[i]-'0');
                switch(v[i]){
                case 1: cerr << '+'; break;
                case 2: cerr << '-'; break;
                }
        }
        cerr << endl;
#endif

        bool plus = true;

        long long k = 0;
        long long m = 0;
        for( long long i = 0 ; i < n ; i++ ) {
                m *= 10;
                m += s[i] - '0';
                if( v[i] != 0 ) {
                        if( plus ) {
                                k += m;
                        } else {
                                k -= m;
                        }
                        m = 0;
                        if( v[i] == 1 ) {
                                plus = true;
                        } else {
                                plus = false;
                        }
                }
        }

        if( k == 0 ) {
                return 1;
        }
        if( k % 2 == 0 || k % 3 == 0 || k % 5 == 0 || k % 7 == 0 ) {
                return 1;
        }
        return 0;
}

long long doit0( const string& s, vector<long long> v )
{
        if( (long long)(v.size()) == (long long)(s.length()) - 1 ) {
                v.push_back( 1 );
                return doit( s, v );
        }

        long long m = 0;
        for( long long k = 0 ; k < 3 ; k++ ) {
                v.push_back( k );
                m += doit0( s, v );
                v.pop_back();
        }
        return m;
}

int main(long long,char**)
{
        long long N = read_n( cin );
        for( long long i = 0 ; i < N ; i++ ) {
                string s;
                cin >> s;
                long long l = s.length();
                
                vector<long long> v;
                long long m = doit0( s, v );
                cout << "Case #" << (i+1) << ": " << m << endl;
        }

        return 0;
}
