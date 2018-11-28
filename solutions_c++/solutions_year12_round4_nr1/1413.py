#include<cstdio>
#include <vector>
#include <map>

#define MAX_N 10001

using namespace std;

long long int dist[MAX_N];
long long int lung[MAX_N];

int n;
long long int D;
map<long long int,bool> *mem[MAX_N];

bool pos(int i, long long int l)
{
  //printf("liana %d lung %lld\n",i,l);
  if (dist[i]+l >= D)
    return true;
  else
  {
    if (mem[i]->find(l) == mem[i]->end())
    {
      for (int j=i+1; (j<n && dist[j]<=dist[i]+l); j++)
      {
        if (pos(j,min(dist[j]-dist[i],lung[j])))
        {
          //printf("liana %d lung %lld ce la fa prendendo %d\n",i,l,j);
          (*mem[i])[l] = true;
          return true;
        }
      }
    }
    (*mem[i])[l] = false;
    return false;
  }
}

int main()
{
  int t;
  bool possibile;
  FILE *inp, * out;
  inp = fopen("input.txt","r");
  out = fopen("output.txt","w");
  fscanf(inp,"%d",&t);
  for (int k=0; k<t; k++)
  {
    fscanf(inp,"%d",&n);
    for (int i=0; i<n; i++)
    {
      fscanf(inp,"%lld %lld",&dist[i],&lung[i]);
    }
    fscanf(inp,"%lld",&D);
    for (int i=0; i<n; i++)
      mem[i] = new map<long long int, bool>();
    printf("caso %d\n",k);
    //for (int i=0; i<n; i++)
    //printf("%lld %lld\n",dist[i],lung[i]);
    possibile = pos(0,dist[0]);
    if (possibile)
      fprintf(out,"Case #%d: YES\n",k+1);
    else
      fprintf(out,"Case #%d: NO\n",k+1);
  }
  fclose(inp);
  fclose(out);
  return 0;
}
