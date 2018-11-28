#include <stdio.h>
#include <math.h>

#define EPS 0.000000000001

#define ABS(xx) ({double xx_=(xx); (xx_>=0)?(xx_):(-xx_);})
#define DX(ss) (xp[ss]-x)
#define DY(ss) (yp[ss]-y)
#define DZ(ss) (zp[ss]-z)
#define ADX(ss) ABS(DX(ss))
#define ADY(ss) ABS(DY(ss))
#define ADZ(ss) ABS(DZ(ss))
#define DIST(ss) ({int ss_=(ss); (ADX(ss_)+ADY(ss_)+ADZ(ss_))/tp[ss_];})

int ac, cs, n;
double xp[1000], yp[1000], zp[1000], tp[1000], x, y, z, t;

int vec(int p)
{
  if ((ADX(p)>=ADY(p)) && (ADX(p)>=ADZ(p)))
    if (DX(p)>=0) return 0; else return 1;
  if (ADY(p)>=ADZ(p))
    if (DY(p)>=0) return 2; else return 3;
  if (DZ(p)>=0) return 4;
  return 5;    
}

double dist(int p)
{
  if ((ADX(p)>=ADY(p)) && (ADX(p)>=ADZ(p)))
    return ADX(p);
  if (ADY(p)>=ADZ(p))
    return ADY(p);
  return ADZ(p);
}

int main()
{
  scanf(" %d ", &ac);
  for(cs=1; cs<=ac; cs++)
    {
      scanf(" %d ", &n);
      for(int i=0; i<n; i++)
	scanf(" %lf %lf %lf %lf ", xp+i, yp+i, zp+i, tp+i);
      x=xp[0]; y=yp[0]; z=zp[0]; t=0;
      while(n>1)
	{
	  double dm=0;
	  for(int vv=0; vv<=5; vv+=2)
	    {
	      int v=vv;
	      t=0;
	      int dummy=0;
	      double d;
	      for(int i=0; i<n; i++)
		{
		  double td=DIST(i);
		  if (td>t)
		    {
		      t=td;
		      dummy=i;
		    }
		}
	      switch(v)
		{
		case 0:
		  d=ADX(dummy);
		  if (DX(dummy)<0) v++;
		  break;
		case 2:
		  d=ADY(dummy);
		  if (DY(dummy)<0) v++;
		  break;
		case 4:
		  d=ADZ(dummy);
		  if (DZ(dummy)<0) v++;
		  break;
		}
	      for(int i=0; i<n; i++)
		if (i!=dummy)
		  {
		    switch(v)
		      {
		      case 0:
			if (DX(i)>EPS)
			  { if (d>ADX(i)) d=ADX(i); }
			else
			  {
			    double tt=(t-DIST(i))*tp[i]/2;
			    if (d>tt) d=tt;
			  }
			break;
		      case 1:
			if (-DX(i)>EPS)
			  { if (d>ADX(i)) d=ADX(i); }
			else
			  {
			    double tt=(t-DIST(i))*tp[i]/2;
			    if (d>tt) d=tt;
			  }
			break;
		      case 2:
			if (DY(i)>EPS)
			  { if (d>ADY(i)) d=ADY(i); }
			else
			  {
			    double tt=(t-DIST(i))*tp[i]/2;
			    if (d>tt) d=tt;
			  }
			break;
		      case 3:
			if (-DY(i)>EPS)
			  { if (d>ADY(i)) d=ADY(i); }
			else
			  {
			    double tt=(t-DIST(i))*tp[i]/2;
			    if (d>tt) d=tt;
			  }
			break;
		      case 4:
			if (DZ(i)>EPS)
			  { if (d>ADZ(i)) d=ADZ(i); }
			else
			  {
			    double tt=(t-DIST(i))*tp[i]/2;
			    if (d>tt) d=tt;
			  }
			break;
		      case 5:
			if (-DZ(i)>EPS)
			  { if (d>ADZ(i)) d=ADZ(i); }
			else
			  {
			    double tt=(t-DIST(i))*tp[i]/2;
			    if (d>tt) d=tt;
			  }
			break;
		      }
		  }
	      // printf("%f %f %f %f %f\n", x, y, z, t, d);
	      switch(v)
		{
		case 0: x+=d; break;
		case 1: x-=d; break;
		case 2: y+=d; break;
		case 3: y-=d; break;
		case 4: z+=d; break;
		case 5: z-=d; break;
		}
	      if (d>dm) dm=d;
	    }
	  if (dm<0.000000000001) break;
	}
      printf("Case #%d: %.6f\n", cs, t);
    }
  return 0;
}
