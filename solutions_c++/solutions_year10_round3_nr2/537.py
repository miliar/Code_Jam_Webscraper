// 2010A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <cassert>
#include <cmath>
#include <string>
#include <set>
using namespace std;

int main(int argc, char *argv[])
{
    freopen("B-small-attempt2.in","r",stdin);
 //    freopen("B-large-practice (1).in","r",stdin);
    freopen("out.txt","w",stdout);
      
    int T;

    scanf("%d",&T);
    
    int CASE = 1;
    while(T--)
    {

		  int L,P,C,res;
          scanf("%d %d %d",&L,&P,&C);
		  int i = 0;
		  res = 0;
		  while(L*C<P){
			  L = L*C;
			  i++;
		  }
		  if(i==0)
			  res = 0;
		  else{
			  int j = 1;
			  res = 0;
			  while(j-1<i){
				j *= 2;
				res++;
			  }
   			  
		  }
		  printf("Case #%d: %d\n",CASE,res);
		  
          CASE++;
    }

    return 0;
}
