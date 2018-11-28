#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

// TOshima

// abc, (ab)b(cd)
int patternMatch (string word, string pattern)
{
    // multiple interpretations of current letter?
    bool multi = false, contained = false;
    string wordLetter, patternLetter;
    int i, ptr = 0;


    // for each letter
    for (i=0; i<pattern.length(); i++)
    {
        patternLetter = pattern[i];
        if (patternLetter == "(")
        {
            multi = true;
        }
        else if (patternLetter == ")")
        {
            // check mult, contained needs to be true
            if (!contained)
            {
                return false;
            }
            ptr++;
            multi = false;
            contained = false;
        }
        else
        {
            wordLetter = word[ptr];

            // mult interpretations
            if (multi)
            {
                if (patternLetter == wordLetter)
                {
                    contained = true;
                }
            }
            else
            {
                // single interpretation, so needs to match
                if (patternLetter != wordLetter)
                {
                    return false;
                }
                ptr++;
            }
        }
        //printf ("%d", a);
        //printf ("%s\n", input.c_str());

    }
    return true;
}


int main()
{
    int L, D, N, i, j, k, count, caseId;
    char chInput [16];
    char chInputLong [1024*1024];
    string input, letter;
    string words [10000];

    // input output streams
    freopen ("A-large.in", "r", stdin);
    freopen ("output.txt", "w", stdout);

    // number of cases
    scanf ("%d%d%d", &L, &D, &N);
    if (N < 1)
        printf ("Error: input file not found\n");

    // for each dictionary word
    for (i=0; i<D; i++)
    {
        scanf ("%s", chInput);
        input = chInput;
        words[i] = input;
        //printf ("%s\n", input.c_str());
    }

    // for each message
    for (caseId=1; caseId<=N; caseId++)
    {
        count = 0;

        scanf ("%s", chInputLong);
        input = chInputLong;

        // for each word
        for (j=0; j<D; j++)
        {
            if (patternMatch (words[j], input))
            {
                count++;
            }
        }

        printf ("Case #%d: %d\n", caseId, count);
    }

    //bool a = patternMatch ("abe", "(ab)b(cd)");
    //printf("%d", a);
    return 0;
}

