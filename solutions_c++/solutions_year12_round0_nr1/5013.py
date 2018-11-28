#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
        int t;
        cin>>t;
        string g;
        char c[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
        getline(cin,g);
        for(int i=1;i<=t;i++)
        {
                getline(cin,g);
                cout<<"Case #"<<i<<": ";
                for(int j=0;j<g.length();j++)
                        if(g[j]==' ')
                                cout<<" ";
                        else
                                cout<<c[((int)g[j]-97)];
                cout<<"\n";
        }
        return 0;
}
