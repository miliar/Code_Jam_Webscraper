#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>

using namespace std;

struct Num
{
    __int64 num;
    __int64 cnt;
};

Num num[500001];
int idx;

bool comp(Num& a,Num& b)
{
    return a.num<b.num;
}

int findIdx(__int64 n)
{
    for(int i=0;i<idx;i++)
        if(num[i].num==n)
            return i;
    return -1;
}

//__int64 getSmallCnt(int n)
//{
//    __int64 ans = 0;
//    for(int i=0;i<idx;i++)
//        if(num[i].num==n)
//            return i;
//    return -1;
//}

int main()
{
    int N;
    cin>>N;
    int n,m;
    __int64 X,Y,Z,ans=0;;
    __int64 A[101];
    int k;
    
    
    for(int i=1;i<=N;i++)
    { 
        cin>>n>>m>>X>>Y>>Z;
        idx=0;
        memset(num,0,sizeof(num));
        memset(A,0,sizeof(A));
        ans=0;
        for(int j=0;j<m;j++)
        {
            cin>>A[j];
        }

        for(int j=0;j<n;j++)
        {
            //cout<<A[j%m]<<" ";
            k=findIdx(A[j%m]);
            if(k>=0)
                num[k].cnt++;
            else
            {
                num[idx].num = A[j%m];
                num[idx].cnt=1;
                idx++;
                sort(num,num+idx,&comp);
                k=findIdx(A[j%m]);
            }
            for(int l=0;l<k;l++)
            {
                if(num[l].num<A[j%m])
                {
                    num[k].cnt += num[l].cnt;
                    num[k].cnt %= 1000000007;
                }
            }

            A[j%m] = (X*A[j%m]+Y*(j+1))%Z;
        }
        /*for(int j=0;j<m;j++)
        {
            cout<<A[j]<<" ";
        }*/
        for(int j=0;j<idx;j++)
        {
            ans+=num[j].cnt;
            ans%=1000000007;
        }
        

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}