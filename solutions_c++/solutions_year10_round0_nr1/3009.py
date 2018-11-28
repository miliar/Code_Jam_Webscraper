#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;


int main ()
{
char file[40]="A-small";
char inputfile[40], outputfile[40];  // for the name of input   and output file
double sum;
int num;
double n;
double due=2;
double k;
int c = 0;
string line;
//scanf("%s", file);         // give desired name

strcpy(inputfile, file);   // naming input file
strcpy(outputfile, file);  // naming output file

strcat(inputfile, ".in");  // adding extension for difference in input & output file
strcat(outputfile, ".out");// adding extension for difference in input & output file

FILE *fp =fopen(inputfile, "r");  //opening input file for read
FILE *ofp=fopen(outputfile, "w");  //opening output file for write


ifstream inFile;
ifstream inFile2;
inFile.open(inputfile);

inFile >> num;


while (inFile >> n) {
    inFile>> k;
    c=c+1;
    sum=pow(due,n);
    double kpiuuno=k+1;
    if ((int)k+1 % (int)sum ==0)
    fprintf(ofp,"Case #%d: ON\n",c);
    else
    fprintf(ofp,"Case #%d: OFF\n",c);
}
return 0;
}

