#include<iostream>
#include<algorithm>
#include<set>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)

bool isok(int a,int b){
  char buf1[10],buf2[10];
  sprintf(buf1,"%d",a);
  sprintf(buf2,"%d",b);
  int len = strlen(buf1);
  rep(i,len){
    rep(j,len){
      if (buf1[(j+i)%len] != buf2[j])goto end;
    }
    return true;
  end:;
  }
  return false;
}


main(){
  int te,tc=1;
  cin>>te;
  while(te--){
    int n,m;
    cin>>n>>m;
    int ans = 0;
    REP(i,n,m+1){
      REP(j,n,i){
	if (isok(i,j))ans++;
      }
    end:;
    }
    cout <<"Case #" << tc++ << ": " << ans << endl;
  }
  return 0;
}

