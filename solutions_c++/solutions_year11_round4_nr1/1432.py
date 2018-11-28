
#include <stdio.h>

struct walk {
  int B;
  int E;
  int w;

};

main() {

  int T;
  


  scanf("%d",&T);

  for (int te = 1; te <= T; te++) {

    struct walk ws[2200], tmp;
    
    int X, S, R, t, N;

    scanf("%d %d %d %d %d",&X,&S,&R,&t,&N);
    double rt = t;
    double time = 0;

    for (int w = 0; w < N; w++) {
      scanf("%d %d %d",&ws[w].B,&ws[w].E,&ws[w].w);
    }
    for (int w = 0; w < N; w++) {
      for (int k = w+1; k < N; k++) {
	
	if (ws[w].B > ws[k].B) {
	  tmp = ws[w];
	  ws[w] = ws[k];
	  ws[k] = tmp;
	}

      }
    }

    int last = N;
    int posc = 0;
    for (int w = 0; w < N; w++) {
      if (posc != ws[w].B) {
	ws[last].B = posc;
	ws[last].E = ws[w].B;
	ws[last].w = 0;
	last++;
      }
      posc = ws[w].E;
    }
    if (posc != X) {
      ws[last].B = posc;
      ws[last].E = X;
      ws[last].w = 0;
      last++;
    }
    
    for (int w = 0; w < last; w++) {
      for (int k = w+1; k < last; k++) {
	
	if (ws[w].w > ws[k].w) {
	  tmp = ws[w];
	  ws[w] = ws[k];
	  ws[k] = tmp;
	}
      }
    }
    
    
    double  pos = 0;
    double endpos = X;

    int w = 0;
    while (w < last) {
      

      // take the walkway
      int speed = ws[w].w + S;
      pos = ws[w].B;
      endpos = ws[w].E;
      w++;
	   


      // now walk or run at this speed;
      
      if (rt > 0) {
	
	double t1 = (endpos - pos)/ (speed + R - S);	
	
	if (t1 > rt)
	  {
	    pos += rt * (speed + R - S);
	    time += rt;
	    rt = 0.0;

	    double t2 = (endpos - pos)/ (speed);	
	    time += t2;
	  }
	else {
	  rt -= t1;
	  time += t1;
	}
      }
      else {
	time += (endpos-pos)/ speed;
      }
      pos = endpos;
    }
    

    printf( "Case #%d: %.9f\n",te,time);
    

  }



}
