#include <iostream>


bool check(char x,char y)
{
     if (x == y || x =='T')
     {
           return true;
     }
     return false;
}
int main()
{
    FILE* f_in = fopen("A-large.in","r");
    FILE* f_out = fopen("1out.txt","w");
    int n;
    fscanf(f_in,"%d\n",&n);
    for (int i = 0 ;i < n ;i++)
    {
        char a[10][10];
        if (i !=0)
        {
              fgets(a[0],10,f_in);
        }
        int s = 0;
        for (int j = 0 ; j < 4; j++)
        {
            fgets(a[j],10,f_in);
            for (int k = 0 ;k < 4 ;k++)
                if (a[j][k]  == '.')
                {
                             s++;
                }
        }
        bool flag1 = false;
        bool flag2 = false;
        for (int j = 0 ;j < 4 ;j++)
        {
            if (check(a[j][0],'X')&&check(a[j][1],'X')&&check(a[j][2],'X')&&check(a[j][3],'X'))
            {
                                                                                               flag1 = true;
            }
            if (check(a[j][0],'O')&&check(a[j][1],'O')&&check(a[j][2],'O')&&check(a[j][3],'O'))
            {
                                                                                               flag2 = true;
            }
            if (check(a[0][j],'X')&&check(a[1][j],'X')&&check(a[2][j],'X')&&check(a[3][j],'X'))
            {
                                                                                           flag1 = true;
            }
            if (check(a[0][j],'O')&&check(a[1][j],'O')&&check(a[2][j],'O')&&check(a[3][j],'O'))
            {
                                                                                           flag2 = true;
            }
        }
        if (check(a[0][0],'X')&&check(a[1][1],'X')&&check(a[2][2],'X')&&check(a[3][3],'X'))
        {
                                                                                           flag1=true;
        }
        if (check(a[0][0],'O')&&check(a[1][1],'O')&&check(a[2][2],'O')&&check(a[3][3],'O'))
        {
                                                                                           flag2=true;
        }
        if (check(a[0][3],'X')&&check(a[1][2],'X')&&check(a[2][1],'X')&&check(a[3][0],'X'))
        {
                                                  flag1=true;
        }
        if (check(a[0][3],'O')&&check(a[1][2],'O')&&check(a[2][1],'O')&&check(a[3][0],'O'))
        {
                                                  flag2=true;
        }

        if(flag1)
        {
             fprintf(f_out,"Case #%d: X won\n",i+1);
        }
        else if(flag2)
        {
             fprintf(f_out,"Case #%d: O won\n",i+1);
        }
        else if (s!=0)
        {
            fprintf(f_out,"Case #%d: Game has not completed\n",i+1);
        }
        else
        {
            fprintf(f_out,"Case #%d: Draw\n",i+1);
        }
        
    }
    fclose(f_out);
    return 0;
}
