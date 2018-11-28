//
//  main.cpp
//  Qual2012-B
//
//  Created by Zaid Jonathan on 4/14/12.
//


#include <stdio.h>
#include <math.h>
#include <iostream>

// few generic routines to make things easier
void openFiles(const char *testName, FILE **in, FILE **out);
int scanInt(FILE  *file);
void scanStr(FILE  *file, char *str, int strlen);
void scanVal(FILE  *file, char *str, int strlen, bool numeric);



void runTest(FILE *in, FILE *out)
{
    int nTestCases;
    fscanf(in, "%d", &nTestCases);
    for(int i=0;i<nTestCases;i++)
        {
        int N = scanInt(in);    // number of googlers  0 > 
        int S = scanInt(in);    // number of surprising scores 0 >= S <= N
        int p = scanInt(in);    // min best result
        int maxGooglers = 0;

        for(int googler=0;googler<N;googler++)
            {
            int t = scanInt(in);
            int avgVal = t/3;
            int minVal, maxVal;
            if (avgVal+1 < p) // can't get to p?
                if (!S || ((avgVal+2) < p)) // No surprises left or can't get to p with surprise?
                    continue;          // not this one! go on to the next googler
            
            char wasHigher = 0; // found a valid sum which is >= p for this googler
            
            // first let's try without the surprise, brute force, but not too brute.
            minVal = avgVal - 1;    
            if (minVal < 0) minVal = 0;
            maxVal = avgVal + 1;
            if (maxVal > 10) maxVal = 10;
            
            // try all combinations of a,b,c 
            for(int a=minVal;!wasHigher && a <= maxVal;a++)
                {
                for(int b=minVal;!wasHigher && b <= maxVal;b++)
                    {
                    for(int c=minVal;!wasHigher && c <=maxVal;c++)
                        {
                        if (a+b+c == t) // makes the total
                            {
                            if (abs(a-b) <= 1 && abs(a-c) <= 1 && abs(b-c) <= 1)    // all are within distance of 1?
                                {
                                if (a >= p || b >= p || c >= p) // any one of them is >= p?
                                    {
                                    maxGooglers++;
                                    wasHigher = 1;
                                    } // had a higher score
                                } // difference was ok
                            } // total was t
                        } // for all c
                    } // for all b
                } // for all a
            
            
            if (!wasHigher && S > 0) // didn't find one but we can try with a surprise?
                {
                minVal = avgVal - 2;
                if (minVal < 0) minVal = 0;
                maxVal = avgVal + 2;
                if (maxVal > 10) maxVal = 10;

                // go through all combinations again
                for(int a=minVal;!wasHigher && a <= maxVal;a++)
                    {
                    for(int b=minVal;!wasHigher && b <= maxVal;b++)
                        {
                        for(int c=minVal;!wasHigher && c <=maxVal;c++)
                            {
                            if (a+b+c == t) // total ok
                                {
                                if (abs(a-b) <= 2 && abs(a-c) <= 2 && abs(b-c) <= 2)    // difference ok
                                    {
                                    if (a >= p || b >= p || c >= p)
                                        {
//                                        fprintf(stderr, "*t=%d %d %d %d\n",t,a,b,c);
                                        maxGooglers++;
                                        wasHigher = true;
                                        S--;
                                        } // had a higher score
                                    } // difference was ok
                                } // total was t
                            } // for all c
                        } // for all b
                    } // for all a
                
                
                } // wasn't higher
                
                
            
            } // for all googlers
        
#if 0        
        fprintf(stderr,"N=%d S=%d p=%d", N, S, p);
        for(int i=0;i<N;i++)
            fprintf(stderr, " %d", t[i]);
        fprintf(stderr, "\n");
#endif        
        
        
        fprintf(out, "Case #%d: %d\n", i+1, maxGooglers);
        } // for all the testcases
    
}



#define TESTFILE_NAME   "test"
#define SMALLFILE_NAME  "small"
#define LARGEFILE_NAME  "large"

#define TESTSUITE       LARGEFILE_NAME

int main(int argc, const char * argv[])
{
    if (argc > 1)   // can specify a directory so we will read from file with testname specified in TESTSUITE
        {
        FILE *in, *out;
        const char *dir = "./";
        char testName[1024];
        if (strncmp(argv[1], "-d", 2) == 0)
            dir = &argv[1][2];
        snprintf(testName, sizeof(testName), "%s/%s",dir,TESTSUITE);
        openFiles(testName, &in, &out);
        runTest(in, out);
        fclose(in);
        fclose(out);
        }
    else
        {
        runTest(stdin, stdout);  // run from stdin/stdout
        }
    
    
    return 0;
}

