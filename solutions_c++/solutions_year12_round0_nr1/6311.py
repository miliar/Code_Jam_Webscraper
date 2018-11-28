#include <iostream>
#include <cstdio>
using namespace std;
#include <fstream>
#include <cstring>

int main()
{
    int n;
    ofstream cout ("out.txt");
    ifstream cin ("in.txt");
    cin>>n;
    char a[1000],ans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    for(int i = 0 ; i <= n ; i++)
    {
        cin.getline(a,102);
        int len = strlen(a);
        cout<<"Case #"<<i<<": ";
        for(int j = 0; j < len ; j++)
        {
            if(a[j]!=' ')
            cout<<ans[a[j]-97];

            else
            cout<<a[j];
        }
        cout<<endl;
    }
}
