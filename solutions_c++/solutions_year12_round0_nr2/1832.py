#include<stdio.h>

using namespace std;

FILE *in, *out;
int t;

int dati[200][200];

int main()
{
  int n, p, s,temp;
  int tot = 0;
  in = fopen("input.txt", "r");
  fscanf(in,"%d",&t);
  for (int volta=0; volta<t; volta++)
  {
    fscanf(in,"%d %d %d",&n,&s,&p);
    dati[volta][0] = n;
    dati[volta][1] = s;
    dati[volta][2] = p;
    for (int i=0; i<n; i++)
    {
      fscanf(in,"%d",&dati[volta][i+3]);
    }
  }
  out = fopen("output.txt", "w");
  for (int volta=0; volta<t; volta++)
  {
    n = dati[volta][0];
    s = dati[volta][1];
    p = dati[volta][2];
    tot = 0;
    if (p!=0)
    {
      for (int i=0; i<n; i++)
      {
	temp = dati[volta][i+3];
	if (temp >= 3*p-2 && p-1>=0)
	  tot++;
	else if ((temp >= 3*p-4) && s>0 && p-2>=0)
	{
	  s--;
	  tot++;
	}
      }
    }
    else
      tot = n;
    fprintf(out,"Case #%d: %d\n",volta+1,tot);
  }
  fclose(in);
  fclose(out);
}
