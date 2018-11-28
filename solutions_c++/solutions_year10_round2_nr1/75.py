#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;

int TC = 1, T, N, M;

vector <string> parse (string s)
{
    vector <string> v;
    string next = "";
    
    for (int i = 0; i < (int) s.length (); i++)
    {
        next += s [i];
        
        if (i + 1 == (int) s.length () || s [i + 1] == '/')
        {
            v.push_back (next);
            next = "";
        }
    }
    
    return v;
}

set <string> direc;

int insert (vector <string> v)
{
    int count = 0;
    string s = "";
    
    for (int i = 0; i < (int) v.size (); i++)
    {
        s += v [i];
        count += direc.insert (s).second ? 1 : 0;
    }
    
    return count;
}

int main ()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    
    for (scanf ("%d", &T); TC <= T; TC++)
    {
        scanf ("%d %d", &N, &M);
        direc.clear ();
        int make = 0;
        char str [1000];
        
        for (int i = 0; i < N; i++)
        {
            do gets (str); while (strlen (str) == 0);
            insert (parse (str));
        }
        
        for (int i = 0; i < M; i++)
        {
            do gets (str); while (strlen (str) == 0);
            make += insert (parse (str));
        }
        
        printf ("Case #%d: %d\n", TC, make);
    }
    
    //system ("pause");
    return 0;
}
