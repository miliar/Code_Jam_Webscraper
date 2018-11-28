#include <iostream>
#include <string>

using namespace std;

string search_engines[1000];
string queries[10000];

/// How many times the i'th search_engine name occurs at or after the j'th query (i,j)
int occurs[100][1001];

/// How many swaps you need to make 
int DP[1000][10000];

int N;
int S;
int Q;

int recurse(int previous_engine, int position)
{
    //cout << previous_engine << " " << position << endl;
    int mini = 100000;
    
    if(position == -1)
    {
        for(int i = 0; i < S; ++i)
        {
            if(queries[0] == search_engines[i])
                continue;
        
            mini = min(mini, recurse(i, 0));
        }
        
        return mini;
    }
    
    if(position == Q)
        return 0;
    
    if(DP[previous_engine][position] != -1)
        return DP[previous_engine][position];
    
    for(int i = 0; i < S; ++i)
    {
        if(queries[position+1] == search_engines[i])
            continue;
        
        mini = min(mini, recurse(i, position+1)+(previous_engine!=i));
    }
    
    DP[previous_engine][position] = mini;
    
    return mini;
}

int main()
{
    cin >> N >> ws;
    
    for(int i = 1; i <= N; ++i)
    {
        cin >> S >> ws;
        
        for(int j = 0; j < S; ++j)
        {
            getline(cin, search_engines[j]);
        }
        
        cin >> Q >> ws;
        
        for(int j = 0; j < Q; ++j)
        {
            getline(cin, queries[j]);
        }
        
        /// Clear DP cache
        for(int j = 0; j < S; ++j)
        {
            for(int k = 0; k < Q; ++k)
            {
                DP[j][k] = -1;
            }
        }
        
        cout << "Case #" << i << ": " << recurse(-1, -1) << endl;
    }
}

