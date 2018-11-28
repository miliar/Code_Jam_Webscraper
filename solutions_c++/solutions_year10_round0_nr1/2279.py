/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

int get(int x,int mask){
  while(x){
    if(!(mask&1)) return 0;
    x--;
      mask>>=1;
  }
  return 1;
}

int main(int argc,char **argv){
  int no,tc;
    scanf(" %d",&no);
    for(tc=1;tc<=no;tc++){
      int N,K;
        scanf(" %d %d",&N,&K);
        int ans=get(N,K);
        printf("Case #%d: %s\n",tc,ans?"ON":"OFF");
      
      }
    return 0;
}

