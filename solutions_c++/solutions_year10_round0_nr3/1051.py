#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    long long r,k,n;int cas;cin>>cas;
    for(int caso=0;caso<cas;caso++){
        cin>>r>>k>>n;
        vector<long long>v(2*n);
        long long sum=0;
        for(int i=0;i<n;i++){cin>>v[i];v[i+n]=v[i];sum+=v[i];}
        long long dev=0;
        long long ind1=0;long long ind2=0;
        for(int i=0;i<r;i++){
            if(k>=sum){dev+=sum;continue;}
            long long t=0;
            for(int j=ind1;j<2*n;j++){
                if(t+v[j]>k){ind2=j%n;break;}
                t+=v[j];
            }
            dev+=t;
            ind1=ind2;
        }
        cout<<"Case #"<<caso+1<<": "<<dev<<endl;
        
    }
    //system("pause");
    return 0;
}


