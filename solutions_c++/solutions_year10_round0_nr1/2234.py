#include<iostream>
#include<fstream>
#include<cstring>
#include<stdlib.h>
using namespace std;
int main()
{
    int i,sw,len;
    long int num,m,t;
    bool flag;
    char str[100],*str1;
    str1=str;
    ifstream fin("A-large.in");
    ofstream fout("output_a_large.out");
    fin>>t;
    m=1;
    while(m<=t)
    {
        fin>>sw>>num;

        if(sw>num)
        fout<<"Case #"<<m<<": OFF"<<endl;
        else
        {
            str1=ltoa(num,str1,2);
            flag=1;

            i=0;
            len=strlen(str);
            i=len-1;
            while(sw>0 && flag==1)
            {
                flag=flag&(str[i]-48);
                i--;
                sw--;
            }
            if(flag==1)
            fout<<"Case #"<<m<<": ON"<<endl;
            else
            fout<<"Case #"<<m<<": OFF"<<endl;

        }
        m++;
    }
}
