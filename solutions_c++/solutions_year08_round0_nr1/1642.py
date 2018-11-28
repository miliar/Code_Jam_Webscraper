#include <stdio.h>

unsigned char find (char haystack[10][100], char* needle)
{
  unsigned int i=0;
  while (i<100)
  {
    unsigned int j=0;
    while (haystack[i][j]==needle[j] && haystack[i][j]!=0 && needle[j]!=0)
    {
      j++;
    }
    if (haystack[i][j]==needle[j]) return i+1;
    i++;
  }

  return 0;
}

int main (int argc, char** argv)
{
  FILE* in;
  FILE* out;
  in=fopen("A-large.in", "rb");
  out=fopen("A-large.out", "wb+");

  unsigned int n, s, q;
  char engine[100][100];
  char input[100];
  bool use[100];
  unsigned int query[1000];

  fscanf(in, "%u\n", &n);
  for (unsigned int i=0; i<n; i++)
  {
    fscanf(in, "%u\n", &s);
    for (unsigned int j=0; j<s; j++)
    {
      fscanf(in, "%[^\n]\n", engine[j]);
      use[j]=1;
    }
    fscanf(in, "%u\n", &q);
    for (unsigned int j=0; j<q; j++)
    {
      fscanf(in, "%[^\n]\n", input);
      query[j]=find(engine, input);
    }
    unsigned int ret=0;

    for (unsigned int j=0; j<q; j++)
    {
      use[query[j]-1]=0;
      char usage=0;
      for (unsigned int k=0; k<s; k++)
      {
        usage+=use[k];
      }
      if (usage==0)
      {
        for (unsigned int k=0; k<s; k++) use[k]=1;
        ret++;
        j--;
      }
    }
    fprintf(out, "Case #%u: %u\n", i+1, ret);
  }

  fclose(in);
  fclose(out);
  return 0;
}
