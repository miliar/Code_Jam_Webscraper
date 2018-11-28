//
//  main.cpp
//  SpeakingInTongues
//
//  Created by Choi Peter on 12. 4. 14..
//


#include <stdio.h>
#include <string.h>

#define ALL_LETTER_SIZE ('z' - 'a' + 1)

#define G1 "ejp mysljylc kd kxveddknmc re jsicpdrysi"
#define G2 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
#define G3 "de kr kd eoya kw aej tysr re ujdr lkgc jv"

#define T1 "our language is impossible to understand"
#define T2 "there are twenty six factorial possibilities"
#define T3 "so it is okay if you want to just give up"
//q z 

char T[ALL_LETTER_SIZE+1];
char G[ALL_LETTER_SIZE+1];
bool bG[ALL_LETTER_SIZE];

char inputS[100+1], outputS[100+1];


void initTG()
{
    int i;
    char c;
    
    for(i=0, c='a' ; i<ALL_LETTER_SIZE ; i++)
    {
        G[i]  = c;
        bG[i] = false;
        c++;
        
        T[i]  = 'a' - 1;
    }
    
    T[ALL_LETTER_SIZE] = '\0';
    G[ALL_LETTER_SIZE] = '\0';
}

//T->G

void MappingByExample()
{
    int i, j;
    int nc; //num of ...
    
    
    nc = 'y' - 'a';
    T[nc]  = 'a';
    bG[nc] = true;
    
    nc = 'e' - 'a';
    T[nc] = 'o';
    bG[nc] = true;
    
    nc = 'q' - 'a';
    T[nc] = 'z';
    bG[nc] = true;
    
    for(i=0 ; i<3 ; i++)
    {
        if (i==0) 
        {
            sprintf(inputS, "%s", G1);
            sprintf(outputS, "%s", T1);
        }
        else if(i==1)
        {
            sprintf(inputS, "%s", G2);
            sprintf(outputS, "%s", T2);
        }
        else if(i==2)
        {
            sprintf(inputS, "%s", G3);
            sprintf(outputS, "%s", T3);            
        }
        
        j=0;
        while(inputS[j] != '\0')
        {
            if(inputS[j] == ' ')
            {
                j++;
                continue;
            }
            
            nc = inputS[j] - 'a';
            if(bG[nc] == false)
            {
                T[nc] = outputS[j];
                bG[nc] = true;
            }
            j++;
        }
    }
    
    //find q(in T)
    for (i=0; i<ALL_LETTER_SIZE; i++) 
    {
        if(bG[i] == false)
        {
            T[i] = 'q';
            bG[i] = true;
        }
    }
}

int main(int argc, const char * argv[])
{
    int n;
    int i, j;
    int nc;
    
    int dummy;
    
    FILE *inputF, *outputF;
    
    initTG(); //init T
    MappingByExample(); //init G

    inputF  = fopen("./A-small-attempt1.in.txt", "r");
    outputF = fopen("./result01.txt","w");
    if(outputF==NULL || inputF==NULL)
    {
        printf("error!\n");
        return -1;
    }

    //scanf("%d\n", &n);
    fscanf(inputF, "%d\n", &n);
    printf("%d\n",n);
    
    
    for(i=0 ;i<n ;i++)
    {
        
        
        //scanf("%[^\n]s", inputS);
        //fscanf(inputF, "%[^\n]s", inputS);
        
        inputS[0]='\0';
        fscanf(inputF, "%[^\n]s", inputS);
        
        while((dummy = fgetc(inputF)) != '\n' && dummy != EOF);
        
        
        j=0;
        while (inputS[j]!='\0')
        {
            if(inputS[j] >= 'a' && inputS[j]<='z')
            {
                nc = inputS[j] - 'a';
                outputS[j] = T[nc];
            }
            else
            {
                outputS[j] = inputS[j];
            }

            j++;
        }
        outputS[j] = '\0';
        
        printf("Case #%d: %s\n",i+1,outputS);
        fprintf(outputF, "Case #%d: %s\n",i+1,outputS);
    }
    fclose(outputF);
    fclose(inputF);
    return 0;
}