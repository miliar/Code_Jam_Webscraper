#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <sstream>
using namespace std;
string tonum(string s)
{
    while(s[0]=='0')s=s.substr(1);
    return s;
}    
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        string s;
        cin>>s;
        s="000000000000000000000"+s;
        next_permutation(s.begin(),s.end());
        
        cout<<"Case #"<<i+1<<": "<<tonum(s)<<endl;
    }
    
   // system("pause");
    return 0;
}
