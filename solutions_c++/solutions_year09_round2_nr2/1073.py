#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
using namespace std;

int T, N;
char S[100];
vector<int> seq;


int main()
{

    FILE* fin = fopen("a.txt", "r");
    FILE* fout = fopen("a.out", "w");

    fscanf(fin, "%d", &T);
   
    for (int cnt = 1; cnt <= T; cnt++)
    {
        fscanf(fin, "%s\n", S); 
        //fprintf(fout, "%s::::", S);
        bool isF = false;
        for (int i = strlen(S)-1; i >= 0; i--)
        {
            for (int j = strlen(S)-1; j > i; j--)
            if (S[i] < S[j])
            {

                     fprintf(fout, "Case #%d: ", cnt);
                     for (int k = 0; k < i; k++)
                     fprintf(fout, "%c", S[k]);
                     
                     fprintf(fout, "%c", S[j]);
                     char c = S[i];
                     S[i] = S[j];
                     S[j] = c; 
                     
            for (int k1 = i+1; k1 < strlen(S); k1++)
                for (int k2 = k1+1; k2 < strlen(S); k2++)       
                if (S[k1] > S[k2])
                {
                     char c = S[k1];
                     S[k1] = S[k2];
                     S[k2] = c;
                }
                
                for (int k = i+1; k < strlen(S); k++)
                    fprintf(fout, "%c", S[k]);
                
                fprintf(fout, "\n");
                     isF = true;
                     break;
            }
            if (isF)
               break;
        }    
        if (isF)
        {
                //fprintf(fout, "Case #%d: %s\n", cnt, S); 
        }
        else
        {
            int len = strlen(S);
            S[len] = '0';
            S[len+1] = '\0';
            
            for (int k1 = 0; k1 < strlen(S); k1++)
                for (int k2 = k1+1; k2 < strlen(S); k2++)       
                if (S[k1] > S[k2])
                {
                     char c = S[k1];
                     S[k1] = S[k2];
                     S[k2] = c;
                }

                if (S[0] == '0')
                {
                  for (int k2 = 1; k2 < strlen(S); k2++)
                if (S[k2] != '0')
                {
                           char c = S[0];
                     S[0] = S[k2];
                     S[k2] = c;
                     break;
                     }
                     }        
                          
            fprintf(fout, "Case #%d: %s\n", cnt, S);
        }
    }
    return 0;
}

        

