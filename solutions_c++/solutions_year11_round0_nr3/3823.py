#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <stack>
#include <set>

using namespace std;

struct node
{
    list<int> candy;
    int Sean_b;
    int Patrick_b;
    int Sean_d;
    int Patrick_d;
    
    node()
    {
        Sean_b = 0;
        Patrick_b = 0;
        Sean_d = 0;
        Patrick_d = 0;
    }    
};




list<int> separate( const char *line )
{
    int i = 0;
    list<int> result;
    string s;
    
    while( true )
    {
        if( line[i] == ' ' )
        {
            result.push_back(atoi(s.c_str()));
            s.clear();
        }
        else
        {
            s += line[i];
        }

        if( line[i] == '\n' || line[i] == 0x10 || line[i] == 0x13 )
        {
            result.push_back(atoi(s.c_str()));
            s.clear();
            break;
        }

        i++;
        
    }

    return result;
}



int main (int argc, const char * argv[])
{
    char buffer[65536];
    set<vector<int> > check;

    if( argc != 2 )
        return EXIT_FAILURE;
    
    FILE *in = fopen(argv[1],"rt");
    
    fgets( buffer, sizeof(buffer), in );
    int N = atoi(buffer);
    
    for( int i = 0; i < N; i++ )
    {
        list<int> candy;
        
        fgets( buffer, sizeof(buffer), in );
        fgets( buffer, sizeof(buffer), in );

        candy = separate( buffer );
                
        stack< node > s;
        node n;
        n.candy = candy;
        s.push(n);
        
        int best = -1;
        
        while( !s.empty() )
        {
            n = s.top();
            s.pop();

            if( n.candy.size() == 0 )
            {
                if( n.Sean_b == n.Patrick_b && n.Patrick_d != 0 )
                    if( n.Sean_d > best )
                    {
                        best = n.Sean_d;
                    }
                
                continue;
            }
            
            int x = n.candy.front();
            n.candy.pop_front();
            
            node next1 = n;
            node next2 = n;
            
            next1.Sean_b ^= x;
            next2.Patrick_b ^= x;
            next1.Sean_d += x;
            next2.Patrick_d += x;
            
            s.push(next1);
            s.push(next2);
        }
        
        if( best == -1 )
            cout << "Case #" << i + 1 << ": " << "NO" << endl;
        else
        {
            
            
            cout << "Case #" << i + 1 << ": " << best << endl;
        }
    }
    
    
    fclose(in);
    
    return 0;
}