// read a token from the current place in the file into str. 
// first scan out any non-alphanumeric characters (blanks, tabs, etc.)
// then scan while we have either alphanumeric (numeric=false) or numeric (numeric=true) fields
void scanVal(FILE  *file, char *str, int strlen, bool numeric)
{
    char c;
    char *p = str;
    while (1)
        {
        c = getc(file);
        if (feof(file))
            break;
        if (isalnum(c))
            break;
        }
    while (1)
        {
        if ((isalnum(c) && !numeric) || isnumber(c))
            {
            *p++ = c;
            c = getc(file);
            if (feof(file))
                break;
            if (p > &str[strlen-2])
                break;
            }
        else
            break;
        }
    *p = '\0';
    
}

// just return the next string in the input
void scanStr(FILE  *file, char *str, int strlen)
{
    scanVal(file, str, strlen, false);
}

// the next string is numeric, scan it and return it's int value
int scanInt(FILE  *file)
{
    int ret = 0;
    char str[1024];
    scanVal(file, str, sizeof(str), true);
    ret = atoi(str);
    return ret;
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
    0 <= a,b,c <= 10
 
    t[i] = a + b + c            // The total points for a Googler is the sum of the three scores in that Googler's triplet of scores
    |a - b| <= 2                // No triplet of scores contains scores that are more than 2 apart
    |a - c| <= 2 
    |b - c| <= 2
   
    for S
    |a - b| = 2                // so it's surprising if a triplet of scores contains two scores that are 2 apart
    |a - c| = 2 
    |b - c| = 2
 
    for N-S
    |a - b| <= 1                
    |a - c| <= 1 
    |b - c| <= 1
    
    max(a,b,c) >= p
 
    can't go more than 2 off the average
 
 */

/*
 Problem
 
 You're watching a show where Googlers (employees of Google) dance, and then each dancer is given a triplet of scores by three judges. Each triplet of scores consists of three integer scores from 0 to 10 inclusive. The judges have very similar standards, so it's surprising if a triplet of scores contains two scores that are 2 apart. No triplet of scores contains scores that are more than 2 apart.
 
 For example: (8, 8, 8) and (7, 8, 7) are not surprising. (6, 7, 8) and (6, 8, 8) are surprising. (7, 6, 9) will never happen.
 
 The total points for a Googler is the sum of the three scores in that Googler's triplet of scores. The best result for a Googler is the maximum of the three scores in that Googler's triplet of scores. Given the total points for each Googler, as well as the number of surprising triplets of scores, what is the maximum number of Googlers that could have had a best result of at least p?
 
 For example, suppose there were 6 Googlers, and they had the following total points: 29, 20, 8, 18, 18, 21. You remember that there were 2 surprising triplets of scores, and you want to know how many Googlers could have gotten a best result of 8 or better.
 
 With those total points, and knowing that two of the triplets were surprising, the triplets of scores could have been:
 
 10 9 10
 6 6 8 (*)
 2 3 3
 6 6 6
 6 6 6
 6 7 8 (*)
 The cases marked with a (*) are the surprising cases. This gives us 3 Googlers who got at least one score of 8 or better. There's no series of triplets of scores that would give us a higher number than 3, so the answer is 3.
 Input
 
 The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line containing integers separated by single spaces. The first integer will be N, the number of Googlers, and the second integer will be S, the number of surprising triplets of scores. The third integer will be p, as described above. Next will be N integers ti: the total points of the Googlers.
 
 Output
 
 For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the maximum number of Googlers who could have had a best result of greater than or equal to p.
 
 Limits
 
 1 ≤ T ≤ 100.
 0 ≤ S ≤ N.
 0 ≤ p ≤ 10.
 0 ≤ ti ≤ 30.
 At least S of the ti values will be between 2 and 28, inclusive.
 Small dataset
 
 1 ≤ N ≤ 3.
 Large dataset
 
 1 ≤ N ≤ 100.
 Sample
 
 
 Input 
 
 Output 
 
 4
 3 1 5 15 13 11
 3 0 8 23 22 21
 2 1 1 8 0
 6 2 8 29 20 8 18 18 21
 Case #1: 3
 Case #2: 2
 Case #3: 1
 Case #4: 3
 

 */

