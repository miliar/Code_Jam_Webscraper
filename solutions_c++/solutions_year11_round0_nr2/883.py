#include <stdio.h>
#include <assert.h>
#include <string.h>

struct combineMap
{
    // e1 can be equal to e2 here
    char e1;
    char e2;
    char res;
};

struct opposeMap
{
    // note e1 != e2
    char e1;
    char e2;
};


int T;              // no of test cases

int C;              // no of combine rules
combineMap comb[99];// the combine map

int D;              // no of destroy/oppose rules
opposeMap  dest[99];// the destroy/oppose map


int N;              // no of elements in the input invoker list
char inp[2000];     // the input list

int nOut;           // no of elements in the output list
char list[2000];    // the output list

char getCombinedChar(char a, char b)
{
    for(int i=0; i<C; i++)
    {
        if(comb[i].e1 == a && comb[i].e2 == b)
            return comb[i].res;

        if(comb[i].e1 == b && comb[i].e2 == a)
            return comb[i].res;
    }
    return 0;
}

bool findIfDest(char b)
{
    for(int j=0;j<nOut;j++)
    {
        char a = list[j];
        
        for(int i=0; i<D; i++)
        {
            if(dest[i].e1 == a && dest[i].e2 == b)
                return true;

            if(dest[i].e1 == b && dest[i].e2 == a)
                return true;            
        }
    }
    return false;
}

void processList()
{
    assert(strlen(inp) == N);
    nOut = 0;
    for(int i=0; i<N;i++)
    {
        if(nOut == 0)   // first item in list
        {
            list[nOut++] = inp[i];
        }
        else
        {
            char lastChar = list[nOut-1];
            char curChar = inp[i];
            // try combining
            char combinedChar = getCombinedChar(lastChar, curChar);
            if(combinedChar)
            {
                list[nOut-1] = combinedChar;
            }
            else
            {
                list[nOut++] = curChar;
            }
            // TODO: do we need to check for destruction/opposition for the combined char?
            if(!combinedChar)
            {
                bool isDest = findIfDest(curChar);
                if(isDest)
                {
                    // re-init the list
                    nOut = 0;
                }
            }
        }
    }
}

void scanCombineList(FILE *fp)
{
    char buf[100];
    for(int i=0;i<C;i++)
    {
        fscanf(fp, "%s", buf);
        comb[i].e1 = buf[0];
        comb[i].e2 = buf[1];
        comb[i].res = buf[2];
    }
}

void scanOpposeList(FILE *fp)
{
    char buf[100];
    for(int i=0;i<D;i++)
    {
        fscanf(fp, "%s", buf);
        dest[i].e1 = buf[0];
        dest[i].e2 = buf[1];
        assert(buf[0] != buf[1]);
    }
}

void printFinalList(FILE *fp)
{
    fprintf(fp, "[");
    
    for(int i=0;i<nOut-1;i++)
        fprintf(fp, "%c, ", list[i]);

    if(nOut > 0)
        fprintf(fp, "%c", list[nOut-1]);
    
    fprintf(fp, "]");

}


int main()
{
    FILE *fp = fopen("c:\\inp.txt", "r+"); // get input data from file
    fscanf(fp, "%d", &T);

    FILE *fpo = fopen("c:\\op.txt", "w+"); // write op data to file

    for(int c=1;c<=T;c++)    // process each test case
    {
        fscanf(fp, "%d", &C);
        scanCombineList(fp);

        fscanf(fp, "%d", &D);
        scanOpposeList(fp);

        fscanf(fp, "%d", &N);
        fscanf(fp, "%s", inp);

        processList();
        fprintf(fpo, "Case #%d: ", c);
        printFinalList(fpo);
        fprintf(fpo, "\n");
    }

    fclose(fp);
    fclose(fpo);
    return 0;
}

