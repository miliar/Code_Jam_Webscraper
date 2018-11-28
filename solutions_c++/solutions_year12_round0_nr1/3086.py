//============================================================================
// Name        : codejama.cpp
// Author      : Tizz
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================



#include <cstdlib>
#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;


ofstream fout("a.out");
	ifstream fin("a.in");
 int number_of_inputs;



char change(char c){

    char result=NULL;

    switch(c){

        case('a'):
        {
            result='y';
            break;
        }

        case('b'):
        {
            result='h';
            break;
        }

        case('c'):
        {
            result='e';
            break;
        }

        case('d'):
        {
            result='s';
            break;
        }

        case('e'):
        {
            result='o';
            break;
        }

        case('f'):
        {
            result='c';
            break;
        }

        case('g'):
        {
            result='v';
            break;
        }

        case('h'):
        {
            result='x';
            break;
        }

        case('i'):
        {
            result='d';
            break;
        }

        case('j'):
        {
            result='u';
            break;
        }

        case('k'):
        {
            result='i';
            break;
        }

        case('l'):
        {
            result='g';
            break;
        }

        case('m'):
        {
            result='l';
            break;
        }

        case('n'):
        {
            result='b';
            break;
        }

        case('o'):
        {
            result='k';
            break;
        }

        case('p'):
        {
            result='r';
            break;
        }

        case('q'):
        {
            result='z';
            break;
        }

        case('r'):
        {
            result='t';
            break;
        }

        case('s'):
        {
            result='n';
            break;
        }

        case('t'):
        {
            result='w';
            break;
        }

        case('u'):
        {
            result='j';
            break;
        }

        case('v'):
        {
            result='p';
            break;
        }

        case('w'):
        {
            result='f';
            break;
        }

        case('x'):
        {
            result='m';
            break;
        }

        case('y'):
        {
            result='a';
            break;
        }

        case('z'):
        {
            result='q';
            break;
        }

        case(' '):
        {
            result=' ';
            break;

                   }

        default:
            break;

    }

    return result;
}

void calc(char *gona, int count){

    int num=0;
    while(num<strlen(gona))
    {
        gona[num]=change(gona[num]);
        num++;
    }

    if(count>=number_of_inputs)
        fout<<"Case #"<<count<<": "<<gona;

    else
        fout<<"Case #"<<count<<": "<<gona<<endl;

}


int main(int argc, char** argv) {

    number_of_inputs=0;

    int count=0;
    char line[120];



    fin>>number_of_inputs;
    //number_of_inputs++;
    fin.getline(line,120);

    while(count<number_of_inputs){
        fin.getline(line,120);
       //cout<<strlen(line);
        calc(line,count+1);
        count++;
    }

    return 0;
}
