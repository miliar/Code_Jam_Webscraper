#include <iostream>
#include <algorithm>
#include <fstream>
#define cin oku
#define cout yaz
using namespace std;
ifstream oku("A-small-attempt3.in");
ofstream yaz("A-small-attempt3.out");
int main()
{
    char p,c[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int n;
    string s;
    cin>>n;
    getline(cin,s);
    string t;
    for(int i=1;i<=n;i++)
    {
        getline(cin,t);
        cout<<"Case #"<<i<<": ";
        for(int j=0;j<t.size();j++)
            if(t[j]==' ')cout<<" ";
            else cout<<c[t[j]-'a'];
        cout<<endl;
    }
    return 0;
}
