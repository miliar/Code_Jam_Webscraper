#include <iostream>

using namespace std;

int main()
{
    int T,N,i,j,a,cnt;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cin>>N;
        cnt=0;
        for(j=1;j<=N;j++)
        {
            cin>>a;
            if(a!=j)
            {
                cnt++;
            }
        }
        cout<<"Case #"<<i<<": "<<cnt<<".000000"<<endl;
    }
    return 0;
}
