#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream ifile; ifile.open("C-small-attempt0.in", ios::in);
    ofstream ofile; ofile.open("output.txt",ios::out);
    int casesnum;
    ifile>>casesnum;
    int test;
    int* list;
    for(test=1; test<=casesnum; test++)
    {
        int size; ifile>>size;
        list = new int[size];
        int i;
        for(i=0; i<size; i++) ifile>>list[i];
        long j;
        int max = -1;
        for(j=1; j<pow(2,size)-1;j++)
        {
                 int k;
                 int count = 0;
                 int result1 = 0; int result2 = 0;
                 for(k=0;k<size; k++)
                 { 
                     if( j & (1<<k))
                     {   
                         result1 = result1 ^ list[k];
                         count = count + list[k];
                     }
                     else
                         result2 = result2 ^ list[k];
                 }
                 if((result1 == result2) && (result1 != 0) && (result2 != 0) )
                     if(count>max)
                                  max=count;
        }
        ofile<<"Case #"<<test<<": ";
        if(max == -1) ofile<<"NO"<<endl;
        else ofile<<max<<endl;
        delete list;
    }
   // system("PAUSE");
    return EXIT_SUCCESS;
}
