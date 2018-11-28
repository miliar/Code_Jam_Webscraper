#include <cstdio>
#include <string.h>

struct r{
  double wp, op, oop, rpi;
  int game;
  r(){};
};
r p[110];

int main(){
  int T, ca = 0;
  scanf("%d", &T);
  while (T--){
    int n;
    scanf("%d", &n);
    
    char s[10], a[110][110];
    gets(s);
    memset(a, 0, sizeof(a));
    memset(p, 0, sizeof(p));
    for (int i=0; i<n; i++)
      gets(a[i]);

      
    for (int i=0; i<n; i++){
      int game = 0, win = 0;
      for (int j=0; j<n; j++)
        if (a[i][j] == '0')
          game++;
        else if (a[i][j] == '1'){
          game++;
          win++;
        }
      p[i].game = game;
      p[i].wp = win;
      p[i].wp /= game;
    }
    
    for (int k=0; k<n; k++){
        for (int i=0; i<n; i++)
          if (a[k][i] != '.'){
            int game = 0, win = 0;
            for (int j=0; j<n; j++)
              if (j!=k){
                if (a[i][j] == '0')
                  game++;
                else if (a[i][j] == '1'){
                  game++;
                  win++;
                }
              }    
            p[k].op += (win*1.0) / game;
          }
      p[k].op /= p[k].game;
    }
    

    for (int x=0; x<n; x++){
      p[x].oop = 0;
      for (int i=0; i<n; i++)
        if (a[x][i] != '.') {
     //     printf("--- %d\n", i);
          p[x].oop += p[i].op;
        }
    //  printf("%d %lf %d\n", x, p[x].oop, p[x].game);
      p[x].oop /= p[x].game;
    }
 
    
    for (int i=0; i<n; i++){
      p[i].rpi = 0.25*p[i].wp + 0.5*p[i].op + 0.25*p[i].oop;
    }
    
    printf("Case #%d:\n", ++ca);
    for (int i=0; i<n; i++){
     // printf("%lf %lf %lf  ", p[i].wp, p[i].op, p[i].oop);
      printf("%.12lf\n", p[i].rpi);
    }
  }
  return 0;
}
