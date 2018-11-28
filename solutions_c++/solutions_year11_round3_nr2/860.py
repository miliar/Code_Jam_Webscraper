//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>

using namespace std;

int main()
{
    freopen("BIT.txt","r",stdin);
    freopen("outputbt.txt","w",stdout);
    int cas,kas;
    cin>>kas;
    for(cas=0;cas<kas;cas++)
    {
        long long L,t,n,c,ar[10999];
        cin>>L>>t>>n>>c;
        for(int i=0;i<c;i++)
        cin>>ar[i];
        vector<int>vec;
        int cur=0,sst=0;

        while(1){
            if(cur==n)break;

            for(int i=0;i<c;i++){
                cur++;
                vec.push_back(ar[i]);
                sst+=ar[i];
                if(cur==n)break;
            }
        }




        long long sum=0,ss=-1;
        for(int i=0;i<n;i++){
            if(sum+vec[i]*2>=t){
                ss=i;
                vec[i]=vec[i]-(t-sum)/2;
                break;
            }
            sum+=vec[i]*2;
        }



        long long res=2*sst;
        while(L>0)
        {
            int mx=0,fl=-1;
            if(ss!=-1)
            for(int i=ss;i<n;i++){
                if(mx<vec[i]){mx=vec[i],fl=i;}
            }
            res-=mx;
            if(fl!=-1)
            vec[fl]=-100000;
            L--;
        }
        cout<<"Case #"<<cas+1<<": "<<res<<endl;
    }
}
