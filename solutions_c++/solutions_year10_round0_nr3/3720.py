#include <stdio.h>
#include <cmath>

main()
{
      FILE * in = fopen("B-small.in", "r");
      FILE * out = fopen("B-small.out","w");
      
      int total;
      fscanf(in,"%d",&total);
      //printf("%d\n",total);
      
      int* arr;
      
      unsigned long int r, k, n;
      int index, emptySeats, income, peopleTotal;
      
      for (int i = 0; i < total; i++)
      {
          fscanf(in, "%d %d %d", &r, &k, &n);
          printf( "%d %d %d\n", r, k, n);
          
          arr = new int[n];
          index = 0;
          income = 0;
          emptySeats = k;
          peopleTotal = 0;
          
          printf("[ ");
          for (int j = 0; j < n; j++)
          {
              fscanf(in, "%d", &arr[j]);
              printf("%d ",arr[j]);
              peopleTotal+=arr[j];
          }
          printf("]\n");
          
          
          //Nolasîts, mainîgie uzstâdîti
          
          if (peopleTotal <= k)
          {
             fprintf(out,"Case #%d: %d\n",i+1,peopleTotal*r);
             continue;
          }
          
          while (r>0)
          {
                //Ja var vçl vienu grupu iesçdinât atrakcijâ
                if (emptySeats >= arr[index])
                {
                   //Iesçdina grupu
                   emptySeats -= arr[index];
                   //Iekasç naudu
                   income += arr[index];
                   //Index pârbîda uz nâkamo grupu 
                   index = (index+1)%n;
                }
                //Ja vairâk vietas atrakcijâ nav, palaiþ atrakciju un gatavojas uzòemt nâkamo grupu
                else
                {
                    emptySeats = k;
                    r--;
                }
          }
          
          fprintf(out,"Case #%d: %d\n",i+1,income);
          
          delete arr;
      }
      
      scanf("a");
}
