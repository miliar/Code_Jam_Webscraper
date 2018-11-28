#include<iostream>
using namespace std;

int pow(int p,int q)
{
    int pt,ans;
    ans=p;
    if(q==0)
        return 1;
    else if(q==1)
        return p;
    else
    {
        for(pt=2;pt<=q;pt++)
            ans=ans*p;
            
        return ans;  
    } 
}

int main()
{
    int t,i,j,a,b,cas=1,tmp,k,elt,x,val=0,pwr=0,cnt=0,ptr,sp=0;
    int tmp_arr[10]={0};
    int ar[10];
    
    scanf("%d",&t);
    
    while(t--)
    {
        scanf("%d %d",&a,&b);
        
        for(i=a;i<b;i++)
        {
            j=0;
            tmp=i;
            
            while(tmp!=0)
            {
                tmp_arr[j]=(tmp%10);
                tmp=tmp/10; 
                j++;                
            }        
            ptr=0;                
            for(k=1;k<j;k++)
            {
                val=0;
                sp=0;
                elt=tmp_arr[0];
                for(x=1;x<j;x++)
                {
                    tmp_arr[x-1]=tmp_arr[x];
                    pwr=pow(10,x-1);
                    val+=pwr*tmp_arr[x-1];
                }
                tmp_arr[x-1]=elt;
                pwr=pow(10,x-1);
                val+=pwr*tmp_arr[x-1];
                
                for(ptr=0;ptr<k-1;ptr++)
                {
                    if(ar[ptr]==val)
                    {
                        sp=1; 
                        break;
                    }                       
                }
                ar[ptr]=val;
                
                if(val>=a && val<=b && val!=i && val>i && sp==0)
                {
                    cnt++;
                }                
            }
            
        } 
        
        
        printf("Case #%d: %d\n",cas++,cnt);
        cnt=0;         
    }    
}
