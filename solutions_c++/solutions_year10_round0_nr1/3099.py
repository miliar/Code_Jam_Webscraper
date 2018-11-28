#include<iostream>
#include<fstream>
#include <stdio.h>
#include <math.h>


using namespace std;
int main()
{
    int T,k,n,i;
    ifstream input;
    ofstream output;
    input.open("A-large.in");
    output.open("plik2.txt");
    input>>T;
    for(i=0;i<T;i++)
    {
        input>>n;
        input>>k;
        if(k%(int)pow(2,n)==(int)pow(2,n)-1) output<<"Case #"<<i+1<<": ON"<<endl;
        else output<<"Case #"<<i+1<<": OFF"<<endl;
                   
    }
    system("pause");
    return 0;
}
