#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

char s[20];

char s1[20];

char tmp[20];

void int_to_char(int a,char *s)
{

    int cnt=0;
    while(a>0)
    {
        tmp[cnt++]=char(a%10+'0');
        a/=10;
    }

    for(int i=cnt-1;i>=0;i--)
       s[cnt-1-i]=tmp[i];
    s[cnt]='\0';
}

void left(char *s)
{
    int m=strlen(s);
    char tmp=s[m-1];
    for(int i=m-1;i>0;i--)
    {
         s[i]=s[i-1];


    }

    s[0]=tmp;

}


int char_to_int(char *s)
{
    int ret=0;
    for(int i=0;i<strlen(s);i++)
    {
        ret=ret*10+s[i]-'0';
    }
    return ret;
}

int main()
{
      int t,A,B;
      freopen("C-small-attempt0.in","r",stdin);
      freopen("outC.txt","w",stdout);
      scanf("%d",&t);
      for(int cas=1;cas<=t;cas++)
      {
          int cnt=0;
          scanf("%d%d",&A,&B);
          for(int i=A;i<=B;i++)
          {

              int_to_char(i,s);
              //cout<<s<<endl;

              int len=strlen(s);
              for(int j=1;j<len;j++)
                {
                     left(s);
                     //cout<<s<<endl;
                     if(s[0]=='0')
                       continue;
                     int re=char_to_int(s);
                     if(re>i&&re>=A&&re<=B)
                       cnt++;

                }

          }
          //cout<<cnt<<endl;

      printf("Case #%d: %d\n",cas,cnt);

      }
      return 0;
}
