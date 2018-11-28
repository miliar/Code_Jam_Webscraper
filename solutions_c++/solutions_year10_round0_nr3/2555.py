#include <stdio.h>
#include <string.h>
#define MAXN 1010
int r,k,n;
int data[1010];

struct Node{
       int next;
       int cal;       
}cnt[MAXN];
int hash[MAXN];
long long menoy[MAXN];

void CanCarryFrom( int x ){
     int i=x,sum=0;
     for(int j=0 ; j<n ;j++)
     {
        
         if(sum+data[i]>k)break;  
         sum += data[i];    
          i = (i+1)%n;
     }
     cnt[x].next = i;
     cnt[x].cal = sum;
};

int main()
{
    int ka=1,kase;
 //   freopen("g3.out","w",stdout);
    scanf("%d", &kase);
    while( ka<=kase){
           scanf("%d%d%d",&r,&k,&n);
           for(int i=0 ;i<n ;i++)       
                   scanf("%d", &data[i]);
           for(int i=0 ; i<n ; i++)
                   CanCarryFrom( i );
           int st=0,j;
           long long ans=0;
           memset(hash , -1 , sizeof(hash));
           
           for( j=0 ; j<r  ; j++)
           if(hash[st]<0){
                   hash[st]=j;
                   menoy[ st ] = ans;
                   ans += cnt[st].cal;
                   
                   st = cnt[st].next;
           }
           else break;
           r -= j;
           int tmp = j - hash[st];
           ans += ((int)(r/tmp))* ( ans - menoy[st] );
           r %= tmp;
           
           while(r--)
           {
              ans += cnt[st].cal;
              st =  cnt[st].next;          
           }
           
           printf("Case #%d: %d\n", ka++,ans );
    }
    return 0;    
}
