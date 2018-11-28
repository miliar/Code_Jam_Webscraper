#include<iostream>
using namespace std;
char s[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cnt=1;
    int T;
    cin>>T;
     char str[105];
     getchar();
    while(T--)
    {
              
              gets(str);
              
              printf("Case #%d: ",cnt++);
              for(int i=0;i<strlen(str);i++)
              if(str[i]>='a'&&str[i]<='z')
              cout<<s[str[i]-'a'];
              else cout<<" ";
              cout<<endl;
              
}
return 0;
}          
    
