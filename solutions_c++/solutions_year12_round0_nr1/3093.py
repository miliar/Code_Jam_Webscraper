#include <iostream>

using namespace std;


char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    int t;
    cin >> t;
    string s;
    getline(cin,s);
    for(int i=0; i<t; i++)
    {
            getline(cin,s);
            cout << "Case #" << i+1 << ": ";
            for(int j=0; j<s.length(); j++)
            {
                    if(s[j]>='a' && s[j]<='z')
                    {
                                 cout << map[s[j]-'a'];
                    }
                    else
                    {
                        cout << s[j];
                    }
            }
            cout << endl;
    }
    return 0;
}
