#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
  int i,j,k,l,T,A,B,P;
  int set[1001],pri=0,o,p,q,r;
  int pr[1001][1001];
  int primes[1000];
  int sst[1001];

  for(i=2;i<1000;i++){
        k=0;
        for(l=2;l<i;l++)if(i%l==0)k=1;
        if(k==0)primes[pri++]=i;
  }

  cin>>T;
  for(i=1;i<=T;i++)
  {
    cin>>A;cin>>B;cin>>P;
    for(j=A;j<=B;j++){set[j]=j;sst[j]=0;}
    for(o=0;o<pri;o++)if(primes[o]>=P)break;
    for(j=A;j<B;j++){
        for(k=j+1;k<=B;k++){
            q=0;
            for(p=o;p<pri;p++){
                if(j%primes[p]==0 && k%primes[p]==0)q=1;
            }
            if(q && set[k]!=set[j]){
                r=set[k];
                for(p=A;p<=B;p++)if(set[p]==r){set[p]=set[j];
//cout<<j<<" "<<k<<" "<<p<<endl;
                }
            }
        }
    }
    for(j=A;j<=B;j++)sst[set[j]]=1;
    r=0;
    for(j=A;j<=B;j++)if(sst[j])r++;
    cout<<"Case #"<<i<<": "<<r<<endl;
  }

  return 0;
}

