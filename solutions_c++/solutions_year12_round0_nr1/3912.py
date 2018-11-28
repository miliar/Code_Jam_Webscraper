#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
char ch[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z',
              't','n','w','j','p','f','m','a','q'};
int main()
{
    string str;
    int ca=1;
    int n;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&n);
    getchar();
    while(n--)
    {
        getline(cin,str);
        cout<<"Case #"<<ca++<<": ";
        for(int i=0;i<str.length();i++)
        {
            if(str[i]==' ')cout<<" ";
            else cout<<ch[str[i]-'a'];
        }
        cout<<endl;
        
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
