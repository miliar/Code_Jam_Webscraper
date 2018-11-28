#include<iostream>
using namespace std;
#include<queue>
const int MAXN = 2000;
long a[MAXN],p,k,l;
long solve()
{
    priority_queue<long>Q;
    long i,j=1,sum=0,c;
    while(!Q.empty())
     Q.pop();
    for(i=0;i<l;i++)
     Q.push(a[i]);
    
    i = 1; 
    while(i<=p&&!Q.empty())
    {
         for(j=c=0;j<k&&!Q.empty();j++)                    
         {
            c += Q.top();
            Q.pop();
            }
     sum += c*i;
    i++;
   }
 return sum;
}
                                                         
      
int main()
{
    freopen("A.txt","w",stdout);
    long i,caseamount,casenum = 1;
    scanf("%ld",&caseamount);
    
    while(caseamount--)
    {
       scanf("%ld%ld%ld",&p,&k,&l);
       
       for(i=0;i<l;i++)
       scanf("%ld",&a[i]);
      
      printf("Case #%ld: %ld\n",casenum++,solve());
                 
    }
       
   // system("pause");
               
    return 0;
}

