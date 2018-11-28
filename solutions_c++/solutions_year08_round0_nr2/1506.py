//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <stdio.h>
#include <vector>
#include <algorithm>


using namespace std;

int main(int argc, char* argv[])
{
  FILE *ent, *sal;
  ent = fopen("B-large.in","rt");
  sal = fopen("SalidaFinal.out","wt");

  vector <int> AEnt;
  vector <int> ASal;

  vector <int> BEnt;
  vector <int> BSal;
  int hr,min,i, j, n, t,conta, contb,NA,NB;
  int inda, indb;

  fscanf(ent,"%d\n",&n);
  for(i=0;i<n;i++)
  {
    fscanf(ent,"%d",&t);
    fscanf(ent,"%d %d",&NA,&NB);
    AEnt.resize(NA);
    ASal.resize(NA);

    BEnt.resize(NB);
    BSal.resize(NB);

    //Lleno las entradas
    for(j=0;j<NA;j++)
    {
      fscanf(ent,"%d:%d ",&hr,&min);
      AEnt[j] = hr*60+min;
      fscanf(ent,"%d:%d",&hr,&min);
      ASal[j] = hr*60+min;
    }
    //Lleno las salidas
    for(j=0;j<NB;j++)
    {
      fscanf(ent,"%d:%d ",&hr,&min);
      BEnt[j] = hr*60+min;
      fscanf(ent,"%d:%d",&hr,&min);
      BSal[j] = hr*60+min;
    }

    sort(AEnt.begin(),AEnt.end(), less<int>() );
    sort(ASal.begin(),ASal.end(), less<int>() );

    sort(BEnt.begin(),BEnt.end(), less<int>() );
    sort(BSal.begin(),BSal.end(), less<int>() );

      
    conta = 0;
    contb = 0;
    indb = 0;
    if(NB != 0)
    {
      for(inda = 0; inda < NA ; inda++)
      {
        if(BSal[indb] + t > AEnt[inda])
          conta++;
        else
          indb++;
        if(indb==NB)
        {
          conta+=NA-inda-1;
          break;
        }
      }
    }
    else
      conta=NA;

    inda = 0;
    if(NA != 0)
    {
      for(indb = 0; indb < NB ; indb++)
      {
        if(ASal[inda] + t > BEnt[indb])
          contb++;
        else
          inda++; 
        if(inda==NA)
        {
          contb+=NB-indb-1;
          break;
        }
      }
    }
    else
      contb = NB;

    printf("Case #%d: %d %d\n",i+1,conta, contb);
    fprintf(sal,"Case #%d: %d %d\n",i+1,conta, contb);
  }
  fclose(ent);
  fclose(sal);
  return 0;
}
//---------------------------------------------------------------------------
