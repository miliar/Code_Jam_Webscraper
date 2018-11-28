//
//  main.cpp
//  Qual2012-C
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


// count how many times we can rotate "number" where the resultant 
// 1) has the same number of digits without leading zeroes 
// 2) > "number"
// 3) <= B
// 4) has not already been seen

#define MAX_DIGITS  10      // we can't have more than this number of digits in the number

int recycleCountInt(int number, int B)
{
    int minVal;         // lowest value any of the results may have, i.e. 10^n-1, where n is the number of digits 
    int nDigits = 0;    // how many digits we have
    for(minVal=1;minVal<10000000;minVal *= 10)
        {
        if (number < minVal)
            break;
        nDigits++;
        }
    minVal /= 10;
    int count = 0;
    int newNum = number;
    int rotations = nDigits-1;
    int recycled[MAX_DIGITS];
    
    
    for(int rotation=1;rotation<=rotations;rotation++)
        {
        int firstDigit = (newNum / minVal);             // first digit
        newNum = ((newNum - (firstDigit*minVal)) * 10) + firstDigit;    // subtract out the first digit, multiply by 10 and add back first decimal digit at the end
        
        if (newNum > number && newNum <= B && newNum > minVal)  // bigger than original number, <= B and doesn't have leading zeroes (> minVal)
            {
            // check to see if we've already seen it
            int recycleCount;
            for(recycleCount=0;recycleCount<count;recycleCount++)
                if (recycled[recycleCount] == newNum)   // already recycled?
                    break;
            
            if (recycleCount >= count)  // not been recycled?
                {
                recycled[count] = newNum;
                count++;
                }
            }
        }
    return (count);
    
}


void runTest(FILE *in, FILE *out)
{
    int nTestCases;
    fscanf(in, "%d", &nTestCases);
    for(int i=0;i<nTestCases;i++)
        {
        int A = scanInt(in);
        int B = scanInt(in);
        int count = 0;
        for(int i=A;i<=B;i++)
            {
            count += recycleCountInt(i, B);
            }
        
        
        fprintf(out, "Case #%d: %d\n", i+1, count);
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
 Problem
 
 Do you ever become frustrated with television because you keep seeing the same things, recycled over and over again? Well I personally don't care about television, but I do sometimes feel that way about numbers.
 
 Let's say a pair of distinct positive integers (n, m) is recycled if you can obtain m by moving some digits from the back of n to the front without changing their order. For example, (12345, 34512) is a recycled pair since you can obtain 34512 by moving 345 from the end of 12345 to the front. Note that n and m must have the same number of digits (excluding leading zeros) in order to be a recycled pair.
 
 Given integers A and B with the same number of digits, how many distinct recycled pairs (n, m) are there with A ≤ n < m ≤ B?
 
 Input
 
 The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line containing the integers A and B.
 
 Output
 
 For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is the number of recycled pairs (n, m) with A ≤ n < m ≤ B.
 
 Limits
 
 1 ≤ T ≤ 50.
 A and B have the same number of digits.
 
 Small dataset
 
 1 ≤ A ≤ B ≤ 1000.
 
 Large dataset
 
 1 ≤ A ≤ B ≤ 2000000.
 
 Sample
 
 
 Input 
 
 Output 
 
 4
 1 9
 10 40
 100 500
 1111 2222
 Case #1: 0
 Case #2: 3
 Case #3: 156
 Case #4: 287
 
 Are we sure about the output to Case #4?
 
 Yes, we're sure about the output to Case #4.
 */

