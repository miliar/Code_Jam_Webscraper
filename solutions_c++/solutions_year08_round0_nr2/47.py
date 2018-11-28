#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>


using namespace std;

int T;

int nA,nB;
int fromA[100];
int toA[100];
int fromB[100];
int toB[100];

void solve()
{
    int mininA=0,mininB=0;
    int inA=0,inB=0;
    int bonusA[2000],bonusB[2000];
    memset(bonusA,0,sizeof(bonusA));
    memset(bonusB,0,sizeof(bonusB));
    for (int i=0;i<24*60;i++)
    {
        inA+=bonusA[i];
        inB+=bonusB[i];
        for (int j=0;j<nA;j++) if(fromA[j]==i)
        {
            inA--;

            bonusB[ toB[j]+T ]++;
        }
        for (int j=0;j<nB;j++) if(fromB[j]==i)
        {
            inB--;
            bonusA[ toA[j]+T ]++;
        }
        mininA<?=inA;
        mininB<?=inB;

    }
    if(mininA<0) cout<<(-mininA);
    else cout<<0;
    cout<<" ";
    if(mininB<0) cout<<(-mininB);
    else cout<<0;
    
}

//=========================================================

int readTime()
{
    int h,m;
    scanf("%d:%d",&h,&m);
    return h*60+m;
}

void readTimes(int n, int* from, int* to)
{
    for (int i=0;i<n;i++)
    {
        from[i]=readTime();
        to[i]=readTime();
    }
}

int main()
{
    int N;
    cin>>N;
    for (int i=1;i<=N;i++)
    {
        
        cin>>T;
        cin>>nA>>nB;
        readTimes(nA,fromA,toB);
        readTimes(nB,fromB,toA);
        
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }
    
    
    

    return 0;
}
