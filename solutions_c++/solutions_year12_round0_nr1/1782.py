#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<list>
#include<queue>
#include<stack>
#include<cstdlib>
#include<sstream>

using namespace std;

char data[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

void filld(int j,string a)
{
    int n = a.length();
    cout<<"Case #"<<j<<": ";
    for(int i=0; i<n; i++)
    {
        if(a.at(i)!=' ')
            cout<<data[a.at(i)-'a'];
        else
            cout<<" ";
    }
    cout<<endl;
}
int main()
{
    int t;
    scanf("%d",&t);
    //  fflush(stdin);
    string a;
    getline(cin,a,'\n');
    for(int i=1; i<=t; i++)
    {
        getline(cin,a,'\n');
        //cout<<a<<"\n";
        filld(i,a);
    }

    return 0;
}



