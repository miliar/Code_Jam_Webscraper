#include <iostream.h>
#include <vector>

using std::vector;

bool containsBoth(vector<char> &result, char e1, char e2)
{
     vector<char>::iterator iter = result.begin();
     int found = 0;
     while(iter != result.end())
     {
         if((*iter == e1 && found == 2) || (*iter == e2 && found == 1))
         {
             return true;
         }
         else if(*iter == e2 && found != 1)
         {
             found = 2;
         }
         else if(*iter == e1 && found != 2)
         {
             found = 1;
         }
         iter++;
     }
     return false;
}

int main()
{
    FILE * input;
    input = fopen("B-small-attempt0.in", "r");
    FILE * output;
    output = fopen("B-small-attempt0.out", "w");
    
    int T;    // num cases
    int C;    // num of combining pairs
    int D;    // num of opposed pairs
    int N;    // num of invokations
    int i, j, k;  // iterators
    vector<char> result;      // resulting list
    
    // get number of cases
    fscanf(input, "%d\n", &T);
    
    for(i = 1; i <= T; i++)
    {
        result.clear();
        // solve for each case
        fscanf(input, "%d ", &C);    // get num of combining pairs
        char combined [C][3];
        
        // fill combining pairs vector
        for(j = 0; j < C; j++)
        {
            for(k = 0; k < 3; k++)
            {
                fscanf(input, "%c", &combined[j][k]);
            }
        }
        
        fscanf(input, " %d ", &D);  // get num of opposing pairs
        char opposed [D][2];
        
        // fill opposing pairs vector
        for(j = 0; j < D; j++)
        {
            for(k = 0; k < 2; k++)
            {
                fscanf(input, "%c", &opposed[j][k]);
            }
        }
        
        fscanf(input, " %d ", &N);  // get num of invokations
        char a;
        for(j = 0; j < N; j++)
        {
            fscanf(input, "%c", &a);
            result.push_back(a);
            int vsize = result.size();
            if(vsize > 1)
            {
                int comb = 0;
                // transform combining pairs, only if we have made 2 or more invokations
                for(k = 0; k < C; k++)
                {
                      if((result[vsize-1] == combined[k][0] && result[vsize-2] == combined[k][1]) ||
                      (result[vsize-1] == combined[k][1] && result[vsize-2] == combined[k][0]))
                      {
                         result.pop_back();
                         result.pop_back();
                         result.push_back(combined[k][2]);
                         comb = 1;
                         break;
                      }
                }
                // clear elements list only if size is 2 or more and we have not made a combination
                if(comb == 0)
                {
                    for(k = 0; k < D; k++)
                    {
                        if(containsBoth(result, opposed[k][0], opposed[k][1]))
                        {
                            result.clear();
                            break;
                        }
                    }
                }
            }
        }
        
        // print resulting vector
        fprintf(output, "Case #%d: [", i);
        vector<char>::iterator iter = result.begin();
        if(iter != result.end())
        {
            fprintf(output, "%c", *iter);
            iter++;
        }
        while(iter != result.end())
        {
            fprintf(output, ", %c", *iter);
            iter++;
        }
        fprintf(output, "]\n");     
    }
    fclose(input);
    fclose(output);
    return 0;
}
