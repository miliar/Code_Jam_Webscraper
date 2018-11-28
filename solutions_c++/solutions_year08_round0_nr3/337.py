#include <stdio.h>
#include <math.h>
#include <assert.h>

#define fp double
#define P 10000
#define PI 3.1415926535897932384626433832795
#define min(a, b) ((a)<(b)? (a): (b))

fp f, R, t, r, g;
fp g2f;
fp al;
fp Rtf;
fp Rtf2;

#define is(x,y) ((x)*(x)+(y)*(y)<=(Rtf2))

fp comp(fp x0, fp x1, fp y0, fp y1)
{
#define D 10
  //assert(is(x0, y0));
  //assert(!is(x1, y1));
  fp s= 0;
  //if((x1-x0)!=(y1-y0)) { printf("%lf %lf   %lf %lf\n", x1, x0, y1, y0);  }
  fp d= (x1-x0)/D;
  if(d<5e-8) return 0;
  for(int i=0; i<D; i++) {
      fp x=x0+i*d;
    for(int j=0; j<D; j++) {
      fp y=y0+j*d;
      if(!is(x,y)) continue;
      if(is(x+d, y+d)) { s+= d*d; continue; }
      s+= comp(x,x+d,y,y+d);
    }
  }
  return s;
}





fp doit(void)
{
  fp res;
  //fp f, R, t, r, g;
  scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
  //
  
  f= f/R;
  t= t/R;
  r= r/R;
  g= g/R;
  R= 1;
  g2f= g/2-f;
  al= r+g/2;
  Rtf= (R-t-f);
  Rtf2=(R-t-f)*(R-t-f);
  if(g2f<=0) return 1;
  if((R-t-f)<=0) return 1;
  int blocks= 0, hblocks= 0;
  fp surf= 0;
  
  int kx=0, ky= 0;
  fp x0, x1, y0, y1;
  while(is(al*(1.+2.*(fp)kx)-g2f, al*(1.+0.)-g2f)) {
    while(ky<=kx && is(x0=al*(1.+2.*(fp)kx)-g2f, y0=al*(1.+2.*(fp)ky)-g2f)) {
      if(is(x1=al*(1.+2.*(fp)kx)+g2f, y1=al*(1.+2.*(fp)ky)+g2f))
        if(kx==ky) hblocks++; else blocks++;
      else {
        // Compute surface for the block..
        surf+= comp(x0, x1, y0, y1)*(kx==ky? 0.5: 1);     
      }
      ky++;
    }
    ky= 0;
    kx++;
  }
  //printf("%d blocks, %f surf", blocks, surf); 
  return 1-8*(((hblocks+2*blocks)*2*g2f*g2f)+surf*1)/PI;
}

main()
{
  int n;
  scanf("%d", &n);
  for(int in=1; in<=n; in++) {
    printf("Case #%d: %lf\n", in, doit());
  }
}




