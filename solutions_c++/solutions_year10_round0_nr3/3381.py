#include <stdio.h>

typedef struct{
  int value;
  int round;
}round_data;

int r,k,n;
int groups[1001];

round_data partial [1001];

int solve () {
  for (int j = 1; j <= n; j++) {    
    partial[j].round = 0;
  }
    
  partial[1].value = 0;
  partial[1].round = 1;
    
  int euros = 0;
    
  int index = 1;
  
  int r_counter = 1;  
  int p_sum = 0;
  
  while (r >= r_counter) {                
  
    p_sum = 0;
    
    int last_index = index;
    
    while (p_sum + groups[index] <= k && (index!=last_index || p_sum == 0)) {
      p_sum += groups[index];
      index++;
      if (index == n+1) index = 1;
    }
    
    euros += p_sum;        
    
    r_counter++;
    
    if (partial[index].round != 0) {
      int dif_v = euros - partial[index].value;
      int dif_r = r_counter - partial[index].round;
      
      int l_int = (r - r_counter + 1)/dif_r;
      
      euros += dif_v * (l_int);
      
      int rest = (r - r_counter + 1)%dif_r;   
      
      r_counter = r - rest + 1;                   
    }
    else {
      partial[index].value = euros;
      partial[index].round = r_counter;
    }
  }
  
  return euros;
}

int main () {
  FILE *fin = fopen("C-small-attempt0.in","r");
  FILE *fout = fopen("C-small.out","w");
  
  int t;
  
  fscanf (fin,"%d",&t);
  for (int i = 1; i <= t; i++) {
      fscanf (fin,"%d %d %d",&r,&k,&n);
      
      for (int j = 1; j <= n; j++) 
        fscanf (fin,"%d",&groups[j]);
        
      int result = solve ();
      
      fprintf (fout,"Case #%d: %d\n",i,result);
  }
  
  fclose (fin);
  fclose (fout);
  return 0;
}
