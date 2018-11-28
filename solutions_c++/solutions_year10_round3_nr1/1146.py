#include<iostream.h>
#include<string.h>
#include<fstream.h>
int func(int a[10002],int b[10002],int n);
int main()
{
    int a[1002]={0};
    int b[1002]={0};
    fstream q("q.in");
    fstream fans("a.out");
    int tc=0;
    q>>tc;
    int n=0;
    int ans=0;
    for(int tcount=0;tcount<tc;tcount++)
    {
        q>>n;
        for(int nn=0;nn<n;nn++)
        {
            q>>a[nn];
            q>>b[nn];
        }

        ans= func(a,b,n);
        fans<<"Case #"<<tcount+1<<": "<<ans<<endl;
    }

    //Input the dataVals into 2 arrays
}

int func(int a[1002],int b[1002],int n)
{

    int count=0;

    //Iterate each entry
    for(int i=0;i<n;i++)
    {
        //if(a[i]==b[i]) continue;
        for(int j=0;j<n;j++)
        {
            if(i==j) continue;
            //Consider a[i]&b[i];
            if(((a[j]<a[i])&&(b[j]>b[i]))||((a[j]>a[i])&&(b[j]<b[i]))) count++;
        }

    }

    //Find the count: intersects

    //Output
    //cout<<"\n"<<count;
    return (count/2);
}
