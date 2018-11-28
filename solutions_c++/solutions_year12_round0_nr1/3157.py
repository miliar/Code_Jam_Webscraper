#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
char mp[]="yhesocvxduiglbkrztnwjpfmaq";



char s[1000];

int main()
{
     //cout<<(int)('z')<<endl;
     freopen("A-small-attempt0.in","r",stdin);
     freopen("outA.txt","w",stdout);
     int cas,t;
     cas=0;
     scanf("%d",&t);
     getchar();
     while(t--)
     {
         //scanf("%s",s);
         gets(s);
         //cout<<s<<" "<<strlen(s)<<endl;
         for(int i=0;i<strlen(s);i++)
         {
             //cout<<s[i]<<endl;
             if(s[i]>='a'&&s[i]<='z')
             {
                 s[i]=mp[s[i]-'a'];
             }

         }
         printf("Case #%d: ",++cas);
         puts(s);

     }
     return 0;
}
