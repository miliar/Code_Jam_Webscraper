#include<iostream>
using namespace std;

long long box_no[105];
long long box_type[105];
long long toy_no[105];
long long toy_type[105];
int n,m;
long long ma=0;

void recur(int pos_n,int pos_m,long long cnt)
{
    long long tmp;
    if(pos_n>=n || pos_m>=m)
    {
        if(ma<cnt)
            ma=cnt;
        return;            
    }
    
    if(box_type[pos_n]==toy_type[pos_m] && box_no[pos_n]>0 && toy_no[pos_m]>0 && box_no[pos_n]>toy_no[pos_m])
    {
            tmp=toy_no[pos_m];
            box_no[pos_n]-=tmp;
            toy_no[pos_m]-=tmp;
            cnt=cnt+tmp;
            
            recur(pos_n,pos_m+1,cnt);
            
            box_no[pos_n]+=tmp;
            toy_no[pos_m]+=tmp;
            cnt=cnt-tmp;
                                                                       
    } 
    
    else if(box_type[pos_n]==toy_type[pos_m] && box_no[pos_n]>0 && toy_no[pos_m]>0 && box_no[pos_n]<=toy_no[pos_m])
    {
            tmp=box_no[pos_n];
            box_no[pos_n]-=tmp;
            toy_no[pos_m]-=tmp;
            cnt=cnt+tmp;
            
            recur(pos_n+1,pos_m,cnt);
            
            box_no[pos_n]+=tmp;
            toy_no[pos_m]+=tmp;
            cnt=cnt-tmp;    
    }   
     
    else
    {
        recur(pos_n+1,pos_m,cnt);
        recur(pos_n,pos_m+1,cnt);   
    }
    
}



int main()
{
    int t,cas=1,i;

    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&n,&m);
        
        for(i=0;i<n;i++)
        {
            scanf("%lld %lld",&box_no[i],&box_type[i]);                
        }      
        
        for(i=0;i<m;i++)
        {
            scanf("%lld %lld",&toy_no[i],&toy_type[i]);                
        }     
        ma=0;
        recur(0,0,0);
        
        printf("Case #%d: %lld\n",cas++,ma);
    }
}
