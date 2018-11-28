#include <string>
#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("c:\\codejam\\input.txt","r",stdin);
    freopen("c:\\codejam\\output.txt","w",stdout);
    int n=0,val=0;
    cin>>n;
    char c;
    char a[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    c = getchar();
    for(int i=0;i<n;i++)
    {
       if(i==0)
       cout<<"Case #"<<i+1<<": ";
      else
       cout<<"\nCase #"<<i+1<<": ";
       c = getchar();
       while(c!='\n' && c!=EOF)
       {
         if(c==32)
         {
          cout<<" ";
         }
        else
        {
         val = c - 97;
         c = val;
         c = a[val];
         cout<<c;
        }
        c = getchar();
       }
    }
    return 0;
}
