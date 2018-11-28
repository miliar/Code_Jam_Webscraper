#include<iostream>
#include<cstdio>
#include<vector>

#define S second
#define F first
#define _m make_pair
#define Pii pair<int,int>
using namespace std;


Pii T2[1001];
bool operator<(Pii a, Pii b)
{
  return a.F<b.F;
}
int main()
{
  int T;
  scanf("%d",&T);
  for(int w=1;w<=T;w++)
  {
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf("%d %d",&T2[i].F,&T2[i].S);
    sort(T2,T2+n);
    int licznik=0;
    for(int i=0;i<n-1;i++)
      for(int j=i+1;j<n;j++)
        if(T2[i].F<T2[j].F && T2[i].S>T2[j].S)licznik++;
    printf("Case #%d: %d\n",w,licznik);
  }
  return 0;
}
