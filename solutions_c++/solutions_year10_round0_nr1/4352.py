#include<iostream>

    using namespace std;

int main()
{
    int T,N,A[30],ans,i,j,x;
    long int K;
    cin>>T;
    for(i=0;i<T;i++)
    {
        cin>>N>>K;
        for(j=0;j<N;j++)
            A[j]=0;
        for(j=0;j<K;j++)
        {
            x=0;
            while(A[x]==1)
            {
                A[x++]=0;
            }
            if(A[x]==0)
                A[x]=1;
            else
                A[x]=0;
        }
        ans=1;
        for(j=0;j<N;j++)
        {
            if(A[j]==0)
            {
                ans=0;
                break;
            }
        }
        if(ans==1)
            cout<<"Case #"<<i+1<<": ON\n";
        else
            cout<<"Case #"<<i+1<<": OFF\n";

    }
    return 0;
}
