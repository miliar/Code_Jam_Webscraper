/*
  Input from stdin, output to stdout
 */

#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;

struct traintime
{
  int t; // time in minutes from 00:00
  int station; // 0=A, 1=B  
  int status; // 0=depart, 1=ready
} S[500];

bool operator < (const traintime &a, const traintime &b)
{
  if(a.t==b.t) return a.status>b.status;
  else return a.t<b.t;
}

int main()
{
  int N;
  scanf("%d", &N);
  for(int t=1; t<=N; t++){
    int T, NA, NB, c=0;
    scanf("%d%d%d", &T, &NA, &NB);
    for(int i=0; i<NA; i++){
      int h, m;
      scanf("%d:%d", &h, &m);
      S[c].t=h*60+m;
      S[c].station=0;
      S[c].status=0;
      c++;

      scanf("%d:%d", &h, &m);
      S[c].t=h*60+m+T;
      S[c].station=1;
      S[c].status=1;
      c++;
    }
    
    for(int i=0; i<NB; i++){
      int h, m;
      scanf("%d:%d", &h, &m);
      S[c].t=h*60+m;
      S[c].station=1;
      S[c].status=0;
      c++;

      scanf("%d:%d", &h, &m);
      S[c].t=h*60+m+T;
      S[c].station=0;
      S[c].status=1;
      c++;
    }

    sort(S, S+c);
    int ans[2]={0}, ct[2]={0}; // ct: current number of trains
    for(int i=0; i<c; i++){
      int station=S[i].station;
      if(S[i].status==0){  //need to depart
	if(ct[station]>0) ct[station]--;
	else ans[station]++; 
      }
      else  //train just got ready
	ct[station]++;
    }
    
    printf("Case #%d: %d %d\n", t, ans[0], ans[1]);
  }
  return 0;
}
