#include <iostream>
#include <fstream>
#include <cstring>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
using namespace std;

#include <stdio.h>
#include <stdlib.h>

int strsz = 0;
int testsz = 0;

int findpattern(char *str, char *test)
{
    int j = 0;
    int count = 0;
    bool bMatch = false;
    int sztest = strlen(test);
    int szstr = strlen(str);
    if (szstr > sztest)
        return 0;
    
    if (szstr == 1)
    {
        while(j < sztest)
        {
            if (test[j++] == str[0])
            count = (count + 1)%10000;
        }
        return count;
     }

    char c1 = str[0];
    char c2 = test[0];
    //char *thistest = test+testpos;
    while(j <= strlen(test))
    {
        c2 = test[j];
        if (c1 == c2)
        {
            bMatch = true;
            count = (count + findpattern(&(str[1]), &(test[j+1])))%10000;
        }
        j++;
    }
    return count;
}

int main()
{

    // FILE *inF = fopen("i:\\timepasscoding\\watershed_09\\B-small-attempt0.txt", "r");
    FILE *inF = fopen("i:\\timepasscoding\\wcg\\C-small-attempt0.in", "r");
    FILE *outF = fopen("i:\\timepasscoding\\wcg\\out_small.txt", "w");
//    ofstream outF;
    string test;
    int cases = 0;
    int instances = 0;
    unsigned int count=0;
    
    //outF.open("i:\\timepasscoding\\wcg\\out.txt");
    fscanf(inF, "%d", &cases);
    char c = fgetc(inF);
    
    char *str = "welcome to code jam";
    strsz = strlen(str);
    
    for (int iCase = 0; iCase < cases; iCase++)
    {
        
        while (!feof(inF))
        {
        c = fgetc(inF);
            if (c == '\n' || c == -1)
            {
                char *cstr2;
                testsz = test.size();
                cstr2 = new char [testsz + 1];
                strcpy (cstr2, test.c_str());
                
                instances = findpattern(str, cstr2);
                printf("Case #%d: %04d\n",iCase+1,instances);
                if (iCase+1 <= cases)
                    fprintf(outF,"Case #%d: %04d\n",iCase+1,instances);fflush(outF);
                
                iCase++;
                free(cstr2);
                test.clear();
            }
            if ((c <= 'z' && c >= 'a')||(c == ' '))
            {
                test.push_back(c);
            }
        }
    }
    fclose(inF);
    fclose(outF);
    return 0;

}