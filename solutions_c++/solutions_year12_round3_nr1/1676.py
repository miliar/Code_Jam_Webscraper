//
//  problem 1C-A.cpp
//  codejam
//
//  Created by Michelangelo Partipilo on 14-04-12.
//  Copyright (c) 2012. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class problemCase
{
public:
    int N;
    int nodeIncidence[1000][1000];
    string result;

    void ParseInput()
    {
        cin >> N;
        
        for (int i=0; i<N; i++)
        {
            int M = 0;
            cin >> M;
            for (int j=0; j<M; j++)
            {
                int P = 0;
                cin >> P;
                nodeIncidence[i][P-1]++;
            }
        }
    }

    problemCase()
    {
        N = 0;
        for (int i=0; i<1000; i++)
            for(int j=0; j<1000; j++)
                nodeIncidence[i][j] = 0;
        ParseInput();
        
        result = "No";
    }
    
    void PrintGraph()
    {
        for (int i=0; i<N; i++)
        {
            for (int j=0; j<N; j++)
            {
                cout << nodeIncidence[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    
    int NumberOfPaths(int i, int j)
    {
        int r = 0;

        if (nodeIncidence[i][j] > 0) r++;
       
        for (int m=0; m<N; m++)
        {
            if (m == j) continue;
            
            if (nodeIncidence[i][m] > 0)
            {
                r += NumberOfPaths(m, j);
            }
        }
        
        return r;
    }
    
    void Solve()
    {
        int i,j,k;
        
        for ( i = 0; i < N && k < 2; i++ )
        {
            for ( j = 0; j < N && k < 2; j++ )
            {
                if (i == j) continue;
                
                k = NumberOfPaths(i, j);
            }
        }

        if (k>=2)
        {
            result = "Yes";
        }
    }
    
    string Result()
    {
        return result;
    }
};

int main(int argc, const char * argv[])
{
    int T = 0;
    string dummy;
    cin >> T;
    getline(cin, dummy);
    for (int i=1; i<=T; i++)
    {
        problemCase problem;
        problem.Solve();
        cout << "Case #" << i << ": " << problem.Result() << endl;
    }
    return 0;
}

