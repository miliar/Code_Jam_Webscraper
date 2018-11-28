#include<fstream>
#include<iostream>
using namespace std;
main()
{
    ifstream in("b.in");
    ofstream out("b.txt");
    int r,n,k,test,a[1000],f[1000];
    long long b[1000];
    in>>test;
    for(int t1=1;t1<=test;t1++)
    {
        in>>r>>k>>n;
        int i,j;
        long long t;
        for(i=0;i<n;i++)
        {
            in>>a[i];
            if(i==0)b[i]=a[i];else b[i]=a[i]+b[i-1];
        }    
        
        out<<"Case "<<'#'<<t1<<": ";
        if(b[n-1]<=k) 
        {
            t=b[n-1];
            out<<t*r<<endl;
        }
        else
        {
            for(i=0;i<n-1;i++)if(b[i]<=k && b[i+1]>k){t=b[i];break;}
            f[0]=i+1;b[0]=t;
            for(i=1;i<n;i++)
            {
                j=f[i-1]-1;
                t-=a[i-1];
                while(t<=k)
                {
                    j=(j+1)%n;
                    t+=a[j];                    
                }    
                t-=a[j];
                f[i]=j;                 
                b[i]=t;
            }    
            for(i=0;i<n;i++)a[i]=1;
            i=j=0;t=0;
            while(a[i])            
            {
                a[i]=0;
                t+=b[i];
                i=f[i];                
                j++;
            }  
            if(r>=j)r=r-j;else t=0;
            
            for(j=0;j<n;j++)a[j]=1;
            j=0;
            long long t0=0,t1=0;
            while(a[i])            
            {
                a[i]=0;
                t0+=b[i];
                i=f[i];                
                j++;
            }
            t0*=r/j;            
            j=r%j;
            while(j>0)
            {
                t1+=b[i];
                i=f[i];                
                j--;
            }    
            out<<t+t0+t1<<endl;
        }        
    }    
}    
