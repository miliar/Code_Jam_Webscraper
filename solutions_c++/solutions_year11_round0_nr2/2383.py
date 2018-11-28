#include <stdio.h>

int combines [26][26];

bool clearers [26][26];

int combs;
int clears;
int n;

char letters[100];
int counting [26];

void clear_board () {
  for (int i =0; i < 26; i++) {
    counting [i] = 0;
    for (int j = 0; j < 26; j++) {
      combines[i][j] = -1;
      clearers [i][j] = false;
    }
  }
}

char putting [100];
int index = 0;

int solution () {
  putting [0] = letters [0]; index = 0;
  
  counting [letters[0]-65]++;
  
  int i = 1;
  while (i < n) {
    index++;
    putting [index] = letters [i];
    counting [letters[i]-65]++;
    
    bool combine = false;
    
    if (index > 0) {
      int id1 = putting [index-1] - 65;
      int id2 = putting [index] - 65;        
    
      if (combines [id1][id2] != -1) {
        char let2 = combines[id1][id2] + 65;
      
        counting [putting[index-1]-65]--;
        counting [putting[index]-65]--;  
      
        putting [index-1] = let2; 
        index--;
      
        combine = true;
      }    
    }
    
    if (index > 0 && !combine) {
      int id1 = putting[index] - 65;
      for (int k = 0; k < 26; k++) {
        if (clearers [id1][k]) {
          if (counting [k] > 0) {
            index = -1;
            
            for (int q = 0; q < 26; q++) counting[q] = 0;                        
            
            break;
          }
        }
      }
    }    
    
    i++;
  }
  
  return 0;
}

int main () {
  FILE *in = fopen ("B-large.in","r");
  FILE *out = fopen ("b.out","w");
  
  int t;
  
  fscanf (in,"%d",&t);
  
  for (int i = 1; i <= t; i++) {
    clear_board ();
    
    fscanf (in,"%d", &combs);        
    
    char temp,l1,l2,l3;
    
    for (int j = 1; j <= combs; j++) {
      fscanf (in,"%c %c %c %c",&temp,&l1,&l2,&l3);

      combines[l1-65][l2-65] = l3-65;
      combines[l2-65][l1-65] = l3-65;
    }      
    
    fscanf (in,"%d",&clears); 
    
    for (int j = 1; j <= clears; j++) {
      fscanf (in,"%c %c %c",&temp,&l1,&l2);
      
      clearers [l1-65][l2-65] = true;
      clearers [l2-65][l1-65] = true;
    }
    
    fscanf (in,"%d",&n);
    
    fscanf (in,"%c",&temp);
    
    for (int j = 0; j < n; j++) {
      fscanf (in,"%c",&letters[j]);
    }        
    
    solution ();
        
    
    fprintf (out,"Case #%d: ",i);
    
    
    fprintf (out,"[");
    for (int j = 0; j <= index; j++) {
      if (j < index)
        fprintf (out,"%c, ",putting[j]);
      else
        fprintf (out,"%c",putting[j]);
    }
    
    fprintf (out,"]");
    
    if (i < t) fprintf (out,"\n");
  }
  
  fclose (in);
  fclose (out);
  
  return 0;
}
