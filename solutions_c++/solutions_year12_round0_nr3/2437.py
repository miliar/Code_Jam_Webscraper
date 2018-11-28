#include <cstdlib>
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int cur_base;

int get_n(int x, int b)
{
    int y = x;
    int res = 0;
    y = y / 10 + (y % 10) * cur_base;
    while (y != x)
    {
          if (y > x && y <= b)
             ++res;
          y = y / 10 + (y % 10) * cur_base;
    }
    
    return res;
}

int main(int argc, char *argv[])
{
     //FILE* fp = fopen("D:\\Arthur\\Dev-Cpp\\Projects\\Code Jam\\C.txt", "r");
     FILE* fp = fopen("D:\\Arthur\\Dev-Cpp\\Projects\\Code Jam\\C3.in", "r");
     FILE* o_fp = fopen("D:\\Arthur\\Dev-Cpp\\Projects\\Code Jam\\C_out.txt", "w");
    int t;
    fscanf(fp, "%d", &t);
    //printf("%d\n", n);
    //system("PAUSE");
    for (int i = 1; i <=t; ++i)
    {
        int a, b;
        fscanf(fp, "%d%d", &a, &b);
        
        int y = a;
        cur_base = 1;
        while(y)
        {
                cur_base *= 10;;
                y /= 10;
        }
        cur_base /= 10;
        
        int counter = 0;   
        for (int j = a; j < b; ++j)
            counter += get_n(j, b);
         printf("%d %d\n", i, counter);    
        fprintf(o_fp, "Case #%d: %d\n", i, counter);
        //system("PAUSE");
    }
    fclose(o_fp);
    
    
    system("PAUSE");
    return 0;
}
