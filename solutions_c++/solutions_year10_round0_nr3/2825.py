#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("C-small-attempt2.in");
    ofstream fout("output.txt");
    int t,r[70],k[70],n[70],a[2000],s[2000],sum=0;
    fin>>t;
    int i,j,start,m,sign;
    for(i=0;i<t;i++)
    {
        sum=0;
        fin>>r[i]>>k[i]>>n[i];
        for(j=0;j<n[i];j++)
        fin>>a[j];
        
        s[0]=0;
        s[1]=a[0];
        for(j=1;j<n[i];j++)
        s[j+1]=s[j]+a[j];
        
        start=0;
        for(j=0;j<r[i];j++)
        {
            if(k[i]>=s[n[i]])
            {
                sum=r[i]*s[n[i]];
                break;
            }
            if(k[i]<s[n[i]]-s[start])
            {
            for(m=start;m<=n[i];m++)
            {
                if(k[i]<s[m]-s[start])
                {
                    sum=sum+s[m-1]-s[start];
                    start=m-1;
                    break;
                }
            }
            }    
            else
            {
            for(m=1;m<=start;m++)
            {
                if(k[i]-s[n[i]]+s[start]<s[m])
                {
                    sum=sum+s[m-1]+s[n[i]]-s[start];
                    start=m-1;
                    break;
                }
            }
            }        
        }
        
        fout<<"Case #"<<i+1<<':'<<" "<<sum<<endl;
        
    }
    return 0;
}
