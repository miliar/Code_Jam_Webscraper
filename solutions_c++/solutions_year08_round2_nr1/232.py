#include <cstdio>
#include <functional>
#include <vector>
#include <iostream>

using namespace std;

typedef long long ll;
typedef pair<ll ,ll> pii;

int main(){
    int test,n;
    ll A,B,C,D,M; 
    pii c;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        vector<pii> vpii;
        cin>>n>>A>>B>>C>>D>>c.first>>c.second>>M;
        vpii.push_back(c);
        //cout<<c.first<<' '<<c.second<<endl;
        for(int i=1;i<n;i++){
            c.first=(A*c.first + B)%M;
            c.second=(C*c.second + D)%M;
            vpii.push_back(c);
             //cout<<c.first<<' '<<c.second<<endl;
        }
        int res=0;
        for(int i=0;i<n;i++)
        for(int j=i+1;j<n;j++)
        for(int k=j+1;k<n;k++)
            if(((vpii[i].first+vpii[j].first+vpii[k].first)%3==0)&&
               ((vpii[i].second+vpii[j].second+vpii[k].second)%3==0))
                res++;
        printf("Case #%d: %d\n",t+1,res); 
    }
}
