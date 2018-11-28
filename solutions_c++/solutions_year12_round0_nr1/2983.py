#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    char p[10000]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    int test;
    cin>>test;

    char str[100000];
    int n=0;
    getchar();//first char \n
    while(test--)
    {
        n++;
        gets(str);
        int i=0;
        cout<<"Case #"<<n<<": ";
        while(str[i]!='\0')
        {
            if(str[i]>=97 && str[i]<=122)
            cout<<p[str[i]-'a'];
            else cout<<" ";
            i++;
        }
        cout<<endl;

    }
    return 0;


}
