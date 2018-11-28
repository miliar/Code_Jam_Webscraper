#include <stdio.h>
#include <bitset>

using namespace std;

void printState(int state)
{
     
     for(int i = 0; i < 32; i++){
         if(state & (1 << i) ) printf("1");
         else printf("0");

     }
         
     printf(" (%d) ", state);     
     printf("\n");
     
}


int main()
{
    int zz, n,k;
    scanf("%d", &zz);
    
    for( int z = 0; z < zz; z++)
    {
         
         scanf("%d%d", &n,&k);
         
         unsigned int power = 1;
         unsigned int state = k;
         int j = 0;
//         state.reset(); power.reset();     
//         power[0] = true;
/*         for( int i = 0; i < k; i++)
  
         {
              state ^= power;
              int j = 0;
         }
*/
         
         //calc power
        for(j = 0; j < k; j++)
        {
             if((state & 1<<j) == 0)
                 break;                            
        }
        
        power = (1<<(j+1)) -1;   


//         printState(state);
//         printState(power);                                       
//         printState(1<<n);


         if( power & 1<<(n) )
             printf("Case #%d: ON\n", z+1);
         else
            printf("Case #%d: OFF\n", z+1); 
         
    }    
    
    
    
    
}
