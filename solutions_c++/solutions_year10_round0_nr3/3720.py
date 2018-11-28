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
          
          
          //Nolas�ts, main�gie uzst�d�ti
          
          if (peopleTotal <= k)
          {
             fprintf(out,"Case #%d: %d\n",i+1,peopleTotal*r);
             continue;
          }
          
          while (r>0)
          {
                //Ja var v�l vienu grupu ies�din�t atrakcij�
                if (emptySeats >= arr[index])
                {
                   //Ies�dina grupu
                   emptySeats -= arr[index];
                   //Iekas� naudu
                   income += arr[index];
                   //Index p�rb�da uz n�kamo grupu 
                   index = (index+1)%n;
                }
                //Ja vair�k vietas atrakcij� nav, palai� atrakciju un gatavojas uz�emt n�kamo grupu
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
