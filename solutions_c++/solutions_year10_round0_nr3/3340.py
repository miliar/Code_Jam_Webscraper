#include <iostream>
using namespace std;

int main()
{
    int i,j,k;
    int casenum;
    int size, round, groupnum;
    int group[1000];
    int result;
    int begin, end, actualsize,playnum;
    
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C.txt","w",stdout);
    
    scanf("%d",&casenum);
    k=0;
    
    for(k=0;k<casenum;k++)
    {
                     scanf("%d%d%d",&round,&size,&groupnum);
                     result =0;

                     for(i =0;i<groupnum;i++)
                     {
                           scanf("%d",&group[i]);
                     }
                     begin = 0;
                     end = groupnum-1;

                   for(i=0;i<round;i++)
                   {
                          actualsize = 0;
                          playnum = 0;
                          while(actualsize<=size&&playnum<=groupnum)
                          {
                             actualsize = actualsize + group[begin];
                             result = result + group[begin];
                             begin++;end++;playnum++;
                             if(begin>=groupnum)begin=begin-groupnum;
                             if(end>=groupnum) end = end - groupnum;                                                                           
                          }
                          begin--;
                          end--;
                          if(begin<0)begin = begin+groupnum;
                          if(end<0)end = end+groupnum;
                          result = result - group[begin];             
                   }
                   printf("Case #%d: %d\n",k+1,result);
    }
    return 0;
}
