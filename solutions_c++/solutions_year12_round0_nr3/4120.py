#include <cstdio>
#include <cstring>
using namespace std;

int sq[10] = {1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000};

int getws(int num)
{
    int weishu = 1;
    while(num >= 10)
    {
           weishu ++;
           num = num / 10;
    }   
    return weishu;
}
int main()
{
    FILE *fin, *fout;
    fin = fopen("C-small-attempt0.in", "r");
    fout = fopen("out.txt", "w");
    
    int i,t,a,b;
    fscanf(fin, "%d", &t);
    for(i = 1; i <= t; i++)
    {
          fscanf(fin, "%d%d", &a, &b);
          int num, total = 0;
          
          for(num = a; num <= b; num++)
          {
               int ws = getws(num);
               int j, num1 ,num2 = num;
               int nn[8] = {0,0,0,0,0,0,0,0};
               int mm = 0;
               for(j = 1; j <= ws; j++)
               {
                     int tail = num2 % 10;
                     num1 = num2 / 10 + tail * sq[ws - 1];
                     if(tail != 0)
                     {     
                          if((num1 <= b) && (num1 >= a) && (num != num1) && (num1 != nn[0]) && (num1 != nn[1]) && 
                          (num1 != nn[2]) && (num1 != nn[3]) && (num1 != nn[4]) && (num1 != nn[5]) && 
                          (num1 != nn[6]) && (num1 != nn[7]))
                          {
                              total ++;    
                          }             
                     }
                     num2 = num1;
                     nn[mm++] = num1;
               }
          }
          total /= 2;
          fprintf(fout ,"Case #%d: %d\n", i, total);   
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
