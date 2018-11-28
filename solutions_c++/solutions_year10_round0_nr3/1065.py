#include<iostream>
#include<cstdlib>
using namespace std;

long long r,n,k,g[1000],head,sum,once,t,tt,i,j,a,b,round[1000],mark[1000]={0},backtrack[1000],length,circle,roundsum,markflag;


int main()
{
    FILE *in,*out;
    //in=freopen("C-small-attempt0.in","r",stdin);
    //in=freopen("C-small.in","r",stdin);
    in=freopen("C-large.in","r",stdin);
    out=freopen("C-small.txt","w",stdout);
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>r>>k>>n;//k is the capacity
        sum=0;
        for (i=0;i<n;i++)
        {
            cin>>g[i];
            sum+=g[i];
        }
        if (sum<=k)
            sum=sum*r;//the simplest case
        else
        {
            sum=0;
            
            for (i=1;i<1000;i++)
            {
                mark[i]=0;
                backtrack[i]=0;
            }
            mark[0]=1;
            backtrack[0]=1;
            markflag=0;
            i=0; 
            circle=1;
            roundsum=0;
            while (markflag==0)
            {
                once=0;
                while (once+g[i]<=k)
                {
                    once+=g[i];
                    i=(i+1)%n;
                }
                round[circle]=once;
                //cout<<"round["<<circle<<"]="<<once<<endl;
                circle++;
                if (mark[i])
                {
                    markflag=1;
                    //if (backtrack[i]!=0)
                    //length=abs(backtrack[i]-circle);
                }
                else 
                {
                    mark[i]=1;
                    backtrack[i]=circle;
                }
            }
            
            for (j=backtrack[i];j<circle;j++)
                roundsum+=round[j];                
            length=circle-backtrack[i];
            
            //cout<<length<<endl;
            
            a=(r-backtrack[i]+1)/length;
            b=(r-backtrack[i]+1)%length;
            //cout<<"a "<<a<<" b "<<b<<endl;
            //cout<<roundsum<<endl;
            
            sum=a*roundsum;
            //cout<<sum<<endl;
            //cout<<"i "<<i<<" backtrack[i] "<<backtrack[i]<<endl;
            for (j=0;j<backtrack[i]+b;j++)
            {
                sum+=round[j];
                //cout<<sum<<endl;
            }

        }
        cout<<"Case #"<<tt<<": "<<sum<<endl;
    }
    fclose(in);
    fclose(out);
    return 0;
}
            
