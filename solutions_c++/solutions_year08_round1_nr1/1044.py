#include <stdio.h>

int findlow(int* x, bool* xu, unsigned int n)
{
  int num=100001;
  unsigned int i=0;
  unsigned int used=0;

  while (i<n)
  {
    if (num>x[i] && xu[i]==0)
    {
      num=x[i];
      used=i;
    }
    i++;
  }

  xu[used]=1;

  return num;
}

int findhigh(int* y, bool* yu, unsigned int n)
{
  int num=-100001;
  unsigned int i=0;
  unsigned int used=0;

  while (i<n)
  {
    if (num<y[i] && yu[i]==0)
    {
      num=y[i];
      used=i;
    }
    i++;
  }

  yu[used]=1;

  return num;
}

int main (int argc, char** argv)
{
  FILE* in;
  FILE* out;
  in=fopen("A-small.in", "rb");
  out=fopen("A-small.out", "wb+");

  unsigned int t;

  fscanf(in, "%u\n", &t);
  for (unsigned int i=0; i<t; i++)
  {
    unsigned int n;
    int x[800], y[800];
    bool xu[800], yu[800];
    fscanf(in, "%u\n", &n);

    for (unsigned int j=0; j<n-1; j++)
    {
      fscanf(in, "%d ", &x[j]);
      xu[j]=0;
    }
    fscanf(in, "%d\n", &x[n-1]);
    xu[n-1]=0;

    for (unsigned int j=0; j<n-1; j++)
    {
      fscanf(in, "%d ", &y[j]);
      yu[j]=0;
    }
    fscanf(in, "%d\n", &y[n-1]);
    yu[n-1]=0;

    int num=0;

    for (unsigned int j=0; j<n; j++)
    {
      num+=findlow(x, xu, n)*findhigh(y, yu, n);
/*
for (unsigned int k=0; k<n; k++)    printf("%d	", x[k]);
printf("\n");
for (unsigned int k=0; k<n; k++)    printf("%d	", xu[k]);
printf("\n");
for (unsigned int k=0; k<n; k++)    printf("%d	", y[k]);
printf("\n");
for (unsigned int k=0; k<n; k++)    printf("%d	", yu[k]);
printf("\n");
*/
    }

    fprintf(out, "Case #%u: %d\n", i+1, num);
  }

  fprintf(out, "\n");

  fclose(in);
  fclose(out);
  return 0;
}
