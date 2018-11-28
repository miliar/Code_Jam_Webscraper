#include<iostream>
#include<cstdlib>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
    char a[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t,i,j;
    freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "A-small-attempt0.out", "w", stdout );
    cin>>t;
    cin.get();
    for(i=1;i<=t;i++)
    {
        string s;
        getline(cin,s);

        for(j=0;j<s.size();j++)
        {
            if(s[j]>96 && s[j]<123)
            s[j]=a[s[j]-97];
        }
        cout<<"Case #"<<i<<":"<<" "<<s<<endl;
    }
  return 0;


}
