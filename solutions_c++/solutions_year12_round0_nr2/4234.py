#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;



void calculation()
{   
    int n, s, p, tmp;
    
    cin >> n >> s >> p;
    
    vector<int> v;
    
    for(int i=0; i<n; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
    }
    
    int res = 0;
    int sur = 0;
    if(p == 0)
    {
        res = n;
    }
    else
    {
        int sure = 3*(p-1)+1;
        int maybe = 3*(p-2)+2;
        
        for(int i=0; i<n; i++)
        {
            tmp = v.at(i);
            if(tmp >= sure)
            {
                res++;
            }
            else if(tmp >= maybe && p > 1)
            {
                sur++;
            }
        }
        res = res + min(s,sur);
    }
    
    cout << res;
}



int main()
{
    int cases;

    cin >> cases;
    for(int i=0; i<cases; i++)
    {
        printf("Case #%d: ", i+1);
        
        calculation();
        
        cout << endl;
    }

    return 0;
}

