#include <iostream>
#include <fstream>
#include <deque>
#include <string>
using namespace std;

typedef deque<string> collection;

istream* input = &cin;
int L = 0, D = 0, N = 0;
collection words, patterns;

class pattern
{
public:
    pattern( const string& p )
    {
        string node;
        bool selection = false;
        string::const_iterator si = p.begin();
        string::const_iterator se = p.end();
        while( si != se )
        {
            char ch = *si;
            switch( ch )
            {
            case '(':
                selection = true;
                break;
            case ')':
                selection = false;
                _nodes.push_back( node );
                node.clear();
                break;
            default:
                if( selection )
                    node.append( 1, ch );
                else
                    _nodes.push_back( string( 1, ch ) );
                break;
            }
            ++si;
        }
    }

    bool apply( const string& word ) const
    {
        collection::const_iterator ni = _nodes.begin();
        collection::const_iterator ne = _nodes.end();
        string::const_iterator si = word.begin();
        string::const_iterator se = word.end();
        while( ni != ne && si != se )
        {
            const string& chpat = *ni;
            char ch = *si;
            if( chpat.find( ch ) == string::npos )
                return false;
            ++ni;
            ++si;
        }

        if( ni != ne || si != se )
            return false;

        return true;
    }

private:
    collection _nodes;
};

int main(int argc, char** argv)
{   
    ifstream ifile;
    if( argc > 1 )
    {
        ifile.open( argv[1], ios::in );
        input = &ifile;
    }

    (*input) >> L >> D >> N >> ws;

    int dt = D;
    while( dt-- )
    {
        string word;
        (*input) >> word >> ws;
        words.push_back( word.substr( 0, L ) );
    }

    int dn = N;
    while( dn-- )
    {
        string pattern;
        (*input) >> pattern >> ws;
        patterns.push_back( pattern );
    }

    collection::const_iterator pi = patterns.begin();
    collection::const_iterator pe = patterns.end();
    int count = 1;
    while( pi != pe )
    {
        const string& p = *pi;
        pattern pat( p );

        collection::const_iterator wi = words.begin();
        collection::const_iterator we = words.end();
        int applied = 0;
        while( wi != we )
        {
            const string& word = *wi;
            if( pat.apply( word ) )
                ++applied;
            ++wi;
        }

        cout << "Case #" << count << ": " << applied << endl;

        ++count;
        ++pi;
    }

	return 0;
}
