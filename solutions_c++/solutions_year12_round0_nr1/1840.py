//
//  main.cpp
//  Qual2012-A
//
//  Created by Zaid Jonathan on 4/14/12.
//


#include <stdio.h>
#include <math.h>
#include <iostream>

// few generic routines to make things easier
void openFiles(const char *testName, FILE **in, FILE **out);


#define MAX_LINE    100+2   

// create a map from the test case results
// set them up so that we have first line is number of test cases 
// then for each following line we have the encrypted line and then the decrypted line


const char *encryptedTest[] = 
    {
    "y qee",
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    NULL
    };

const char *decryptedTest[] = 
    {
    "a zoo",
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up",
    NULL
};


// fill up a translation map indexed by the encrypted letter with the value being the decrypted letter

void fillMap(char *map, int mapLen)
{
    
    char mapped[26];    // letters we have mapped
    for(int i=0;i<mapLen;i++)
        {
        map[i] = '\0';
        mapped[i] = 0;
        }
    if (mapLen < 26)
        fprintf(stderr, "map is too small, this is doomed to fail\n");
    
    for(int i=0;encryptedTest[i];i++)
        {
        const char *encryptedLine, *decryptedLine;
        encryptedLine = encryptedTest[i];
        decryptedLine = decryptedTest[i];
        if (strlen(encryptedLine) != strlen(decryptedLine))
            fprintf(stderr, "oops. lines are not the same length: (%d,%d)\n", (int) strlen(encryptedLine), (int) strlen(decryptedLine));
        const char *encrypted = encryptedLine, *decrypted = decryptedLine;
      
        while (*decrypted)
            {
            char c = *encrypted;
            if (c >= 'a' && c <= 'z')
                {
                int mapIndex = c - 'a';
                if (map[mapIndex] == '\0')
                    map[mapIndex] = *decrypted;
                else if (map[mapIndex] != *decrypted)
                    fprintf(stderr, "something wrong here, encrypted char %c wants to be %c but was %c\n",*encrypted, *decrypted, map[mapIndex]);
                if (*decrypted >= 'a' && *decrypted <= 'z') // mark it as mapped. We do this so we can resolve one last letter if needed :)
                    mapped[*decrypted-'a'] = 1;
                }
            encrypted++; 
            decrypted++;
            } // for decrypted string
        
        } // for all test lines
    
    char reverseMap[mapLen];
    for(int i=0;i<mapLen;i++)
        reverseMap[mapLen] = '\0';
    
    int countMissing = 0;   // how many letters we couldn't map
    int lastMissingIndex;   // index of the last missing letter in the map
    for(char c='a';c <= 'z';c++)
        {
        int mapIndex = c - 'a';
        if (map[mapIndex] == '\0')  // couldn't find a translation for this one?
            {
            countMissing++;
            lastMissingIndex = mapIndex;
            //fprintf(stderr, "Missing mapping for %c\n", c);
            }
        }
    if (countMissing == 1) // we can fix this 
        {
        // find the letter we haven't mapped yet
        for(char c='a';c <= 'z';c++)
            {
            if (!mapped[c-'a'])
                {
                map[lastMissingIndex] = c; // and here it is
                countMissing--;
                break; 
                }
            } // for all the mapped letters
        
        } // missing one letter
    
    if (countMissing > 0)
        fprintf(stderr, "still have missing letters, test will fail\n");
    

}

    // map used to translate
 
void runTest(FILE *in, FILE *out, char *map)
{
    int nTestCases;
    fscanf(in, "%d\n", &nTestCases);
    for(int nTest=0;nTest<nTestCases;nTest++)
        {
        char G[MAX_LINE];
        fprintf(out, "Case #%d: ",nTest+1);
        if (fgets(G, sizeof(G), in))
            {
            for(int i=0;i<MAX_LINE && G[i];i++)
                {
                char c = G[i];
                if (c >= 'a' && c <= 'z')
                    c = map[c-'a'];
                fprintf(out, "%c", c);
                }
            } // got the line
        } // for all the testcases
    
}



#define TESTFILE_NAME   "test"
#define SMALLFILE_NAME  "small"
#define LARGEFILE_NAME  "large"

#define TESTSUITE       SMALLFILE_NAME

int main(int argc, const char * argv[])
{
    char map[26];
    fillMap(map, sizeof(map));
    if (argc > 1)   // can specify a directory so we will read from file with testname specified in TESTSUITE
        {
        FILE *in, *out;
        const char *dir = "./";
        char testName[1024];
        if (strncmp(argv[1], "-d", 2) == 0)
            dir = &argv[1][2];
        snprintf(testName, sizeof(testName), "%s/%s",dir,TESTSUITE);
        openFiles(testName, &in, &out);
        runTest(in, out, map);
        fclose(in);
        fclose(out);
        fflush(stdout);
        }
    else
        {
        runTest(stdin, stdout, map);  // run from stdin/stdout
        }


    return 0;
}


// open input/output files. If name not specified, just use stdin/stdout
// otherwise the name should be without a suffix and the input file has ".in" appended and the output file ".out"
void openFiles(const char *testName, FILE **in, FILE **out)
{
    if (testName && *testName)
        {
        char outName[1024+4];
        char inName[1024+4];
        snprintf(inName, sizeof(inName), "%s.in", testName);
        snprintf(outName, sizeof(outName), "%s.out", testName);
        *in = fopen(inName, "r");
        *out = fopen(outName, "w");
        }
    else
        {
        *in = stdin;
        *out = stdout;
        }
    
}


/*
 
 Problem
 
 We have come up with the best possible language here at Google, called Googlerese. To translate text into Googlerese, we take any message and replace each English letter with another English letter. This mapping is one-to-one and onto, which means that the same input letter always gets replaced with the same output letter, and different input letters always get replaced with different output letters. A letter may be replaced by itself. Spaces are left as-is.
 
 For example (and here is a hint!), our awesome translation algorithm includes the following three mappings: 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'. This means that "a zoo" will become "y qee".
 
 Googlerese is based on the best possible replacement mapping, and we will never change it. It will always be the same. In every test case. We will not tell you the rest of our mapping because that would make the problem too easy, but there are a few examples below that may help.
 
 Given some text in Googlerese, can you translate it to back to normal text?
 
 Solving this problem
 
 Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has only 1 Small input. Once you have solved the Small input, you have finished solving this problem.
 
 Input
 
 The first line of the input gives the number of test cases, T. T test cases follow, one per line.
 
 Each line consists of a string G in Googlerese, made up of one or more words containing the letters 'a' - 'z'. There will be exactly one space (' ') character between consecutive words and no spaces at the beginning or at the end of any line.
 
 Output
 
 For each test case, output one line containing "Case #X: S" where X is the case number and S is the string that becomes G in Googlerese.
 
 Limits
 
 1 ≤ T ≤ 30.
 G contains at most 100 characters.
 None of the text is guaranteed to be valid English.
 Sample
 
 Input
 3
 ejp mysljylc kd kxveddknmc re jsicpdrysi
 rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
 de kr kd eoya kw aej tysr re ujdr lkgc jv
 
 
 Output
 Case #1: our language is impossible to understand
 Case #2: there are twenty six factorial possibilities
 Case #3: so it is okay if you want to just give up

 
 */

