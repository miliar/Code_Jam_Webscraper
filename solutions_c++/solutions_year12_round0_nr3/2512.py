//
//  main.cpp
//  GoogleCJ_2
//
//  Created by Michèle De Decker on 14/04/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <string>
#include <set>
#include <fstream>
#include <sstream>

using namespace std;

string to_string(int v);
int to_int(string s);
string move(string s);
int calcul_pairs(int n);

int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    
    set<int> paired;
    
    int T = 0;
    input >> T;
    input.ignore();
    
    for(int i = 0; i < T; i++)
    {
        int A,B, count = 0;
        string sa,sb;
        input >> A >> B;
        sa = to_string(A);
        sb = to_string(B);
        
        if(sa.length() == 1 or sb.length() == 1)
            output << "Case #" << i+1 << ": 0" << endl;
        else
        {
            for(int j = A; j < B; j++)
            {
                A = to_int(move(to_string(j)));
                while(A != j)
                {
                    if(A > j && A <= B)
                        count++;
                    A = to_int(move(to_string(A)));
                }
            }
            output << "Case #" << i+1 << ": " << count << endl; 
        }
        
    }
    
        
    return 0;
}

string to_string(int v)
{
    stringstream out;
    out << v;
    return out.str();
}

int to_int(string s)
{
    int v;
    stringstream(s) >> v;
    return v;
}

string move(string s)
{
    if(s.length() > 1)
    {
        string temp;
        temp = s[0];
        s.erase(0,1);
        s += temp;
        if(s[0] == '0')
            return move(s);
    }
    return s;
}

int calcul_pairs(int n)
{
    if(n <= 1)
        return 0;
    return n-1 + calcul_pairs(n-1);
}
