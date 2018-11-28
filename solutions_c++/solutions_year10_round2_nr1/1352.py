#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;

struct node{
   char str[110];
   bool operator < (const node& l) const
   {
       return strcmp(str,l.str)<0;
   }
};
node st[220];
int solve(int s,int t)
{
    int len1=strlen(st[s].str);
    int len2=strlen(st[t].str);
    int len=min(len1,len2);
    int i=0;
    while(i<len)
    {
       if(st[s].str[i]!=st[t].str[i])
          break;
       i++;
    }
    int ret=0;
    if(i>=len2&&(st[s].str[i]=='/'||i>=len1))
       return 0;
    while(st[t].str[i]!='/')
       i--;
   // cout<<i<<endl;
    while(i<len2)
    {
       if(st[t].str[i]=='/')
          ret++;
       i++;
    }
    return ret;
}

int n,m;
int main(void)
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    int cas=1;
    scanf("%d",&T);
    while(T--)
    {
    scanf("%d%d",&n,&m);
    for(int i=0;i<n;i++)
       scanf("%s",st[i].str);
    for(int i=0;i<m;i++)
       scanf("%s",st[i+n].str);
   
    sort(st,st+n);
  //  sort(st+n,st+n+m);
    int ans=0;
    for(int i=n;i<n+m;i++)
    {
        int mn=0;
        int len=strlen(st[i].str);
        for(int j=0;j<len;j++)
           if(st[i].str[j]=='/')
               mn++;
        
        for(int j=0;j<i;j++)
        {
            mn=min(mn,solve(j,i));
        }
        ans+=mn;
    //    cout<<ans<<endl;
    }
     printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}

/*
0 2
/yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

8 8
/q8t9/d09pk/8id
/q4z
/1h4
/q8t9/d09pk
/1qbf4
/cjvs
/rt2
/q8t9
/vnv
/v48v/xjm0b
/v48v/cjvs/1qbf4
/v48v/cjvs/qbv4/vuu
/v48v/xjm0b/1h4
/v48v/0u5/1ve4w/d09pk/1ve4w/ngw8d
/v48v/1qbf4
/v48v/4t2cb/0u5/rt2/1h4
*/
