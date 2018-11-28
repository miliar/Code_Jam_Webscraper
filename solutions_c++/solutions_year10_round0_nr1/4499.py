#include <stdio.h>

int main(void)
{
    int db = 0;
    int temp = 0;
    int i = 0;
    int n = 0;
    int k = 0;
    int snappers[30];
    int states[30];
    scanf("%d", &temp);
    db = 0;
    int flag = 1;
    while(fscanf(stdin,"%d %d\n",&n, &k)==2)
    {
       db = db + 1;
       int j = 0;
      // int jmax = 0;
       for(i = 0; i< 30; i++) snappers[i] = 0; //zeros for starting position
       states[0] = 1;
       for(i = 1; i< 30; i++) states[i] = 0; //zeros for starting position
       for(i=0; i<k;i++) 
       { 
          for(j=0;j<n;j++)
          {
             if(states[j])   snappers[j] = !snappers[j];
          }
          flag = 1;
         for(j=1; j<n;j++)
           if(states[j-1] && snappers[j-1] &&flag) states[j] = 1; else {flag = 0; states[j] = 0;}
       }
       int flag = 1;
       for(i=0;flag && (i<n);i++)
         if(!snappers[i]) flag = 0;
       printf("Case #%d: %s\n",db, flag?"ON":"OFF");
    }
    
    return 0;
}
