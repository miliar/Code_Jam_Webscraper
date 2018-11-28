#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
using namespace std;

void test()
{
    int N;
    cin>>N;
    int i,res=0,mn=100000001,x;

    __int64 sum=0;
    for(i=0;i<N;i++)
    {
        cin>>x;
        res^=x;
        sum+=x;
        if(x<mn) mn=x;
    }
    if(res!=0||N<2)
    {
        cout<<"NO";
        return;
    }
    cout<<sum-mn;
    return;

}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;

    //cout<<(5^4)<<" "<<(7^9)<<" "<<(50^10)<<endl;
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<": ";
      test();
      cout<<endl;
    }
    return 0;
}
