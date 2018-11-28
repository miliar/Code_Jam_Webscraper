#include<stdio.h>
#include<iostream>
#include<string>

using namespace std;

int main()
{
    int ncase,ccase;
    string P,Pb,O;
    int nc,ns;
    int x,y,z;
    
    cin >> ncase;
    for(ccase = 1;ccase <= ncase;ccase++)
    {
        P = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000";
        Pb = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000";
        O = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000";
        
        cin >> nc >> ns;
        for(x = 0;x < ns;x++)
        {
            for(y = 0;y < ns;y++)
            {
                if(P[y] == '1')
                {
                    if(O[y] == '1')O[y] = '0';
                    else O[y] = '1';
                }
            }
            P = Pb;
            for(z = 0;z <= ns;z++)
            {
                if(O[z] == '1')
                {
                    P[z + 1] = '1';
                }
                else break;
            }
        }
        
        cout << "Case #" << ccase << ": ";
        if(P[nc] == '0') cout << "OFF" << endl;
        else if(P[nc] == '1') cout << "ON" << endl;
    }
    
    while(getchar()!=EOF);
    return 0;
}
