#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
int t,q,a,b,i;
double x,p1=1.0,p2=1.0,ans,curr;

int main()
{
  FILE *in=fopen("A-small-attempt0.in","r");
  FILE *out=fopen("A-small-attempt0.out","w");
  fscanf(in,"%d",& t);
  for(q=1;q<=t;q++)
  {
      p1=1.0;
      p2=1.0;
      fscanf(in,"%d%d",& a,& b);
  for(i=1;i<=a;i++)
  {
    fscanf(in,"%lf",& x);
    p1*=x;
    if (i==a) p2*=(1.0-x);
    else p2*=x;
  }

  ans=2.0+(double)b;//give up

  curr=p1*(double)(b-a+1)+(1.0-p1)*(double)(b-a+1+b+1);//finish
  if (curr < ans) ans=curr;

  curr=(p1+p2)*(double)(2+b-a+1)+(1.0-p1-p2)*(double)(3+b-a+1+b);//backspace once
  if (curr < ans) ans=curr;

  fprintf(out,"Case #%d: %lf\n", q, ans);

  }
  fclose(in);
  fclose(out);
return 0;
}
