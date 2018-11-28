#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct eve{
  int time;
  int type;
  int st;
} ev[100000];

int evcmp(const void *a, const void *b){
  eve* ta=(eve*)a;
  eve* tb=(eve*)b;
  if (ta->time!=tb->time) return ta->time-tb->time;
  if (ta->type!=tb->type) return ta->type-tb->type;
  return ta->st-tb->st;
}

int main(){
  int i,l,u;
  int t,clock;
  int na,nb,c[2],loan[2];
  int evc,h,m,h1,m1;
  char s[10001];
  gets(s);
  sscanf(s,"%d",&l);
  for (u=0; u<l; u++){
    evc=0;
    c[0]=c[1]=loan[0]=loan[1]=0;
    gets(s);
    sscanf(s,"%d",&t);
    clock=0;
    gets(s);
    sscanf(s,"%d %d",&na,&nb);
    for (i=0; i<na; i++){
      gets(s);
      sscanf(s,"%d:%d %d:%d",&h,&m, &h1,&m1);
      ev[evc].time=h*60+m;
      ev[evc].type=1;
      ev[evc].st=0;
      evc++;
      ev[evc].time=h1*60+m1+t;
      ev[evc].type=0;
      ev[evc].st=1;
      evc++;
    }
    for (i=0; i<nb; i++){
      gets(s);
      sscanf(s,"%d:%d %d:%d",&h,&m, &h1,&m1);
      ev[evc].time=h*60+m;
      ev[evc].type=1;
      ev[evc].st=1;
      evc++;
      ev[evc].time=h1*60+m1+t;
      ev[evc].type=0;
      ev[evc].st=0;
      evc++;
    }
    qsort(ev,evc,sizeof(eve),evcmp);
    for (i=0; i<evc; i++){
      if (ev[i].type==0){
	c[ev[i].st]++;
      }
      else{
	if (c[ev[i].st]==0)
	  loan[ev[i].st]++;
	else
	  c[ev[i].st]--;
      }
    }
    //simulate
    printf("Case #%d: %d %d\n",u+1,loan[0],loan[1]);
  }
  return 0;
}
