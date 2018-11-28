#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("out.txt","w",stdout);
    string s;
    char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l',
                'b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int n;
    cin>>n;
    string c;
    getline(cin,c);
    for (int i=0; i<n; i++)
    {
        cout<<"Case #"<<i+1<<": ";
        getline(cin,s);
        for (int j=0; j<s.length(); j++)
        if (s[j]==' ') cout<<" ";
           else cout<<a[(int)s[j]-97];
        if (i!=n-1) cout<<endl;
        s.erase();
        }
     fclose(stdin);
     fclose(stdout);
    //system("pause");
    return 0;
}
