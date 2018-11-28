#include <stdio.h>

FILE *fin = fopen ("A-small-attempt0.in","r");
FILE *fout = fopen ("a.out","w");

char mapping[26] ={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main () {
  int t;
  fscanf (fin,"%d",&t);
    
  char temp;
        
  fscanf (fin,"%c",&temp);
  
  for (int i = 1; i <= t; i++) {    
    fprintf (fout,"Case #%d: ",i);
    
    while (fscanf(fin, "%c", &temp) != EOF && temp != '\n') {
      char printTo = temp;
      if (temp != ' ')
        printTo = mapping[temp-'a'];
        
      fprintf (fout,"%c",printTo);          
    }
    
    fprintf (fout,"\n");
  }
  
  return 0;
}
