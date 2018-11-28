#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;

int mod2er(int x, int k){
k++;
for(int i=0;i<x;i++)
{if(k%2==1 || k==0)return 0;
k/=2;
}
return 1;
}

int main(){
int T,C=1,n,k,t;
cin>>T;
for(;C<=T;C++){
cin>>n>>k;
t=mod2er(n,k);
printf("Case #%d: %s\n",C,t?"ON":"OFF");
}
return 0;
}
