#include<iostream>
using namespace std;

int main()
{
    int t,n,s,p,cas=1,b,tmp,cnt=0,j=0,elt1,elt2,diff=0,k,c=0,ma=0,i;
    int arr[105][4];
    
    scanf("%d",&t);
    
    while(t--)    
    {
        scanf("%d %d %d",&n,&s,&p);
        for(i=0;i<n;i++)
            scanf("%d",&arr[i][0]);
            
        
        for(i=0;i<(1<<n);i++)
        {
            b=i;
            tmp=i; 
            
            cnt=0;
            k=0;
            while(b>0)
            {
                if(b&1)
                {
                    if(arr[k][0]==29 || arr[k][0]==30 || arr[k][0]==0 || arr[k][0]==1)
                    {
                                     
                    }
                    else
                        cnt++;
                }
                b=b>>1;
                k++; 
            }     
            
            if(cnt==s)
            {
                      
                j=0;
                c=0;
                while(tmp>0)
                {
                    if(tmp&1)
                    {
                        if(arr[j][0]==29 || arr[j][0]==30 || arr[j][0]==0 || arr[j][0]==1)
                        {
                            elt1=arr[j][0];
                            elt2=elt1/3;
                            
                            arr[j][1]=elt2;
                            arr[j][2]=elt2;
                            arr[j][3]=elt2;
                            diff=elt1-(3*elt2);
                            
                            if(diff==0)
                            {
                                if(arr[j][3]>=p)
                                    c++;           
                            }
                            else if(diff==1)
                            {
                                arr[j][3]++; 
                                if(arr[j][3]>=p)
                                    c++;    
                            }
                            else if(diff==2)
                            {
                                arr[j][2]++;
                                arr[j][3]++; 
                                if(arr[j][3]>=p)
                                    c++;    
                            }             
                        }
                        else
                        {
                            elt1=arr[j][0];
                            elt2=elt1/3;
                        
                            arr[j][1]=elt2;
                            arr[j][2]=elt2;
                            arr[j][3]=elt2;
                            diff=elt1-(3*elt2);
                        
                            if(diff==0)
                            {
                                arr[j][1]--;
                                arr[j][3]++;
                                if(arr[j][3]>=p)
                                    c++;
                            }
                            else if(diff==1)
                            {
                                arr[j][1]--;
                                arr[j][2]++;
                                arr[j][3]++;
                                if(arr[j][3]>=p)
                                    c++;     
                            }
                            else if(diff==2)
                            {
                                arr[j][3]=arr[j][3]+2;  
                                if(arr[j][3]>=p)
                                    c++;   
                            }
                        }
                    }
                    else
                    {
                        elt1=arr[j][0];
                        elt2=elt1/3;
                            
                        arr[j][1]=elt2;
                        arr[j][2]=elt2;
                        arr[j][3]=elt2;
                        diff=elt1-(3*elt2);
                            
                        if(diff==0)
                        {
                            if(arr[j][3]>=p)
                                c++;           
                        }
                        else if(diff==1)
                        {
                            arr[j][3]++; 
                            if(arr[j][3]>=p)
                                c++;    
                        }
                        else if(diff==2)
                        {
                            arr[j][2]++;
                            arr[j][3]++; 
                            if(arr[j][3]>=p)
                                c++;    
                        }
                                   
                    }
                    tmp=tmp>>1;
                    j++;
                    diff=0;          
                }    
                
                for(;j<n;j++)
                {
                    elt1=arr[j][0];
                        elt2=elt1/3;
                            
                        arr[j][1]=elt2;
                        arr[j][2]=elt2;
                        arr[j][3]=elt2;
                        diff=elt1-(3*elt2);
                            
                        if(diff==0)
                        {
                            if(arr[j][3]>=p)
                                c++;           
                        }
                        else if(diff==1)
                        {
                            arr[j][3]++; 
                            if(arr[j][3]>=p)
                                c++;    
                        }
                        else if(diff==2)
                        {
                            arr[j][2]++;
                            arr[j][3]++; 
                            if(arr[j][3]>=p)
                                c++;    
                        }                 
                }
                
                if(ma<c)
                    ma=c;
                      
            }
            
            
                       
        }
        
        printf("Case #%d: %d\n",cas++,ma);
        ma=0;
        
        
                  
    }
}
