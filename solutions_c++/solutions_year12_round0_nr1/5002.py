#include<iostream>
#include<cstring>
using namespace std;

int main()
{
char arr[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int t;
scanf("%d",&t);
char str[110],ans[110],wr[100];
gets(wr);
for(int j=1;j<=t;j++)
{
     gets(str);
     int l=strlen(str);
     for(int i=0;i<=l;i++)
     {
         if(str[i]>='a'&&str[i]<='z')   
         ans[i]=arr[str[i]-'a'];  
         else
         ans[i]=str[i];  
        //cout<<str[i]<<" "<<ans[i]<<endl;;
     }     

printf("Case #%d: %s\n",j,ans);
}

return 0;
}
