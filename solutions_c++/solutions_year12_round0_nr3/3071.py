#include<stdio.h>
#include<iostream>
using namespace std;
#include<stdlib.h>
#include<string.h>

main()
{
    FILE * fi=fopen("input.txt","r");
    FILE * fo=fopen("output.txt","w");
    int T;
    fscanf(fi,"%d\n",&T);
    for(int line=0;line<T;line++)
    {
        int A,B,digit,out_count=0;
        char str[7];
        fscanf(fi,"%d %d\n",&A,&B);
        itoa ( A, str, 10 );
        digit=strlen(str);
        for(int i=B;i>=A;i--)
        {
            char stri[5],temp[5];
            itoa ( i, stri, 10 );
            int num;
            for(int j=0;j<digit-1;j++)
            {
                strcpy(temp,stri);
                for(int k=0;k<digit;k++)
                {
                    stri[k]=temp[(k+1)%digit];
                }
                num=atoi(stri);
                if(num<i && num >= A)
                {
                    out_count++;
                }
            }
        }
        fprintf(fo,"Case #%d: %d\n",(line+1),out_count);
    }
    fclose(fi);
    fclose(fo);
}

