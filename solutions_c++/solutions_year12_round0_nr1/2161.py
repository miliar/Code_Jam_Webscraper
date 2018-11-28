// =========================================================
//
//       Filename:  Speaking in Tongues.cpp
//
//    Description:
//
//        Version:  1.0
//        Created:  04/14/2012
//       Revision:  none
//       Compiler:  g++
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 04/14/2012
//
// =========================================================

#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

#define MAXLINE 200

char goo1[] = "y qee";
char goo2[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
char goo3[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char goo4[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

char str1[] = "a zoo";
char str2[] = "our language is impossible to understand";
char str3[] = "there are twenty six factorial possibilities";
char str4[] = "so it is okay if you want to just give up";

void train(char mapping[])
{
    char *p, *q;

    for (p = goo1, q = str1; *p; ++p, ++q)
        mapping[(int)*p] = *q;

    for (p = goo2, q = str2; *p; ++p, ++q)
        mapping[(int)*p] = *q;

    for (p = goo3, q = str3; *p; ++p, ++q)
        mapping[(int)*p] = *q;

    for (p = goo4, q = str4; *p; ++p, ++q)
        mapping[(int)*p] = *q;

    // 'z' is left
    mapping[(int)'z'] = 'q';
}

void translate(char mapping[], char goo[], char str[])
{
    char *p, *q;
    for (p=goo, q=str; *p; ++p, ++q)
        *q = mapping[(int)*p];
    *q = 0;
}

int main()
{
    char mapping[256];

    train(mapping);

    //for (char i='a'; i<='z'; i++)
    //    cout << i << "\t" << mapping[i] << endl;
    //cout << translate(mapping, goo4) << endl;

    unsigned int case_no;
    char goo[MAXLINE];
    char str[MAXLINE];

    // load input
    cin >> case_no;
    cin.getline(goo, MAXLINE);

    for (unsigned int i = 0; i < case_no; i++)
    {
        // init parameters
        cin.getline(goo, MAXLINE);
        //cout << goo << endl;
        // sove problem
        cout << "Case #" << i+1 << ": ";
        translate(mapping, goo, str);
        cout << str << endl;
    }

    return 0;

}
