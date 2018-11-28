#include<iostream>
using namespace std;
char str[1000];
int m,n;
struct Node
{
     char str[110];
}node[10000];
int usen,usee;
struct Edge
{
     int to,next;
}edge[10000];
int pre[10000];
char in[1000];
int ins(char *str)
{
    int now=0;
    int res=0;
    for(int i=1;str[i-1];i++)
    {
         int s=0;
         while(str[i]&&str[i]!='/')
         {
             in[s++]=str[i++];
         }
      //   cout<<i<<endl;system("pause");i--;
         in[s]='\0';
      //   cout<<in<<endl;
         int p=pre[now];
         while(p!=-1)
         {
              if(strcmp(in,node[edge[p].to].str)==0)
              break;
              p=edge[p].next;
         }
    //     cout<<p<<endl;
         if(p==-1)
         {
             strcpy(node[usen].str,in);
             edge[usee].to=usen;
             edge[usee].next=pre[now];
             pre[now]=usee++;
             now=usen;
             usen++;
             res++;
         }
         else
              now=edge[p].to;
    }
    return res;
}
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
       usen=1,usee=0;
       memset(pre,-1,sizeof(pre));
       scanf("%d%d",&n,&m);
       for(int i=1;i<=n;i++)
       {
            scanf("%s",&str);
            ins(str);
       }
       int res=0;
       for(int i=1;i<=m;i++)
       {
           scanf("%s",str);
           res+=ins(str);
       }
       printf("Case #%d: %d\n",ca,res);
    }
}
    
