#include <stdio.h>
#include <string.h>

int main(int argc, char * argv[])
{
    int tests; //Number of lines
    int i, j; //iterators
    int tmp;
    FILE *f_in, *f_out;

    int googlers, surprising, minscore;
    int basescore, mod;
    int count;
    char scores[100];

    f_in = fopen("in.txt", "r");
    f_out = fopen("out.txt", "w");

    fscanf(f_in, "%d", &tests);
    fgetc(f_in); //Remove newline

    for(i = 0, count = 0; i < tests; ++i, count = 0)
    {
        //Read all the necessary data
        fscanf(f_in, "%d", &googlers); //How many dancers
        fscanf(f_in, "%d", &surprising); //Home many scores were interesting
        fscanf(f_in, "%d", &minscore); //The score we are interested in
        
        memset(scores, -1, 100);
        for(j = 0; j < googlers; ++j)
        {
            fscanf(f_in, "%d", &tmp); //fscanf expects an int, not a char
            scores[j] = tmp; //
        }
        
        fgetc(f_in); //Newline

        //Check to see how many of the scores could have a best
        //score of minscore or greater
        for(j = 0; j < googlers; ++j)
        {
            basescore = scores[j] / 3;
            mod = scores[j] - (basescore * 3); //Safe modulo

            //Obviously possible
            if(basescore >= minscore)
                ++count;

            //Add 1 to a value or two
            else if(mod > 0 && basescore+1 >= minscore)
                ++count;

            //Add two if a surprising result is still possible
            else if(mod == 2 && surprising > 0 && basescore+2 >= minscore)
            {
                ++count;
                --surprising;
            }

            //Add from 1, subtract from another.
            else if(mod == 0 && basescore != 0 && surprising > 0 && basescore+1 >= minscore)
            {
                ++count;
                --surprising;
            }
        }

        //Print results to file
        fprintf(f_out, "Case #%d: %d\n", i+1, count);
    }

    return 0;
}
