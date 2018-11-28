//
//  main.cpp
//  DancingWithTheGooglers
//
//  Created by Choi Peter on 12. 4. 14..
//

#include <stdio.h>

#define SCORE_ARRAY_SIZE 3
#define NOTZERO(a) (a != 0)

//sepurate the score
void SepurateScore(const int nScore, int *aScore)
{
    int i;
    int nRest;
    
    for (i=0; i<SCORE_ARRAY_SIZE; i++)
    {
        aScore[i] = nScore/SCORE_ARRAY_SIZE;
    }
    
    nRest = nScore % SCORE_ARRAY_SIZE;
    i=0;
    while (nRest != 0)
    {
        aScore[i]++;
        nRest--;
        (i == SCORE_ARRAY_SIZE-1) ? (i=0) : (i++);
    }
    //printf("array(%d,%d,%d)\n",aScore[0],aScore[1],aScore[2]);
}

//return true if it is possible and complet work
//possible case n n n ; n+1 n+1 n ;
bool MakeSurprisingScore(int *aScore)
{
        
        
    if(aScore[0] == aScore[1])
    {
        if(NOTZERO(aScore[1]) && aScore[0] == aScore[2]+1)//case2
        {
            aScore[0]++;
            aScore[1]--;
        }
        else if(NOTZERO(aScore[2]))//case1
        {
            aScore[0]++;
            aScore[2]--;
        }
        else
        {
            return false;
        }
        
    }
    else
    {
        return false;
    }
    return true;
}

int main(int argc, const char * argv[])
{
    ///for intputs
    int T; //times...
    int N; //Googlers num
    int S; //Surprising num
    int p; //At least num
    //int Scores[100];
    int Scores;
    FILE *inputF;
 
    ///For solving problem
    int i,j;
    
    ///for output
    int aTriple[SCORE_ARRAY_SIZE];
    int nOutput;
    FILE *outputF;
    
    
    inputF  = fopen("./B-large.in.txt", "r");
    //outputF = fopen("./B_result_small01.txt","w");
    outputF = fopen("./B_result_large01.txt","w");
    if(outputF==NULL || inputF==NULL)
    {
        printf("error!\n");
        return -1;
    }
    
    
    //scanf("%d\n",&T);
    fscanf(inputF, "%d\n",&T);
    
    for( i=0 ; i<T ; i++)
    {
        //init
        nOutput=0;
        
        //Get input
        //scanf("%d %d %d",&N,&S,&p);
        fscanf(inputF, "%d %d %d",&N,&S,&p);
        //printf("N=%d, S=%d, p=%d\n",N,S,p);
        
        for(j=0 ; j<N ; j++)
        {
            fscanf(inputF, "%d",&Scores);
            
            //Slove
            SepurateScore(Scores, aTriple);
            if(aTriple[0] >= p)
            {
                nOutput++;
            }
            else
            {
                if (aTriple[0] == p-1)
                {
                    if(S > 0 &&  MakeSurprisingScore(aTriple))
                    {
                        S--;
                        nOutput++;
                        //printf("===>array(%d,%d,%d)\n",aTriple[0],aTriple[1],aTriple[2]);
                    }
                }
            }
         }
        
        
        //output
        //printf("Case #%d: %d\n",i+1,nOutput);
        fprintf(outputF, "Case #%d: %d\n",i+1,nOutput);
    }
   // getchar();
    
    fclose(outputF);
    fclose(inputF);
    
    return 0;
}

