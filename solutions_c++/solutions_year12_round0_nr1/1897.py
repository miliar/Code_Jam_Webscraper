#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <deque>
#include <sstream>
#include <cmath>

using namespace std;

string b("ynficwlbkuomxsevzpdrjgthaq");

string solve(string s)
{
    return s;
}

int main() 
{
    string line;
    getline(cin, line);
    int T = strtol(line.c_str(), 0, 10);

    for(int t=1; t <= T; t++)
    {
        getline(cin, line);
        for(int i = 0; i < (int)line.size(); i++)
            if(line[i] != ' ') line[i] = b.find(line[i]) + 'a';
        
        cout << "Case #" << t << ": " << line << endl;
    }   
    
    return 0;
}
    
