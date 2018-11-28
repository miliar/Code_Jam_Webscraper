#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#define N 30


using namespace std;

char a[N]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
string s,t;
int main(int argc, char *argv[])
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    int l,n;
    int i,j,k;
    cin>>n;
    getline(cin,s);
    for(k=1;k<=n;k++)
    {
        getline(cin,s);
        l=s.length();
        t.clear();
        for(i=0;i<l;i++)
        {
            if(s[i]>'z'||s[i]<'a')
            {
                t.push_back(' ');
            }
            else
            t.push_back(a[s[i]-'a']);
        }
        cout<<"Case #"<<k<<": "<<t<<endl;
    }
    
   // system("PAUSE");
    return 0;
}
