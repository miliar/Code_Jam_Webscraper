#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

#include <sstream>

#include <boost/bind.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/algorithm/string.hpp>

using namespace std;

typedef boost::shared_ptr<struct tree> ptree;

struct tree
{
    tree() : p(0) {}
    double p;
    string feature; 

    ptree left, right;    
};

ptree readtree( vector<string> const& t, int & i )
{
    assert ( t[i] == "(" );
    ++i;
    
    ptree res(new tree());
    res->p = strtof(t[i].c_str(), 0);
    ++i;

    if (t[i] != ")" )
    { 
        res->feature = t[i];
        ++i;

        res->left  = readtree(t, i);
        res->right = readtree(t, i);
    }

    assert( t[i] == ")" );
    ++i;

    return res;    
}

void prepare( string & t )
{
    for ( size_t j = 0; j != t.size(); ++j )
    {
        if (t[j] == '(')
            t.insert(t.begin() + j + 1, ' '), ++j;
        else if ( t[j] == ')' )
            t.insert(t.begin() + j, ' '), ++j;
    }
}

int main()
{
    int N;
    cin >> N;

    for (int n = 0; n < N; ++n)
    {
        int L;
        cin >> L;
        
        string s;
        for (int i = 0; i != L+1; ++i)
        {
            string t;
            getline(cin, t);

            prepare(t);

            s += " ";
            s += t;
        }

        istringstream is(s);
        vector<string> tokens;
        
        while(1)
        {
            string t;
            is >> t;

            if ( t.empty() )
                break;

            tokens.push_back(t);
        }

        int id = 0;
        ptree t = readtree(tokens, id); 
        assert(id == tokens.size());

        int A;
        cin >> A;

        cout << "Case #" << (n + 1) << ":\n";
        for ( int i = 0; i != A; ++i )
        {
            int f;
            string name;
            cin >> name >> f;

            set<string> features;

            for ( int j = 0; j != f; ++j )
            {
                string t;
                cin >> t;

                features.insert(t);
            }

            ptree d = t;

            double res = 1;

            while ( d != 0 )
            {
                res *= d->p;
                
                if (d->feature.empty())
                    break;

                if (features.find(d->feature) != features.end())
                    d = d->left;
                else
                    d = d->right;
            }
            printf("%.7f\n", res);
        }

    }   
}

