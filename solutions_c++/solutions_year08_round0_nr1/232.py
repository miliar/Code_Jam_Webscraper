#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <sstream>

using namespace std;

int main()
{
    int N;
    string line;
    stringstream iss;
    
    getline( cin, line );
	iss.clear();
    iss.str( line );
	iss >> N;
    for(int n = 1; n <= N; n++)
    {
        set<string> s;
        int S;

        getline( cin, line );
		iss.clear();
        iss.str( line );
		iss >> S;

        vector<string> v(S);
        for(int i = 0; i < S; i++)
        {
            getline( cin, v[i] );
        }
        
        int Q;
        getline( cin, line );
		iss.clear();
        iss.str( line );
        iss >> Q;
        
        s.insert( v.begin(), v.end() );
        int res = 0;
        while( Q-- )
        {
            getline( cin, line );
            if( s.count( line ) )
                s.erase( line );
                
            if( s.size() == 0 )
            {
                res++;
                s.insert( v.begin(), v.end() );
                s.erase( line );
            }
        }
        
        cout << "Case #" << n << ": " << res << endl;
    }
}
