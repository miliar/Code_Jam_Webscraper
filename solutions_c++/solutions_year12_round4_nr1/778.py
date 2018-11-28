#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<sstream>
#include<queue>

using namespace std;

const int MX=111111;
int N,DD;

int D[MX],L[MX],ML[MX];

void test()
{
    int i,j;
    cin>>N;


    for(i=0;i<N;i++)
    {
        cin>>D[i]>>L[i];
    }
    cin>>DD;

    ML[0]=D[0];

    for(i=1;i<N;i++) ML[i]=0;

    for(i=0;i<N;i++) if(ML[i])
        {
            if(ML[i]>L[i]) ML[i]=L[i];
            //cout<<i<<" "<<ML[i]<<" "<<D[i]<<endl;
            if(D[i]+ML[i]>=DD)
                {
                    cout<<"YES";
                    return;
                }
            j=i+1;

            while(j<N&&D[j]<=D[i]+ML[i])
            {
                if(ML[j]<D[j]-D[i])
                    {
                        ML[j]=D[j]-D[i];
                    }
                j++;
            }
        }

    cout<<"NO";

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int i,I;
    cin>>I;

    for(i=0;i<I;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        test();
        cout<<endl;
    }
    return 0;
}
