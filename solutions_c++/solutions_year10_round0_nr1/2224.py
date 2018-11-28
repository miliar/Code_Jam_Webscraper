#include<iostream>
#include<fstream>
#include<cstring>
#include<stdlib.h>
using namespace std;
int main()
{
    int i,n_swi,k;
    long int num,m,t;
    bool an;
    char str[100],*str1;
    str1=str;
    ifstream fin("A-large.in");
    ofstream fout("output-large.out");
    fin>>t;
    m=1;
    while(m<=t)
    {
        fin>>n_swi>>num;

        if(n_swi>num)
        fout<<"Case #"<<m<<": OFF"<<endl;
        else
        {
            str1=ltoa(num,str1,2);
            an=1;

            i=0;
            k=strlen(str);
            i=k-1;
            while(n_swi>0 && an==1)
            {
                an=an&(str[i]-48);
                i--;
                n_swi--;
            }
            if(an==1)
            fout<<"Case #"<<m<<": ON"<<endl;
            else
            fout<<"Case #"<<m<<": OFF"<<endl;

        }
        m++;
    }
}
