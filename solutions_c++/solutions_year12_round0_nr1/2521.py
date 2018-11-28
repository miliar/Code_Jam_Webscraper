#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char results[3][101]={
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char inputs[3][101]={
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
};

char correlations[26];

int main(int argc, char **argv)
{
    int T;
    char string[101];
    int count, count2;
    // Gets the correlations
    memset(correlations, -1, sizeof(char)*26*2);
    for(count=0;count<3;count++)
        for(count2=0;count2<100 && results[count][count2] != 0;count2++)
        {
            if(inputs[count][count2]==' ')
                continue;
            if(correlations[results[count][count2]-'a'] == -1)
                correlations[results[count][count2]-'a'] = inputs[count][count2];
            else if(correlations[results[count][count2]-'a'] != inputs[count][count2])
            {
                printf("Panic at the disco!\n");
                exit(0);
            }
        }
    // Checks if we have all letters
/*    for(count=0;count<26;count++)
    {
        if(correlations[count] == -1)
            correlations[count] = count+'a';        
        //printf("Letter %c -> %c\n", count+'a', correlations[count]);    
    }*/
    correlations['q'-'a']='z';
    correlations['z'-'a']='q';
    count2=1;
    // Reads the number of cases
    scanf("%d", &count);
    //rewind(stdin);
    fflush(stdin);
    getc(stdin); 
    // For each case
    while(count2 <= count)
    {
        
        // Header
        printf("Case #%d: ", count2);
        char text[101];
        
        gets(text);
        for(int i=0;i<101 && text[i]!=0;i++)
        {
            if(text[i]!=' ')
                printf("%c", correlations[text[i]-'a']);
            else
                printf(" ");
        }
        printf("\n");
        count2++;
    }
}