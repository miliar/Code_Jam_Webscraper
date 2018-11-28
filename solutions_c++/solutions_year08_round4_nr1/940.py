#include <iostream>
#include <fstream>

#include <vector>
#include <set>
#include <map>

#include <algorithm>

using namespace std;

const unsigned Count = 20000;

    unsigned ops[Count];
    bool changable[Count];
    
    bool value[Count];
        unsigned M;
    
    
int count(unsigned root, bool expect)
{
    if (value[root] == expect)
    {
        return 0;
    }
    if (root >= (M - 1) / 2)
        return -1;
        
    if (ops[root] == 1)
    {
        // And
        
        if (expect)
        {
            if ((value[root * 2 + 2] ^ value[root * 2 + 1]))
            {
                if (changable[root])
                {
                    return 1;
                }
            }

            int left = count(root * 2 + 2, true);
            int right = count(root * 2 + 1, true);
            if (!changable[root])
            {
                return left != -1 && right != -1 ? left + right : -1;
            }
            else
            {
                return (left != -1) ^ (right != -1) ? max(left, right) + 1 : 
                    (left == -1 && right == -1 ? -1 : min(min(left, right) + 1, left + right) );
            }
        }
        else
        {
            int left = count(root * 2 + 2, false);
            int right = count(root * 2 + 1, false);
            return left == -1 && right == -1 ? -1 : 
                ((left != -1) ^ (right != -1) ? max(left, right) : min(left, right));
        }
        
    }
    else
    {
        // or
        if (!expect)
        {
            if ((value[root * 2 + 2] ^ value[root * 2 + 1]))
            {
                if (changable[root])
                {
                    return 1;
                }
            }

            int left = count(root * 2 + 2, false);
            int right = count(root * 2 + 1, false);
            if (!changable[root])
            {
                return left != -1 && right != -1 ? left + right : -1;
            }
            else
            {
                return (left != -1) ^ (right != -1) ? max(left, right) + 1 : 
                    (left == -1 && right == -1 ? -1 : min(min(left, right) + 1, left + right) );
            }
        }
        else
        {
            int left = count(root * 2 + 2, true);
            int right = count(root * 2 + 1, true);
            return left == -1 && right == -1 ? -1 : 
                ((left != -1) ^ (right != -1) ? max(left, right) : min(left, right));
        }
        
    }
}
    
int main()
{
    unsigned tests;
//    ifstream cin("example.in");
    
    cin >> tests;
    for (unsigned i = 0; i < tests; ++i)
    {
        unsigned rv;
        cin >> M >> rv;
        unsigned n = 0;
        bool exp = rv != 0;
        for (;n < (M - 1) / 2; ++n)
        {
            unsigned G, C;
            cin >> G >> C;
            ops[n] = G;
            changable[n] = C != 0;
        }
        for (; n < M; ++n)
        {
            unsigned v;
            cin >> v;
            value[n] = v != 0;
        }
        
        for (n = (M - 1) / 2; n != 0;)
        {
            --n;
            value[n] = ops[n] == 0 ? (value[2 * n + 1] || value[2 * n + 2]) : (value[2 * n + 1] && value[2 * n + 2]);
        }
        
        int c = count(0, exp);
        if (c == -1)
        cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
        else
        cout << "Case #" << (i + 1) << ": " << c << endl;
    }
    
    return 0;
}

