#include<iostream>
using namespace std;
char s[6000],s1[6001][6001];
int main()
{
    int a,b,c,j,k,m,i,count,ca=1,flag;
    bool arr[27][16];
    cin>>a>>b>>c;
    for(i=0;i<b;i++) cin>>s1[i];
    for(i=0;i<c;i++)
    {
       for(j=0;j<27;j++)
         for(k=0;k<16;k++)
           arr[j][k]=0;
       cin>>s;
       m=1;
       for(j=0;j<strlen(s);j++)
       {
          if(s[j]=='(')
          {
            while(s[++j]!=')') arr[int(s[j])-97][m]=1;
            m++;
          }
          else arr[int(s[j])-97][m++]=1;
       }
       count=0;
       for(j=0;j<b;j++)
       {
           flag=1;
           for(k=0;k<strlen(s1[j]);k++) 
              if(arr[int(s1[j][k])-97][k+1]==0) {flag=0;break;}
           if(flag==1) count++;
       }
       cout<<"Case #"<<ca++<<": "<<count<<"\n";
    }
    return 0;
}
