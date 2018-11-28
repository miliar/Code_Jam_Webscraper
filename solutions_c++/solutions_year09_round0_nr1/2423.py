#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

// L lowercase letters in every word
// D words in the language
//
// L D N
#define BUFSZ 10000


bool matchfunc(char *token, int index, std::string word)
{
    int trueindex=0;
    int i=0;
    char agua[100];
    strcpy(agua, word.c_str());

    while (i < index)
    {
        if (token[trueindex++] == '(')
        {
            while (token[trueindex++] != ')');
        }
        i++;
    }
    if (token[trueindex] == '(')
    {
        while (token[trueindex] != ')')
        {
            if (token[trueindex++] == agua[index])
            {
                return true;
            }
        };
    }
    else if (token[trueindex] == agua[index])
    {
        return true;
    }

    return false;
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int L, N;
    float D, i;
    int j, k, l;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }


    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    subtoken = strtok_r(token, " ", &sptr2);
    L = atoi(subtoken);
    subtoken = strtok_r(NULL, " ", &sptr2);
    D = atof(subtoken);
    subtoken = strtok_r(NULL, " ", &sptr2);
    N = atoi(subtoken);

    std::vector<std::string> words;

//    printf("L=%d, D=%f, N=%d\n", L, D, N);
    for (i=0; i<D; i++)
    {
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        words.push_back(token);
    }
//    printf("words: %d\n", words.size());

    for (j=0; j<N; j++)
    {
        std::vector<std::string> matches;
        matches.clear();

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

                        int m=0;
        for (k=0; k<L; k++)
        {
//    printf("loop, %d\n", k+1);
            if (k == 0)
            {
                for (l=0; l < words.size(); l++)
                {
                    if (matchfunc(token, k, words[l]))
                    {
                        matches.push_back(words[l]);
//                        printf("hello, %s\n", words[l].c_str());
                    }
                }
            }
            else
            {
                std::vector<std::string>::iterator cii;
                for (cii=matches.begin(); cii != matches.end();)
                {
                    if (!matchfunc(token, k, *cii))
                    {
//                        if (k == 4)
//                        {
//                            printf("erased %d %s\n", m++, (*cii).c_str());
//                        }
                        matches.erase(cii);
                    }
                    else
                    {
//                        if (k == 4)
//                        {
//                            printf("kept %d %s\n", m++, (*cii).c_str());
//                        }
                        cii++;
                    }
                }
            }
//            printf("hello, %d\n", matches.size());
        }

        printf("Case #%d: %d\n", j+1, matches.size());
    }


    fclose(fp);
    return 0;
}
