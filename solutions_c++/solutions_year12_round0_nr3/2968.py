#include<iostream>
using namespace std;
int A,B;
int check(char s[],int s1)
{
   
    char temp=s[0];
    for(int i=1;i<strlen(s);i++)
    s[i-1]=s[i];
    s[strlen(s)-1]=temp;
    int s2=atoi(s);
   // cout<<"s1Ϊ"<<s1<<endl; 
   // cout<<"s2 Ϊ"<<s2<<endl;
    if(s2>=A&&s2<=B&&s2>s1)
    return 1;
    else return 0;
}
    
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cnt=1;
    cin>>T;
    char str[20];
    while(T--)
    {
              int ans=0;
              cin>>A>>B;
              for(int i=A;i<=B;i++)
              {
                      sprintf(str,"%d",i);
                      //cout<<"strΪ"<<str<<endl;
                      
                      for(int j=1;j<strlen(str);j++)
                      {if(check(str,i))
                      {ans++;
                      //cout<<i<<" "<<str<<" "<<ans<<endl;
                      }
                     }
                      }
              printf("Case #%d: %d\n",cnt++,ans);
              }
    return 0;
}
         
