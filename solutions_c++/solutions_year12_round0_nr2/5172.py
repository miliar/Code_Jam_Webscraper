#include<iostream>
#include<conio.h>


using namespace std;

int main()

{
   freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    int t,n,s,p,a[100],i,b[3],b1[3],ans,divide,mod,i1=0,s1;
    cin>>t;
    while(t--)
    {
        i1++;
        ans=0;
        cin>>n>>s>>p;s1=s;
        for(i=0;i<n;i++) 
        {
            cin>>a[i];
            divide=a[i]/3;
            
            mod=a[i]%3;
            if(mod==0)
            {
                b[0]=b[1]=b[2]=divide;
                b1[0]=divide-1;b[1]=divide;b[2]=divide+1;
                if(divide>=p)
                {
                    ans++;//s--;
                }
                else
                {
                if(s>0&&(divide+1)>=p&&divide>0)
                {
                    ans++;s--;
                }
               // if(s1==0&&(divide+1)>=p&&divide>0)
                //{ans++;
                //}
            }    
            }
             else if(mod==1)
            {
                b[0]=b[1]=divide;b[2]=divide+1;
                b1[0]=divide-1;b1[1]=b1[2]=divide+1;
                if(divide>=p||(divide+1)>=p)
                {
                    ans++;//s--;
                    
                }else
                {
                if(s>0&&(divide+1)>=p && divide>0)
                {
                    ans++;s--;
                    
                }
               // if(s1==0&&(divide+1)>=p&&divide>0)
                //{ans++;
                //}
                }
            }
            else 
            {
                b[0]=b[1]=divide+1;b[2]=divide;
                b1[0]=b1[1]=divide;b1[2]=divide+2;
                if(divide>=p||(divide+1)>=p)
                {
                    ans++;
                }else
                {
                if(s>0&&(divide+2)>=p&&divide>0)
                {
                    ans++;s--;
                    
                }
                //if(s1==0&&(divide+2)>=p&&divide>0)
                //{ans++;
                //}
                }
            }
            
            
        }   cout<<"Case #"<<i1<<": "<<ans<<"\n"; 
        
        
        
        
    }
    
    return 0;
    
}
