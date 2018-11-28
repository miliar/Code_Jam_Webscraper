#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int t, n, k; 
    //int *power;
    //int *stat;
    int power[11];
    int stat[11]; 

    /*
    4
    1 0
    1 1
    4 0
    4 47
    */
    
  //freopen("in1.txt", "r", stdin);
  //freopen("out.txt", "w", stdout);
    
    scanf("%d", &t);
    
    for(int c=1; c<=t; c++)
    {
      scanf("%d %d", &n, &k);
      printf("Case #%d: ", c);
      
//      power = (int *) malloc(sizeof(int)*n);
  //    stat  = (int *) malloc(sizeof(int)*n);
      
      memset(power, 0, sizeof(int)*11);
      memset(stat, 0, sizeof(int)*11);
      
      power[0] = 1;
      stat[0] = 0;
      
      while (k-->0)
      { 
       
        if(power[0])
           stat[0] = !stat[0];
        
        for(int j=1; j<n; j++)
        {
          if(power[j])
          stat[j] =  !stat[j];

          power[j] = power[j-1] && stat[j-1];
        }
        
      
      }
      
      if (power[n-1] && stat[n-1])
         printf("ON");
      else
         printf("OFF");
         
      printf("\n");
      
    }
    
    //system("pause");
    return 0;
}
