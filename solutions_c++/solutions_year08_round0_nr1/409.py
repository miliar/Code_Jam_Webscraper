#include<iostream>
using namespace std;
#include<algorithm>
const int MAXN = 120;
struct node
{
  char str[MAXN];
  long id;
}a[200],b[1200];

bool operator<(const node a,const node b)
{
    return strcmp(a.str,b.str)<0;
}

bool visited[1200][110];

long ans[1200][110];     

long label[1200];

long s,q;       

long dp(long depth,long id)
{
    if(depth>=q) return 0;
    
    if(visited[depth][id]) return ans[depth][id];
    
    visited[depth][id] = true;
    
    long i;
    if(id==label[depth])
    ans[depth][id] = q;
    else
    ans[depth][id] = dp(depth+1,id);
    
    for(i=0;i<id;i++)
    ans[depth][id] = min(ans[depth][id],1+dp(depth+1,i));
    
    for(i=id+1;i<s;i++)
    ans[depth][id] = min(ans[depth][id],1+dp(depth+1,i));
    
 return ans[depth][id];
}

long binarysearch(long left,long right,const char *s)
{
    long l = left,r = right,mid;
    long flag;
    while(r-l>1)
    {
         mid = (l+r)>>1;
         flag = strcmp(a[mid].str,s);
         if(!flag)
         return mid;
         else if(flag>0)
         r = mid;
         else
         l = mid;
         }
     flag = strcmp(a[r].str,s);
    if(!flag) return r;
   return l;
}
                     
    
int main()
{
    long caseamount,casenum = 1;
    long i,j;
    long opt;
    freopen("AAA.txt","w",stdout);
    scanf("%ld%*c",&caseamount);
    while(caseamount--)
    {
       scanf("%ld%*c",&s);
       for(i=0;i<s;i++)
       gets(a[i].str);
       sort(a,a+s);
       scanf("%ld%*c",&q);
       for(i=0;i<q;i++)
       gets(b[i].str);
       
       for(i=0;i<q;i++)
          label[i] = binarysearch(0,s-1,b[i].str);
       
      /* for(i=0;i<s;i++)
       printf("%s ",a[i].str);
       printf("\n");
       for(i=0;i<q;i++)
       printf("(%s %ld)  ",b[i].str,label[i]);
       printf("\n");
       */                      
       
       for(i=0;i<q;i++)
        for(j=0;j<s;j++)
        visited[i][j] = false;
        
      opt = dp(0,0);
      for(i=1;i<s;i++)
      opt = min(opt,dp(0,i));
    printf("Case #%ld: %ld\n",casenum++,opt);
}
//system("pause");

                       
    return 0;
}
