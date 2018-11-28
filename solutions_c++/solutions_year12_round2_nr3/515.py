#include<iostream>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<sstream>
#include<queue>
#include<cstdio>

using namespace std;

int N;

const int MX=555;
const int MY=111111;
int A[MX];

int FROM[MX*111111];
void test()
{
    cin>>N;
    int i,x,mx,sum,ans;

    for(i=0;i<N;i++) cin>>A[i];

    mx=1<<N;

    cout<<endl;

    set<int> S;
    for(x=1;x<mx;x++)
    {
        sum=0;
        for(i=0;i<N;i++) if(x&(1<<i)) sum+=A[i];
        if(S.find(sum)!=S.end())
        {
            for(i=0;i<N;i++) if(x&(1<<i)) cout<<A[i]<<" ";
            cout<<endl;

            ans=sum;

            for(x=1;x<mx;x++)
            {
                sum=0;
                for(i=0;i<N;i++) if(x&(1<<i)) sum+=A[i];
                if(sum==ans)
                {
                    for(i=0;i<N;i++) if(x&(1<<i)) cout<<A[i]<<" ";
                    return;
                }
            }
        }
        else S.insert(sum);
    }


    cout<<"Impossible";


}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
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
