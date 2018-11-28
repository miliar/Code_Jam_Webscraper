//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <string>
#include <vector>
#include <stdio>
#include <map>
using namespace std;

vector<int> pet;
map <string,int> servidores;


int sig (int ind,int lim);

int main(int argc, char* argv[])
{
  int n,s,q,i,j;
  int cont = 0, indice = 0;

  FILE *sal,*ent;
  sal = fopen("Salida.txt","wt");
  ent = fopen("A-small-attempt0.in","rt");

  fscanf(ent,"%d",&n);
  char buf[200];
  for(i=0;i<n;i++)
  {
    fscanf(ent,"%d",&s);
    servidores.clear();
    fflush(stdin);
    for(j=0;j<s;j++)
    {
      fgets(buf,200,ent);
      servidores.insert(make_pair(buf, j));
    }

    fscanf(ent,"%d",&q);
    pet.resize(q);
    fflush(stdin);

    for(j=0;j<q;j++)
    {
      fgets(buf,200,ent);
      pet[j] = servidores.find(buf)->second;
    }

    indice = -1;
    cont = 0;
    do
    {
      indice = sig(indice+1, q) ;
      cont++;
    }while(indice >=0);
    cont--;
    fprintf(sal,"Case #%d: %d\n",n,cont);
    printf("Case #%d: %d\n",i+1,cont);
  }
  fclose(ent);
  fclose(sal);
  return 0;
}
//---------------------------------------------------------------------------
int sig (int ind,int lim)
{
  int banderas[6] = {0},res;
  unsigned int sum = 0,tam = servidores.size()-1;
  bool f = true;

  for(res = ind; res < lim; res++)
  {
    if(banderas[ pet[res] ]==0)
    {
      if(sum == tam)
      {
        f = false;
        break;
      }
      banderas[ pet[res] ] = 1;
      sum++;
    }
  }
  if(f)
    return -1;
  return res;
}
