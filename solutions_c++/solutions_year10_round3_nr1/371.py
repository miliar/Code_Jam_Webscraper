#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <ctime>
// #define NDEBUG
#include "assert.h"
#include "string.h"
#define MP make_pair
#define COMMENT 1
using namespace std;

typedef unsigned uint;
typedef long long int llint;
typedef pair<int,int> PII;

int T[10002],t,N,c=0;
PII A[10001];

void update(int idx,int val){
  idx++;
  while (idx<10001){
    T[idx]+=val;
    idx+=idx&-idx;
  }}
int read(int idx){
  idx++;
  int sum=0;
  while (idx>0){
    sum+=T[idx];
    idx-=idx&-idx;}
  return sum;}

int main(){
  scanf("%d",&t);
  while (c++<t){
    memset(T,0,sizeof T);
    scanf("%d",&N);
    for (int i=0; i<N; i++) scanf("%d %d",&A[i].first,&A[i].second);
    sort(A,A+N);
    int sol=0;
    for (int i=0; i<N; i++){
      sol+=read(10000-A[i].second);
      update(10000-A[i].second,1);
    }
  printf("Case #%d: %d\n",c,sol);
  }
}
      
  
