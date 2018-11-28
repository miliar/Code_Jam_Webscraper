#include<cstdio>

int c, d, tests;
int p[200], v[200];

bool test(double t) {
  double last = -1e14;
  for(int i=0;i<c;i++) {
    for(int j=0;j<v[i];j++) {
      if(last + d > p[i]) {
        if(last + d - p[i] > t)
          return 0;
        last += (double)d;
      }
      else {
        if(p[i] - last - d <= t)
          last += (double)d;
        else
          last = (double)p[i] - t;
      }
    }
  }
  return 1;
}      

int main() {
  scanf("%d",&tests);
  for(int t=1;t<=tests;t++) {
    scanf("%d %d",&c,&d);
    for(int i=0;i<c;i++)     
      scanf("%d %d",&p[i],&v[i]);
    long long a = 0; long long b = 1e13; long long c;
    for(;;) {
      if(b-a < 2) {
        if(test((double)a)) c = a;
        else c = b;
        break;
      }
      c = (a+b)/2;
      if(test((double)c)) b = c;
      else a = c;
    }
    if(c > 0 && test((double)c-0.5))
      printf("Case #%d: %I64d.5\n",t,c-1);
    else printf("Case #%d: %I64d.0\n",t,c);
  }
  return 0;
}
    
    

    
        
        
    
  
