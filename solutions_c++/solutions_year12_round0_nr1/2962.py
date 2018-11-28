#include <iostream>
#include <cstdio>

using namespace std;

char let[] = {"yhesocvxduiglbkrztnwjpfmaq"};

int main()
{
    freopen("A.out","w",stdout);
    freopen("A.in","r",stdin);
    string g;
    int n;
    cin>>n;
    getline(cin,g);
    for(int i = 0; i < n; i++)
    {
        getline(cin,g);
        cout<<"Case #"<<i+1<<": ";
        for(int j = 0; j < g.length(); j++)
        {
            if(g[j] == ' ') { cout<<' '; continue;}
            cout<<let[toupper(g[j]) - 65];
        }
        cout<<endl;
    }
return 0;
}
