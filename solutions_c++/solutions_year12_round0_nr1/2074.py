#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<string>
#include<algorithm>
#include<stack>
#include<vector>
using namespace std;

int main()
{
    char arr[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int tc;
    cin>>tc;
    string str = "";
    getline(cin,str);
    for(int i = 1;i<=tc; i++)
    {
            getline(cin,str);
            printf("Case #%d: ",i);
            for(int j = 0;j<str.length();j++)
            {
                    if(str[j] == ' ')
                              printf(" ");
                    else
                        cout<<arr[str[j]-'a'];
            }
            printf("\n");
    }
    return 0;
}
