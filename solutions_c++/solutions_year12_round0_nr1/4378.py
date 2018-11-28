#include<iostream>
#include<cstring>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<vector>
#include<sstream>
#include<cctype>
using namespace std;
int main()
{
        int t;
        cin>>t;
        char table[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
        int j=1;
        cin.ignore();   
        while(t--)
        {
                string s;
                string ans="";                  
                getline(cin,s);         
                for(int i=0;i<s.size();i++)
                {
                        if(isalpha(s[i]))
                        {
                                int index=s[i]-'a';
                                char rep=table[index];
                                ans+=rep;
                        }
                        else
                                ans+=s[i];
                }
                cout<<"Case #"<<j<<": "<<ans<<endl;
                j++;
        }
        return 0;
}
