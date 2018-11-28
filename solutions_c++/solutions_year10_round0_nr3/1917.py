#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double ldouble;
using namespace std;
int main(){
    int test,z;
    cin>>test;
    for(z=1;z<=test;z++){
            int64 R,K,N,i;
            cin>>R>>K>>N;
            int group[N],cost[N],ends[N];
            for(i=0;i<N;i++){
                            cin>>group[i];
            }
             for(i=0;i<N;i++){
                    int64 j=i,total=0;
                    while((total+group[j])<=K){
                                  total+=group[j];
                                  j++;
                                  j%=N;
                                  if(j==i)
                                          break;
                    }
                    cost[i]=total;
                    ends[i]=j;
             }
            int64 money=0,pos=0;
            for(i=0;i<R;i++){
                       money+=cost[pos];
                       pos=ends[pos];
            }
            cout<<"Case #"<<z<<": "<<money<<endl;
    }
    return 0;
}
