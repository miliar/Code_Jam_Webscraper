#include<iostream>
using namespace std;
long long sum;
const int MAXN = 250;

char str[MAXN];
long len;
long long cnt;

long a[3]={1,-1};


struct node
{
   long pos,flag;
}queue[MAXN<<1];
long queuetail;       

inline long long getval(long i,long j)
{
  long long sum = 0,k;
  for(k=i;k<j;k++)
   sum = sum*10+(str[k]-'0');
 return sum;
}

inline bool bound()
{
   long i;
   long long sum = 0,temp;
   for(i=1;i<queuetail;i++)
   {
     temp = getval(queue[i-1].pos,queue[i].pos);
     sum += queue[i].flag*temp;
    }
 if(sum%2==0)
 return true;
 if(sum%3==0)
 return true;
 if(sum%5==0)
 return true;
 if(sum%7==0)
 return true;
return false;
}
  
                            
    
      
void dfs(long depth)
{
   if(depth==len)
   {
      if(bound())
      cnt++;
     long i;
   //  for(i=0;i<queuetail;i++)
   //  printf("%ld %ld   ",queue[i].pos,queue[i].flag);
    // printf("\n");
      
     return;
    }
   
   node temp;
   long i,j;
   if(!depth)
   {
   
   for(i=depth+1;i<=len;i++)
    for(j=0;j<1;j++)
    {
      temp.pos = i;
      
      temp.flag = a[j];
      
      queue[queuetail++] = temp;
      
      dfs(i);
                               
      queuetail--;
      }
      }    
   else
   {
   for(i=depth+1;i<=len;i++)
    for(j=0;j<2;j++)
    {
      temp.pos = i;
      
      temp.flag = a[j];
      
      queue[queuetail++] = temp;
      
      dfs(i);
                               
      queuetail--;
      }
   }
               
      
}
      
int main()
{
    long caseamount,casenum = 1;
    node temp;
    freopen("B.txt","w",stdout);
    
   scanf("%ld%*c",&caseamount);
   while(caseamount--)
  // while(true)
    {
       gets(str);
       len = strlen(str);
       
       queuetail = 0;
       temp.pos = 0;
       queue[queuetail++] = temp;
       cnt = 0;
       dfs(0);                 
      printf("Case #%ld: %I64d\n",casenum++,cnt);
            
     }  
    // system("pause");
                     
    return 0;
}
