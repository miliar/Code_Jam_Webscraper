#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define MAX_LEN 1024
int n, m;

char E[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char G[27] ={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};

char A[26][2] = { {'a','y'},
{'b','n'},
{'c','f'},
{'d','i'},
{'e','c'}
};


int Q2012();
int Q2012_ETOG();
int Q2012_GTOE();
int main( )
{
    
    Q2012_GTOE();
    return 0;
}

int Q2012()
{
    FILE *fp;
    int i, t, tt;
    size_t j;
    int bFound = 0;
    char line[MAX_LEN];
    char output[MAX_LEN];
    fp = fopen("input_2012.txt","r");
    fgets(line,MAX_LEN,fp);

    tt = atoi(line);
    for( t = 1; t <= tt; ++ t )
    {
        fgets(line,MAX_LEN,fp);

        for( j = 0; j < strlen(line); j++)
        {
            bFound = 0;
            for( i = 0; i<27; i++)
            {
                if(G[i] == line[j])
                {
                    output[j] = E[i];
                    printf("%c", E[i]);
                    bFound = 1;
                }
            }
            if(!bFound)
            {
                output[j] = line[j];
                printf("%c", line[j]);
            }
        }
        output[j]='\0';
        printf("Case#%d : %s\n", t, output);
    }
    
    return 0;
}



int Q2012_GTOE()
{
    FILE *fp, *fpo;
    int i, t=1, tt;
    size_t j = 0;
    int bFound = 0;
    char c;
    int line = 0;
    char output[MAX_LEN];
    fp = fopen("input.txt","r");
    fpo = fopen("output.txt","w");

    if (fp == NULL) perror ("Error opening file");
    else
    {
        fscanf(fp, "%d", &tt);
        do {
            bFound = 0;
            c = fgetc (fp);
            if(line==0)
            {
                line++;
                continue;
            }
            if (c == '\n' )
            {
               output[j]=0;
               fprintf(fpo, "Case #%d: %s\n", t++, output);
               j=0;
               if(t > tt)
                   break;
               continue;
            }

            for( i = 0; i<26; i++)
            {
                if(G[i] == c)
                {
                    output[j++] = E[i];
                    //printf("%c", E[i]);
                    bFound = 1;
                }
            }
            if(!bFound)
            {
                output[j++] = c;
                //printf("%c", c);
            }
        } while (c != EOF);
        fclose (fp);
        fclose (fpo);
    }
    
    return 0;
}

int Q2012_ETOG()
{
    FILE *fp, *fpo;
    int i, t=1, tt;
    size_t j = 0;
    int bFound = 0;
    char c;
    int line = 0;
    char output[MAX_LEN];
    fp = fopen("input_2012.txt","r");
    fpo = fopen("output_2012.txt","w");

    if (fp == NULL) perror ("Error opening file");
    else
    {
        fscanf(fp, "%d", &tt);
        do {
            bFound = 0;
            c = fgetc (fp);
            if(line==0)
            {
                line++;
                continue;
            }
            if (c == '\n' )
            {
               output[j]=0;
               fprintf(fpo, "Case #%d: %s\n", t++, output);
               j=0;
               if(t > tt)
                   break;
               continue;
            }

            for( i = 0; i<26; i++)
            {
                if(E[i] == c)
                {
                    output[j++] = G[i];
                    //printf("%c", E[i]);
                    bFound = 1;
                }
            }
            if(!bFound)
            {
                output[j++] = c;
                //printf("%c", c);
            }
        } while (c != EOF);
        fclose (fp);
        fclose (fpo);
    }
    
    return 0;
}