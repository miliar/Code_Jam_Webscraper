#include<iostream>

    using namespace std;

int main()
{
    int i,T,N,x,no;
    long int j,R,k,A[1000],ans[50],sum,temp[1000];
    cin>>T;
    for(i=0;i<T;i++)
    {
        cin>>R>>k>>N;
        for(j=0;j<N;j++)
            cin>>A[j];
        ans[i]=0;
        for(j=0;j<R;j++)
        {
            sum=0;
            no=0;
            while(sum<=k&&no<N)
            {
                sum+=A[no++];
            }
            if(sum>k)
            {
                no--;
                sum-=A[no];
            }
            ans[i]+=sum;
            for(x=0;x<no;x++)
            {
                temp[x]=A[x];
            }
            for(x=0;x<N-no;x++)
            {
                A[x]=A[x+no];
            }
            for(x=0;x<no;x++)
            {
                A[N-no+x]=temp[x];
            }
        }
    }
    for(i=0;i<T;i++)
        cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
    return 0;
}
