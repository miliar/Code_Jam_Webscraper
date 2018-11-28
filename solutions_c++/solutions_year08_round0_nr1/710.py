#include<stdio.h>
#include<map>
#include<iostream>
#include<string>

using namespace std;

int q[1001];
string flag;

int main()
{
    map<string,int> se;
    string s;
    int ncase,ccase;
    int ns,nq,n;
    int x,y,z;
    
    cin >> ncase;
    for(ccase = 1;ccase <= ncase;ccase++)
    {
        cin >> ns;
        se.clear();
        flag.erase();
        flag = "1";
        getline(cin,s);
        for(x = 1;x <= ns;x++)
        {
            getline(cin,s);
            se[s] = x;
            flag += "0";
        }
        
        cin >> nq;
        getline(cin,s);
        n = 0;
        for(x = 0;x < nq;x++)
        {
            getline(cin,s);
            q[x] = se[s];
            flag[q[x]] = '1';
            
            if(flag.find("0",0) == string::npos)
            {
                n++;
                for(y = 1;y < flag.size();y++)
                    flag[y] = '0';
                flag[q[x]] = '1';
            }
        }
        
        cout << "Case #" << ccase << ": " << n << endl;
    }
    
    return 0;
}
