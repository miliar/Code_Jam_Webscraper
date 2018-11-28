#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

//struct letter
//{
//    int idx;
//    int cnt;
//};
//
//bool comp(letter& a,letter& b)
//{
//    return a.cnt>b.cnt;
//}

int main()
{
    int N;
    int P,K,L;
    int l[1001];
    cin>>N;
    int idx;
    __int64 ans;
    for(int i=1;i<=N;i++)
    { 
        cin>>P>>K>>L;
        for(int j=0;j<L;j++)
        {
            cin>>l[j];
        }
        sort(l,l+L);
        ans=0;
        idx=0;
        for(int j=0;j<L;j++)
        {
            ans+=l[L-j-1]*(idx/K+1);
            idx++;
        }
        //for(int j=0;j<L;j++)
        //{
        //    cout<<l[j]<<" " ;
        //}

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}