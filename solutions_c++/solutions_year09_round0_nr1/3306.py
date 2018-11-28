#include "gcjAlienLang.h"
#include "gcjFileHandler.h"


gcjAlienLang::gcjAlienLang()
{
    nbrOfAlienChars = 0;
    nbrOfAlienWords = 0;
    pDict = NULL;
}


void gcjAlienLang::Init(int chars, int words)
{
    nbrOfAlienChars = chars;
    nbrOfAlienWords = words;
    //pDict = new char[nbrOfAlienWords][nbrOfAlienChars + 1];
    pDict = new char*[nbrOfAlienWords];
    for (int i = 0; i < nbrOfAlienWords; i++)
    {
        pDict[i] = new char[nbrOfAlienChars + 1];
    }
    cout << nbrOfAlienChars << " " << nbrOfAlienWords << endl;
    return;
}


void gcjAlienLang::fillDict(gcjFileHandler &fileHandle)
{
    for (int i = 0; i < nbrOfAlienWords; i++)
    {
        fileHandle.getStr(pDict[i], nbrOfAlienChars + 1);
        cout << pDict[i] << endl;
    }
    return;
}


int gcjAlienLang::invokeAlgo(char *inputStr)
{
    int len = strlen(inputStr);
    
    if (len == nbrOfAlienChars)
    {
        return (quickMatch(inputStr));
    }

    char *p = inputStr;

    int i = 0;
    int numChar[nbrOfAlienChars];
    char **cont;
    cont = new char*[nbrOfAlienChars];
    while (i < nbrOfAlienChars)
    {
        if (*p != '(')
        {
            cont[i] = new char[1];
            cont[i][0] = *p;
            numChar[i] = 1;
            p++;
            i++;
        }
        else
        {
            char *pend = NULL;
            pend = strchr(p, ')');
            numChar[i] = (pend - p) - 1;
            cont[i] = new char[numChar[i]];
            p++;
            memcpy(cont[i], p, numChar[i]);
            p = pend;
            p++;
            i++;
        }
    }

    int nbrOfMatchWords = 0;
    for (int j = 0; j < nbrOfAlienWords; j++)
    {
        char *pch = pDict[j];
        int nbrOfMatches = 0;
        for (int k = 0; k < nbrOfAlienChars; k++)
        {
            bool match = false;
            for (int l = 0; l < numChar[k]; l++)
            {
                if (*pch == cont[k][l])
                {
                    match = true;
                    break;
                }
            }

            if (match)
            {
                pch++;
                nbrOfMatches++;
                match = false;
            }
            else
            {
                break;
            }
        }

        if (nbrOfMatches == nbrOfAlienChars)
        {
            nbrOfMatchWords++;
        }
    }

    
    return nbrOfMatchWords;
}


int gcjAlienLang::quickMatch(char *inStr)
{
    int matched = 0;
    for (int i = 0; i < nbrOfAlienWords; i ++)
    {
        if (!strcmp(pDict[i], inStr))
        {
            matched++;
        }
    }

    return matched;
}


gcjAlienLang::~gcjAlienLang()
{
    nbrOfAlienChars = 0;
    nbrOfAlienWords = 0;
    pDict = NULL;
}
