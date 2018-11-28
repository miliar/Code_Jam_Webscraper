#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>
#include <vector>
#include <iostream>

using namespace std;

int main() {
  int T,N;
  int i,j,k,m;
  char s[512], *p, *q, c;

  vector<int> v;
  int cred[2], pos[2];
  int clock, dist, t, d;

  scanf("%d\n",&T);
  //cout << T << endl;    

  for(i=1;i<=T;i++) {
    v.clear();

    fgets(s,512,stdin);
    //printf("s=[%s]\n",s);
    p = strtok(s," \r\n\t");
    N = atoi(p);    
    //cout << N << endl;

    for(j=0;j<N;j++) {
      p = strtok(NULL," \r\t\n");
      c = *p;
      p = strtok(NULL," \r\t\n");

      if (c=='O') v.push_back(atoi(p));
      if (c=='B') v.push_back(-atoi(p));
    }

    // done reading
    clock = 0;
    pos[0] = pos[1] = 1;
    k = -1;

    for(j=0;j<v.size();j++) {
      //printf("before clock=%d pos=(%d,%d) E=%d\n",clock,pos[0],pos[1],v[j]);

      if (v[j] < 0 ) k = 1; else k = 0;

      dist = abs(pos[k] - abs(v[j]));

      t = dist + 1;
      pos[k] = abs(v[j]);
      clock += t;
      
      // move other robot towards next goal, at most t steps
      for(m=j+1;m<v.size();m++)
	if (v[m] * v[j] < 0) {
	  
	  d = abs(pos[1-k] - abs(v[m]));
	  if (d <= t)
	    pos[1-k] = abs(v[m]);
	  else {
	    if (abs(v[m]) > pos[1-k])
	      pos[1-k] += t;
	    else
	      pos[1-k] -= t;
	  }
	  break;
	}

      //printf("after clock=%d bot=%d pos=(%d,%d) t=%d\n",clock,k,pos[0],pos[1],t);
    }
    
    printf("Case #%d: %d\n",i,clock);
  }

  return 0;
}
