#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(void)
{
   string s;
   getline(cin,s);
   stringstream ss(s);
   int t;
   ss >> t;
   for (int i=1; i<=t; i++)
   {
        getline(cin,s);
        string list = "";
        int arr[300];
        for (int k=0;k<300;k++)
        {
            arr[k] = 0;
        }
        for (int k=0;k<s.length();k++)
        {
            if (list.find(s[k])==string::npos)
            {
                list = list + s[k];
            }
        }
        if (list.length()>=1)   {arr[list[0]] = 1;}
        if (list.length()>=2)   {arr[list[1]] = 0;}        
        for (int k=2;k<list.length();k++)
        {
            arr[list[k]] = k;
        }
        unsigned long long ans = 0;
        int base = list.length();
        if (base==1) { base = 2; }
        for (int k=0;k<s.length();k++)
        {
            ans *= base;
            ans += arr[s[k]];
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}
