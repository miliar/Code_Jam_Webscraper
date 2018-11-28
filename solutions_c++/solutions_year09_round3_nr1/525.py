#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <map>
using namespace std;

int main()
{
    int casenumber;
    string number;
    int numberlength;
    int different;
    unsigned long long  sum;
    unsigned long long base;
    
    map<char, int> m;
    
    cin >> casenumber;
    for(int x = 0; x < casenumber; ++x)
    {
        cin >> number;
        m.clear();
        different = 0;
        numberlength = number.length();
        
        if(numberlength == 1)
        {
            cout << "Case #" << x + 1 << ": 1" << endl;
            continue;
        }
        
        for(int i = 0; i < numberlength; ++i)
        {
            if(m[number[i]] == 0)
            {
                different += 1;
                m[number[i]] = different;
            }
        }
        
        int b = m.size();
        if(b == 1) b = 2;
        sum = 0;
        base = 1;
        for(int i = numberlength-1; i >= 0; --i, base *= b)
        {
            if(m[number[i]] == 1) sum += (base);
            else if(m[number[i]] == 2);
            else sum += (base * (m[number[i]]-1));
        }
        cout << "Case #" << x + 1 << ": " << sum << endl;
    }
            
            
        
            
        
    return 0;
}
