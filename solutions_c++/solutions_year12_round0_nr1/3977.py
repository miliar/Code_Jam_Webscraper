#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

char map_char[]={'y','h','e','s','o','c','v',
                'x','d','u','i','g','l','b',
                'k','r','z','t','n','w',
                'j','p','f','m','a','q'};
int main()
{
 int n=0;
 ifstream cin("a.in");
 ofstream cout("a.out");
 cin>>n;
 string str;
 getline(cin,str);
 for(int i=0;i<n;i++)
 {
     getline(cin,str);
     for(int j=0;j<str.length();j++)
     {
        if(str[j]!=' ')
        {
            if(str[j]>='a'&&str[j]<='z')
            {
                char temp=str[j];
                str[j]=map_char[temp-'a'];
            }
        }
     }
     cout<<"Case #"<<i+1<<": "<<str<<endl;
 }
    return 0;
}
