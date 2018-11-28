#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>

#define rep(i,n) for(int i=0;i<n;i++)
#define rp(i,n) for(i=0;i<n;i++)
#define pr(i) cout<<i<<endl

using namespace std;

int n,a,b,t,k,tmp,r,cnt;
int e[9];
map<int,int> his;


int main(){

  cin>>n;e[0]=1;
  rep(i,7)e[i+1]=e[i]*10;

  rep(ii,n){

    r=0;k=0;

    cin>>a>>b;t=a;
    while(t>0){k++;t/=10;}

    for(int s=a;s<=b;s++){

      his.clear();

      for(int j=1;j<k;j++){
	tmp=s/e[j]+(s%e[j])*e[k-j];
	if(tmp>s&&tmp<=b){
	  if(his[tmp]++==0)r++;
	}
      }

    }
    cout<<"Case #"<<ii+1<<": "<<r<<endl;
  }

  

}
