#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<inttypes.h>
#include<string.h>

int main()
{ 
    int numberCases;
    int numberPeople;
    int good;
    int average;
    int bad;
    int s;
    int score;
    int min;
    int ans;
    
    scanf("%d",&numberCases);
    for(int i=0;i<numberCases;i++)
    {
            good = 0;
            average = 0;
            bad = 0;
            ans =0;
            scanf("%d",&numberPeople);
            scanf("%d",&s);
            scanf("%d",&min);
            min = (3*min) - 2;
            for(int j=0;j<numberPeople;j++)
            {       
                    scanf("%d",&score);
                    if(score>=min)
                                  good++;
                    else if(score >= (min-2) && (min-2) > 0)
                    {
                          average++;     
                    }
                    else
                          bad++;
                                 
            }
            
          if(s>=average)
                        ans = good + average;
          else
                        ans =good + s;
          
          printf("Case #%d: %d\n",i+1,ans);
    }

  return 0;    
}
