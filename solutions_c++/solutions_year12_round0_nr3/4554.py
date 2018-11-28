//
//  problemC.cpp
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
    void ParseInput()
    {
        cin >> n >> m;
    }

    int n, m;
    int result;
    
    problemCase()
    {
        ParseInput();
        result = 0;
    }

    bool ArePair(string a, string b)
    {
        if (a.length() == 1 || b.length() == 1) return false;
        
        for (int i=0; i<a.length(); i++)
        {
            std::rotate(b.begin(), b.begin() + 1, b.end());
            if (b[0] == '0') continue;
            if (a == b) return true;
        }
        
        return false;
    }
    
    bool ArePair(int a, int b)
    {
        ostringstream strcN(ostringstream::in);
        strcN << a;
        string strN = strcN.str();
        
        ostringstream strcM(ostringstream::in);
        strcM << b;
        string strM = strcM.str();
        
        return ArePair(strN, strM);
    }
    
    void Solve()
    {
        result = 0;
        
        for (int i=n; i<= m; i++)
        {
            for (int j=i+1; j<=m; j++)
            {
                if (ArePair(i, j))
                {
                    result++;
                }
            }
        }
    }
    
    int Result()
    {
        return result;
    }
};

int main(int argc, const char * argv[])
{
    int N = 0;
    string dummy;
    cin >> N;
    getline(cin, dummy);
    for (int i=1; i<=N; i++)
    {
        problemCase problem;
        problem.Solve();
        cout << "Case #" << i << ": " << problem.Result() << endl;
    }
    return 0;
}

