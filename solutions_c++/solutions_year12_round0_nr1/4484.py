#include<iostream>
#include<map>
#include<cstring>
using namespace std;
char a[30]={'y','h','e','s','o','c','v',
            'x','d','u','i','g','l','b',
            'k','r','z','t','n','w',
            'j','p','f','m','a','q'};
int main()
{
     freopen("n.txt","w",stdout);
     int t;
     char str[100+10];
     cin>>t;        
     gets(str);
     for(int i=0;i<t;i++)
     {  gets(str);   
        //gets(str); 
        //puts(str);
        int length=strlen(str);
        for(int j=0;j<length;j++)
        {
          if(str[j]<'a'||str[j]>'z')
             continue;
          str[j]=a[str[j]-'a'];
        }
       // cout<<i<<endl;
        printf("Case #%d: %s\n",i+1,str);        
     }
     return 0;
}
