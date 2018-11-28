#include <stdio.h>
#include <stdlib.h>

int main (int argc, char** argv)
{
  FILE* in;
  FILE* out;
  in=fopen("B-large.in", "rb");
  out=fopen("B-large.out", "wb+");

  unsigned int n;
  unsigned int go[400];
  bool way[200];
  bool done[200];

  fscanf(in, "%u\n", &n);
  for (unsigned int i=0; i<n; i++)
  {
    unsigned int t, a, b;
    fscanf(in, "%u\n%u %u\n", &t, &a, &b);
    for (unsigned int j=0; j<a+b; j++)
    {
      unsigned int h1, m1, h2, m2;
      fscanf(in, "%u:%u %u:%u\n", &h1, &m1, &h2, &m2);
      go[2*j]=h1*60+m1;
      go[2*j+1]=h2*60+m2;
      way[j]=j<a?0:1;
      done[j]=0;
    }

    for (unsigned int j=1; j<a+b; j++)
    {
      if (go[2*j]<go[2*j-2])
      {
        unsigned int storedep=go[2*j];
        unsigned int storearr=go[2*j+1];
        bool storedir=way[j];
        go[2*j]=go[2*j-2];
        go[2*j+1]=go[2*j-1];
        go[2*j-2]=storedep;
        go[2*j-1]=storearr;
        way[j]=way[j-1];
        way[j-1]=storedir;
        j=0;
      }
    }

    unsigned int arr;
    bool from;
    unsigned int outputa=0;
    unsigned int outputb=0;
    unsigned int trains=a+b;

    while (trains>0)
    {
      for (unsigned int j=0; j<a+b; j++)
      {
        arr=go[2*j+1];
        from=way[j];
        if (done[j]==0)
        {
          done[j]=1;
          trains--;
          break;
        }
      }

      if (from) outputb++; else outputa++;

      for (unsigned int j=0; j<a+b; j++)
      {
        if (done[j]==0 && from!=way[j] && go[2*j]>=arr+t)
        {
          arr=go[2*j+1];
          done[j]=1;
          from=!from;
          j=0;
          trains--;
        }
      }
      from=!from;
    }

    fprintf(out, "Case #%u: %u %u\n", i+1, outputa, outputb);
  }

  fclose(in);
  fclose(out);
  return 0;
}
