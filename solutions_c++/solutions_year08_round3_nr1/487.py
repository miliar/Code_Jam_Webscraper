#include <stdio.h>




int p,k,l,NrCazuri,litere[1020],contor,i,pozitie,adancime,j;
__int64 nr_apasari;


void quicksort(int li,int ls)
  {int h,i,j,aux;
   h=litere[(li+ls)/2];
   i=li;j=ls;

   do{
   while (litere[i]<h) i++;
   while (litere[j]>h) j--;
   if (i<=j)
       {aux=litere[i];
        litere[i++]=litere[j];
        litere[j--]=aux;
        }
   }while (i<=j);
   if (li<j) quicksort(li,j);
   if (i<ls) quicksort(i,ls);
   }





int main()
 {FILE *f,*g;


  f=fopen("intrare.in","r");
  g=fopen("iesire.out","w");
  fscanf(f,"%d",&NrCazuri);
  for (contor=1;contor<=NrCazuri;contor++)
     {
      fscanf(f,"%d %d %d",&p,&k,&l);
      for (i=1;i<=l;i++)
          fscanf(f,"%d",&litere[i]);
          
      if (l>p*k) fprintf(g,"Case #%d: Impossible\n",contor);  
           else
      {        

      quicksort(1,l);

      pozitie=l;
      adancime=0;
      nr_apasari=0;

      for (j=1;j<=l/k;j++)
        {adancime++;
         for (i=pozitie;i>pozitie-k;i--)
           nr_apasari+=adancime*litere[i];
         pozitie=i;
         }
      adancime++;  
      if (l%k!=0) for (i=1;i<=l%k;i++)
                            nr_apasari+=adancime*litere[i]; 
      fprintf(g,"Case #%d: %I64d\n",contor,nr_apasari);
      }          
      /*
      for (i=1;i<=l;i++)
          fprintf(g,"%d ",litere[i]);
      fprintf(g,"\n");
      */
      }

  fclose(f);
  fclose(g);
  return 0;
}
