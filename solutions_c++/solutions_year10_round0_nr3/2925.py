#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main ()
{
char file[40]="B-small";
char inputfile[40], outputfile[40];
int sum;
int num;
int n;
int k;
int r;
int p;
int rt;
int eur;
int count;
int c = 0;
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

for (int t=1;t<=num;t++)
{   
    eur=0;
    rt=0;
    inFile>>r;
    inFile>>k;
    inFile>>n;
    int group[n];
    for(int i=0;i<n;i++)
       inFile>>group[i];
    /*for(int i=0;i<n;i++)
       cout<<group[i];
    cout<<endl;*/
    p=0;
    while(rt<r)
    {
        rt++;
        sum=0;
        count=0;
        while((sum<=k)&&(count<n))
        {
           sum=sum+group[p];
           if(sum<=k)
           {
           eur=eur+group[p];
           count++;
           if (p==(n-1))
           p=0;
           else
           p++;
           }
        }
        /*if (p==(n-1))
        p=0;
        else
        p++;*/
    }
    fprintf(ofp,"Case #%d: %d\n",t,eur);
}

return 0;
}
