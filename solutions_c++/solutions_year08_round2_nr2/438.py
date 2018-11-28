#include<iostream>
using namespace std;
const int MAXN = 1200;
long set[MAXN],A,B,P;
long prime[MAXN],cnt;
bool v[MAXN],visited[MAXN];

void fun()
{
    long i,j;
    cnt = 0;
    
    for(i=2;i<=1000;i++)
     if(!v[i])
     {
     prime[cnt++] = i;
     for(j=i<<1;j<=1000;j += i)
      v[j] = true;
      }
  
  //for(i=0;i<cnt;i++)
 // printf("%ld ",prime[i]);
 //printf("\n");
}
                   
     
void initset()
{
   long i;
   for(i=A;i<=B;i++)
   set[i] = i;
}

long findset(const long x)
{   
   long i,j,k;
   for(i=x;set[i]!=i;i=set[i]);
   
   for(j=x;j!=i;j=k)
   {
      k = set[j];
      set[j] = i;
   }
 return i;
}

inline void unionset(const long x,const long y)
{
     set[x] = y;
}

long solve()
{
    long long i,j,k,p;
    long low;
    long setx,sety,setz;
    long sum=B-A+1;
    
    for(k=0;k<cnt;k++)
     if(prime[k]>=P)
     {
        low = k;
        break;
        }
   //   printf("%ld %ld\n",low,prime[low]);
        
                      
  /*  for(i=A;i<=B;i++)
    {
      
                      
      for(j=low;j<cnt&&i*prime[j]<=B;j++)
       for(k=i*prime[j];k<=B;k *= prime[j])
       {
           setx = findset(k/prime[j]);
           sety = findset(k);
           if(setx!=sety)
           unionset(sety,setx);
       }
    }*/
    
    for(i=A;i<=B;i++)
     for(j=i+1;j<=B;j++)
     {
       for(k=low;prime[k]<=i&&k<cnt;k++)
        if(i%prime[k]==0&&j%prime[k]==0)
        {
           setx = findset(i);
           sety = findset(j);
           
          /* for(p=A;p<=B;p++)
           {
              setz = findset(p);
              if(setz==sety)
              unionset(p,setx);
           }
           */                
           
           if(setx!=sety)
           {
           unionset(sety,setx);
           sum--;
           }
           
           }
           }
                  
                                                           
   //for(i=A;i<=B;i++)
  //  visited[i] = false;
    
  /* for(i=A;i<=B;i++)
   {
    setx = findset(i);
    set[i] = setx;
   }                 
   */
 /*  for(i=A,sum = 0;i<=B;i++)                                                           
   {
        setx = findset(i);
        if(!visited[setx])
        {
           sum++;
           visited[setx] = true;
           }
   }*/
 return sum;
}                                                

int main()
{
    freopen("B.txt","w",stdout);
    fun();
    long caseamount,casenum = 1;
    long ans;
    scanf("%ld",&caseamount);
    while(caseamount--)
    {
        scanf("%ld%ld%ld",&A,&B,&P);
        initset();
        
        ans = solve();
        
        printf("Case #%ld: %ld\n",casenum++,ans);
        }
   
   
 //  system("pause");
                         
    return 0;
}
