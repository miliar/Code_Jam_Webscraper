#include <stdio.h>

char engine[128][256];
int query[1024];

int sw[128],next[128];

void solve(int S,int Q)
{
  for (int i=0; i<S; i++) sw[i]=0;
  for (int i=Q-1; i>=0; i--) {
    int fst=0, snd=1;
    for (int j=1; j<S; j++) {
      if (sw[j]<sw[fst]) {
        snd=fst;
        fst=j;
      } else if (sw[j]<sw[snd]) {
        snd=j;
      }
    }
    for (int j=0; j<S; j++) {
      if (query[i]==j) {
        next[j] = (j!=fst ? sw[fst] : sw[snd]) + 1;
      } else {
        next[j] = sw[j];
      }
    }
    for (int j=0; j<S; j++) {
      sw[j]=next[j];
    }
  }
  int mn=0;
  for (int j=0; j<S; j++) {
    if (sw[j]<sw[mn]) mn=j;
  }
  printf("%d\n",sw[mn]);
}

void read_string(char *p)
{
  fgets(p,128,stdin);
  while (*p!=0) {
    if (*p=='\n' || *p=='\r') { *p=0; break; }
    p++;
  }
}

int main()
{
  int N,S,Q;
  char q_temp[256];
  
  scanf("%d\n",&N);
  for (int j=0; j<N; j++) {
    scanf("%d\n",&S);
    for (int i=0; i<S;i++) {
      read_string(engine[i]);
    }
    scanf("%d\n",&Q);
    for (int i=0; i<Q;i++) {
      read_string(q_temp);
      for (int k=0; k<S; k++) {
        bool match=true;
        for (char *p=engine[k],*q=q_temp; ; p++,q++) {
          if (*p!=*q) {
            match=false;
            break;
          }
          if (*p==0) break;
        }
        if (match) {
          query[i]=k;
          break;
        }
      }
    }
    printf("Case #%d: ",j+1);
    solve(S,Q);
  }
  
  return 0;
}

