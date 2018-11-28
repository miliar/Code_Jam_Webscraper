//
//  main.cpp
//  Google
//
//  Created by Manthan Systems on 25/03/12.
//  Copyright (c) 2012 Manthan Software Services. All rights reserved.
//

#include <iostream>
#include <fstream.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main (int argc, const char * argv[])
{

    int N,i=1,j,q;
	double long T;
	long int K;
    char c;
    std::ifstream f1("A-small.in");
f1>>N;

	ofstream f2("A-small-answer.in");
    std::string line;
//   std::ifstream in("A-small-practice.in");
    getline(f1,line);

    for(i;i<=N;i++)
	{
    getline(f1,line);
        char d[line.size()];
        printf("\n");
        f2<<"Case #"<<i<<": ";

        for (int k=0; k<line.size(); k++) {
                    d[k]=line[k];
//        while (f1>>c  && f1.peek()!='\n' ) {
        printf("%c",d[k]);
            switch (d[k]) {
                case 'a':
                case 'A':
                    d[k]='y';
//                    //index++;
                    break;
                case 'b':
                case 'B':
                    d[k]='h';
                    //index++;
                    break;
                case 'c':
                case 'C':
                    d[k]='e';
                    //index++;
                    break;
                case 'd':
                case 'D':
                    d[k]='s';
                    //index++;
                    break;
                case 'e':
                case 'E':
                    d[k]='o';
                    //index++;
                    break;
                case 'f':
                case 'F':
                    d[k]='c';
                    //index++;
                    break;
                case 'g':
                case 'G':
                    d[k]='v';
                    //index++;
                    break;
                case 'h':
                case 'H':
                    d[k]='x';
                    //index++;
                    break;  
                case 'i':
                case 'I':
                    d[k]='d';
                    //index++;
                    break;
                case 'j':
                case 'J':
                    d[k]='u';
                    //index++;
                    break;
                case 'k':
                case 'K':
                    d[k]='i';
                    //index++;
                    break;
                case 'l':
                case 'L':
                    d[k]='g';
                    //index++;
                    break;
                case 'm':
                case 'M':
                    d[k]='l';
                    //index++;
                    break;
                case 'n':
                case 'N':
                    d[k]='b';
                    //index++;
                    break;
                case 'o':
                case 'O':
                    d[k]='k';
                    //index++;
                    break;
                case 'p':
                case 'P':
                    d[k]='r';
                    //index++;
                    break;  
                case 'q':
                case 'Q':
                    d[k]='z';
                    //index++;
                    break;
                case 'r':
                case 'R':
                    d[k]='t';
                    //index++;
                    break;
                case 's':
                case 'S':
                    d[k]='n';
                    //index++;
                    break;
                case 't':
                case 'T':
                    d[k]='w';
                    //index++;
                    break;
                case 'u':
                case 'U':
                    d[k]='j';
                    //index++;
                    break;
                case 'v':
                case 'V':
                    d[k]='p';
                    //index++;
                    break;
                case 'w':
                case 'W':
                    d[k]='f';
                    //index++;
                    break;
                case 'x':
                case 'X':
                    d[k]='m';
                    //index++;
                    break;  
                case 'y':
                case 'Y':
                    d[k]='a';
                    //index++;
                    break;
                case 'z':
                case 'Z':
                    d[k]='q';
                    //index++;
                    break;
//                case  32:
//                    d[k]=32;
//                    index ++;
                default:
                    d[k]=d[k];
                    //index++;
                    break;
            }
            f2<<d[k];

}
        f2<<"\n";

   
        
              
    
   }
    f1.close();
    f2.close();
    return 0;
}

