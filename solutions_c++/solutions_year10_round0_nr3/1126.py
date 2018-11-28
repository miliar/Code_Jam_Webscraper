#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
using namespace std;
int rnd[2000][2];
int data[1000];
int prnd[2000];
int R,K,N;
int exist;
int rno;
int next;
long long getearning(int top)
{ exist=0;
  if(prnd[top]!=-1)
  { exist=1;
    return rnd[prnd[top]][1];
  }
  long long sum=0;
  int cur=top;
  while(sum<K)
  { if(sum+data[cur]>K)
    break;
    sum+=data[cur];
    cur=(cur+1)%N;
    if(cur==top)
    break;
  }
  prnd[top]=rno;
  rnd[rno][0]=top;
  rnd[rno][1]=sum;
  next=cur;
  return sum;
}
int main()
{ int T;
  scanf("%d\n",&T);
  for(int t=0;t<T;t++)
  { scanf("%d %d %d\n",&R,&K,&N);
    for(int i=0;i<N-1;i++)
    scanf("%d ",&data[i]);
    scanf("%d\n",&data[N-1]);
    rno=0;
    exist=0;
    for(int i=0;i<N;i++)
    prnd[i]=-1;
    int cur=0;
    long long sum=0;
    while(exist==0&&rno<R)
    { 
      long long earn=getearning(cur);
      if(exist==1)
      { long long done=(R-rno)/(rno-prnd[cur]);
        long long tearn=0;
        for(int i=prnd[cur];i<rno;i++)
        tearn+=rnd[i][1];
        sum+=done*tearn;
        rno+=done*(rno-prnd[cur]);
        for(int tr=prnd[cur];rno<R;tr++,rno++)
        { sum+=rnd[tr][1];
        }
        break;
      }
      else
      { sum+=earn;
        cur=next;
        rno++;
      }
    }
    printf("Case #%d: %lld\n",t+1,sum);
  }
}
