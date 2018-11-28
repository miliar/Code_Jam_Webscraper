/* -*- c++ -*-
   ID: dirtysalt
   PROG: 
   LANG: C++
   copy[write] by dirlt(dirtysalt1987@gmail.com) */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstring>

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <algorithm>

using namespace std;
typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < double >VD;
typedef pair < int, int >PII;
#define SZ(v) ((int)((sizeof(v))/sizeof(*(v))))
#define PV(v) do {						\
    cout<<#v<<endl;						\
    for(int i=0;i<(int)(v).size();i++)cout<<(v)[i]<<" ";	\
    cout<<endl; \
  }while(0)
#define PA(v) do{							\
    cout<<#v<<endl;							\
    for(int i=0;i<(int)(sizeof(v)/sizeof(*(v)));i++)cout<<(v)[i]<<" ";	\
    cout<<endl;								\
  }while(0)
#define FUNC() do{					\
    cout<<"=========="<<__func__<<"=========="<<endl;	\
  }while(0)
char *pat="?welcome to code jam";
char src[1024];
int plen;
int slen;
/* DP[i][j] the numbers ot 1..ith of src matches 1..jth of pat */
int DP[1000][50];
int main()
{
  plen=strlen(pat);
  int casn;
  scanf("%d\n",&casn);
  for(int t=1;t<=casn;t++){
    src[0]='?';
    gets(src+1);
    //printf("%s\n",src);
    slen=strlen(src);
    for(int i=0;i<slen;i++)DP[i][0]=1;
    for(int i=1;i<slen;i++){
      for(int j=1;j<plen;j++){
	DP[i][j]=DP[i-1][j];
	if(src[i]==pat[j])DP[i][j]+=DP[i-1][j-1];
	DP[i][j]%=10000;
      }
    }
    printf("Case #%d: %04d\n",t,DP[slen-1][plen-1]);
  }
  return 0;
}
