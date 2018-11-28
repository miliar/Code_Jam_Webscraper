#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<fstream>
using namespace std;
int t,i,n,j;
char g[256],x;
char code[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    ifstream cin;
    ofstream cout;
    cin.open("A-small-attempt0.in");
    cout.open("A-small-attempt0.out");

    cin>>t;
    cin.get(x);
    for(i=1;i<=t;i++)
    {
        cin.getline(g,101);

        cout<<"Case #"<<i<<": ";

        n=strlen(g);
        for(j=0;j<=n-1;j++)
         if (g[j] == ' ') cout<<' ';
         else cout<<code[g[j]-'a'];
        cout<<endl;
    }
    cin.close();
    cout.close();
return 0;
}
