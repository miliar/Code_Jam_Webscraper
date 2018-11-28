#include<iostream>
#include<string>
using namespace std;
int main()
{
    //freopen("inp.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int test;
    string str;
    cin>>test;
    getchar();
    int i;
    char al[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    for(i=0;i<test;i++)
    {
        getline(cin,str);
        for(int j=0;j<str.size();j++)
        {
            if(str[j]!=' ') str[j]=al[str[j]-'a'];
        }
        cout<<"Case #"<<i+1<<": "<<str<<endl;
    }
    return 0;
}
