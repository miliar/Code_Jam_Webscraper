#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    int t; long a[1010]; long n; long small=10000000; long out=0; long output[110];long sum=0;
    cin>>t;
    for(int i=0;i<t;i++)
    {
            cin>>n;
            for(int j=0;j<n;j++)
            {
                    cin>>a[j];
                    sum+=a[j];
                    if(a[j]<small)
                                  small=a[j];
                    out=out^a[j];
            }
            if(out==0)
                      output[i]=sum-small;
            else
                      output[i]=-1;
            
            for(int j=0;j<n;j++)
                    a[j]=0;
            small=10000000;
            out=0;
            sum=0;
    }
    
    for(int i=0;i<t;i++)
    {
            if(output[i]==-1)
                             cout<<"Case #"<<i+1<<": NO"<<endl;
            else
                             cout<<"Case #"<<i+1<<": "<<output[i]<<endl;
    }
    getchar();
    getchar();
    return 0;
}



            
                    
