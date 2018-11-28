#include <iostream>
#include<string.h>
#include<stdio.h>
using namespace std;


int main()
{
    int i,t,k;
    char str[105];

freopen ("out.txt","w",stdout);
freopen("in.txt","r",stdin);

    char arr[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    scanf("%d",&t);
    gets(str);
    k=1;
    while(t--)
    {
        gets(str);
        cout<<"Case #"<<k<<": ";
        for(i=0;i<strlen(str);i++)
        {
            if(str[i]<'a' || str[i]>'z')
                cout<<str[i];
            else
                cout<<arr[(str[i] - 97)];
        }
        cout<<"\n";

        k++;
    }

    return 0;

}
