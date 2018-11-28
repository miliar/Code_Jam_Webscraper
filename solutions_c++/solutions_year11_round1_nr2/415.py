#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
int N,l[10001],d[10001],M,lenght_now=0,head[11],tail[11],similiar[10001],ans=N+1,save_point=-1,T;
vector <int> store[1025];
char str[10001][11],temp[27],block[27];
int DFS(int fst,int lst,int now,int point)
{
    if(fst>lst)
      return 0;
    //printf("%d %d",fst,lst);system("pause");
    if(fst+1==lst)
    {//printf("!");
      // printf("%d %s\n",d[fst],str[d[fst]]);
       if(save_point<point||(save_point==point&&ans>d[fst]))
         {ans=d[fst];save_point=point;}           
       return 0;
    }
    for(int k2=fst;k2<lst;k2++)
    {
       int u=1,sum=0;
       for(int k3=0;k3<l[d[k2]];k3++)
       {
           if(str[d[k2]][k3]==temp[now])
             sum+=u;    
           u*=2;
       }       
       store[sum].push_back(d[k2]);
    }
    int temp1=0,ooo=-1;
    for(int i=0;i<=1024;i++)
    {
       if(store[i].size()==lst-fst)
          ooo=i;
       for(int j=0;j<store[i].size();j++)       
       {//printf("%d,%d | ",store[i][j],i);
         d[fst+temp1] = store[i][j];
         similiar[fst+temp1] = i;   
         temp1++;   
       }
       while(store[i].size()>0)
         store[i].pop_back();
    }
    int temp2=fst;
    for(int i=fst+1;i<lst;i++)
    {
       if(similiar[i]!=similiar[i-1])
         {
          if(similiar[i-1]!=0)
            DFS(temp2,i,now+1,point);
          else
            DFS(temp2,i,now+1,point+1);
          temp2=i;
         }
    }
    if(ooo==-1)
      DFS(temp2,lst,now+1,point);
    if(ooo!=-1)
     { DFS(fst,lst,now+1,point);}
}
bool cmp(int i,int j)
{
  return l[i]<l[j];     
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int r = 1;r<=T;r++)
    {
        printf("Case #%d:",r);
        scanf("%d",&N);
        scanf("%d",&M);
        for(int i=0;i<N;i++)
          scanf("%s",str[i]),l[i] = strlen(str[i]),d[i] = i;
        sort(d,d+N,cmp);
        for(int i=0;i<=10;i++)
          head[i] = 0,tail[i] = -1;
        lenght_now = l[d[0]];
        head[lenght_now] = 0;//printf("%d",lenght_now);
        for(int i=1;i<N;i++)
        {//printf("%d ",l[d[i]]);
          if(l[d[i]]!=l[d[i-1]])
          {
             tail[lenght_now++] = i;
             head[lenght_now] = i;                            
             //printf("%d %d",head[lenght_now],tail[lenght_now-1]);
          }        
        }tail[lenght_now] = N;
        for(int i=0;i<M;i++)
        {  
          scanf("%s",temp);save_point = -1;ans=N+1;
          for(int k1=1;k1<=10;k1++)
          {
               DFS(head[k1],tail[k1],0,0);
               //printf("%d %d %d\n",head[k1],tail[k1]);
          }
          printf(" %s",str[ans]);
        }
        printf("\n");
    }
    //system("pause");
    return 0;
}
