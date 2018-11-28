#include<fstream>
#include<algorithm>
#include<iostream>
#include<string>
#include<map>
#include<sstream>
using namespace std;
ifstream fin("C.in");
ofstream fout("C.out");
int sub1[25],sub2[25],P1,P2,N;
int S[25];
map<string,bool> mp;
//bool vis[20][5000][5000];
string numstr(int i,int j,int k)
{
    stringstream ss;
    ss<<i<<"-"<<j<<"-"<<k;
    string ret;
    ss>>ret;
    return ret;
}
bool solve(int ind,int sum1,int sum2)
{
    if(ind==N)return 0;
    if(mp[numstr(ind,sum1,sum2)])return 0;
    //if(vis[ind][sum1][sum2])return 0;
    if(sum1==sum2&&ind&&sum1)
    return 1;
    //vis[ind][sum1][sum2]=1;
    mp[numstr(ind,sum1,sum2)]=1;
    int op;
    //cin>>op;
    //if(op==1)
    if(solve(ind+1,sum1,sum2))
    {
        //sub2[P2++]=S[ind];
        return 1;
    }
    if(solve(ind+1,sum1+S[ind],sum2))
    {
        sub1[P1++]=S[ind];
        return 1;
    }
    //if(op==2)
    if(solve(ind+1,sum1,sum2+S[ind]))
    {
        sub2[P2++]=S[ind];
        return 1;
    }
    //if(op==3)
    
    return 0;
}
int main()
{
    int T;
    fin>>T;
    for(int c=1;c<=T;c++)
    {
        mp.clear();
        fin>>N;
        P1=0,P2=0;
        fout<<"Case #"<<c<<":"<<endl;
        for(int i=0;i<N;i++)
        fin>>S[i];
        if(solve(0,0,0))
        {
            //reverse(sub1,sub1+P1);
            for(int i=P1-1;i>-1;i--)
            fout<<sub1[i]<<" ";
            fout<<endl;
            for(int i=P2-1;i>-1;i--)
            fout<<sub2[i]<<" ";
            fout<<endl;
        }
        else
        fout<<"Impossible"<<endl;
    }
    return 0;
}
