#include<iostream>
#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<utility>
#include<algorithm>
#include<queue>
#include<stack>
#include<list>
#include<vector>
#include<map>
#include<set>
using namespace std;

template<class T>
bool chkmax(T&a,T b){return a<b?a=b,1:0;}
template<class T>
bool chkmin(T&a,T b){return a>b?a=b,1:0;}


char mp[100][100];
int n,K;
void judge(bool&b,bool&r){
  int i,j,k;
  for(i=0;i<n;++i){
    for(j=0;j<n-K+1;++j){
      if(mp[i][j]=='.')continue;
      char x=mp[i][j];
      for(k=0;j+k<n && k<K && mp[i][j+k]==x;++k);
      if(k==K){
        if(x=='B')b=true;
        else if(x=='R')r=true;
      }
    }
  }
  for(i=0;i<n-K+1;++i){
    for(j=0;j<n;++j){
      if(mp[i][j]=='.')continue;
      char x=mp[i][j];
      for(k=0;i+k<n && k<K && mp[i+k][j]==x;++k);
      if(k==K){
        if(x=='B')b=true;
        else if(x=='R')r=true;
      }
    }
  }
  for(i=0;i<n-K+1;++i){
    for(j=0;j<n-K+1;++j){
      if(mp[i][j]=='.')continue;
      char x=mp[i][j];
      for(k=0;i+k<n && j+k<n && k<K && mp[i+k][j+k]==x;++k);
      if(k==K){
        if(x=='B')b=true;
        else if(x=='R')r=true;
      }
    }
  }
  for(i=K-1;i<n;++i){
    for(j=0;j<n-K+1;++j){
      if(mp[i][j]=='.')continue;
      char x=mp[i][j];
      for(k=0;i-k>=0 && j+k<n && k<K && mp[i-k][j+k]==x;++k);
      if(k==K){
        if(x=='B')b=true;
        else if(x=='R')r=true;
      }
    }
  }
}
void rotate(){
  int i,j,k;
  for(i=0;i<n;++i){
    for(j=n-1,k=n-1;j>=0;--j){
      if(mp[i][j]!='.'){
        char x=mp[i][j];
        mp[i][j]='.';
        mp[i][k--]=x;
      }
    }
  }
}



int main(){
	//freopen("A.in","r",stdin);
	//freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

  int Cas,ca=0;
  scanf("%d",&Cas);
  while(Cas--){
    scanf("%d%d",&n,&K);
    int i;
    for(i=0;i<n;++i)scanf("%s",mp[i]);
    bool b=false,r=false;
    //judge(b,r);
    rotate();

    //for(i=0;i<n;++i)puts(mp[i]);
    judge(b,r);
    printf("Case #%d: ",++ca);
    if(b&&r)puts("Both");
    else if(b)puts("Blue");
    else if(r)puts("Red");
    else puts("Neither");
  }
  return 0;
}
