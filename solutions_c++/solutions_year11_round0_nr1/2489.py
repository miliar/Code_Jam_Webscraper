#include <stdio.h>

typedef struct {
  int robot;
  int but;
}data;

data info[101];

int n;  

int diff (int v1 , int v2) {
  if (v1 > v2) return v1-v2;
  return v2 - v1;
}

int solution () {
  int pos [3];
  int time [3];
  
  int total = 0;
  
  pos [1] = 1; pos [2] = 1;
  time [1] = 0; time[2] = 0;
  
  
  for (int i = 1; i <= n; i++) {
    int tdiff = total - time[info[i].robot];
    int pdiff =  diff (pos[info[i].robot] , info[i].but);
    
    if (tdiff >= pdiff) {
      pos [info[i].robot] = info[i].but;
      time [info[i].robot] = total + 1;
      total++;
    }
    else {
      pos [info[i].robot] = info [i].but;
      time [info[i].robot] = total + (pdiff - tdiff + 1);
      total = time[info[i].robot];
    }
  }
  
  return total;
}

int main () {
  FILE *in = fopen ("A-large.in","r");
  FILE *out = fopen ("a.out","w");
  
  int t;
  
  fscanf (in,"%d",&t);
  
  for (int i = 1; i <= t; i++) {
    fscanf (in,"%d", &n);
    char temp;
    
    for (int j = 1; j <= n; j++) {      
      fscanf (in,"%c",&temp);
      char robot;
      int button;
      fscanf (in,"%c %d",&temp,&button);
      
      if (temp == 'O') 
        info [j].robot = 1;              
      else
        info [j].robot = 2;      
      
      info [j].but = button;
    }
    
    fscanf (in,"%c",&temp);
    
    int s = solution ();
    
    if (i < t)
      fprintf (out,"Case #%d: %d\n",i,s);
    else 
      fprintf (out,"Case #%d: %d",i,s);
  }
  
  fclose (in);
  fclose (out);
  
  return 0;
}
