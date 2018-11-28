#include <cstdio>
#include <string.h>

int cc, oc, n;
char c[40][5], o[40][5];

bool opp(char a, char b){
  for (int i=0; i<oc; i++)
    if (o[i][0] == a && o[i][1] == b ||
        o[i][0] == b && o[i][1] == a )
      return true;
  return false;
}

int com(char a, char b){
  for (int i=0; i<cc; i++)
    if (c[i][0] == a && c[i][1] == b ||
        c[i][0] == b && c[i][1] == a )
      return i;
  return -1;
}
 
int main(){
  int T, ca= 0;
  scanf("%d", &T);
  while (T--){
    

    char s[110];
    memset(s, 0, sizeof(s));
    memset(c, 0, sizeof(c));
    memset(o, 0, sizeof(o));

        
    scanf("%d", &cc);
    for (int i=0; i<cc; i++){
      scanf("%s", c[i]);
   //   printf("%s\n", c[i]);
    }
    scanf("%d", &oc);
    for (int i=0; i<oc; i++){
      scanf("%s", o[i]);
   //   printf("%s\n", o[i]);
    }
    scanf("%d ", &n);
    scanf("%s", s);
   // printf(" - %s\n", s);



    
    char queue[110]; memset(queue, 0, sizeof(queue));
    int qt = 0;
    queue[qt++] = s[0];
    int i= 1;
    while (i<n){
      queue[qt++] = s[i];
     // printf("%d %d\n", qt, i);
      int q = com(queue[qt-2], queue[qt-1]);
      if (q != -1){
        qt -= 2;
        queue[qt++] = c[q][2];
        i++;
        continue;
      }     
      
      for (int j=qt-2; j>=0; j--)
        if (opp(queue[j], queue[qt-1])){
          qt = 0;
          if (i+1 < n)
            queue[qt++] = s[i+1];
          i++;
          break;
        }
      i++;
    }
 //   printf("%d \n", qt);
    
 //   printf("%d\n", qt);
    printf("Case #%d: [", ++ca);
    for (int i=0; i<qt; i++){
      printf("%c", queue[i]);
      if (i!=qt-1) printf(", ");
    }
    printf("]\n");
  
  }
  return 0;
}
