#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
using namespace std;
int main()
{ int T;
  scanf("%d\n",&T);
  for(int t=0;t<T;t++)
  { int N,K;
    scanf("%d %d\n",&N,&K);
    string binary="";
    while(K>0)
    { binary+=char(K%2+'0');
      K=K/2;
    }
    int on=1;
    int blen=binary.size();
    while(blen<N)
    { binary+="0";
      blen++;
    }
    for(int i=0;i<N;i++)
    if(binary[i]=='0')
    { on=0;
      break;
    }
    printf("Case #%d: %s\n",t+1,(on?"ON":"OFF"));
  }
}
