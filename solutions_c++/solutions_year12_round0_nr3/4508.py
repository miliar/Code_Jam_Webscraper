#include <iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
using namespace std;

int main()
{
    char temp[500],n[100],tmp;
    int t,i,a,b,r,j,count,k,number,o,len,m;
    ifstream inp_file("input",ios::in);
    inp_file.getline(temp,500);
    t=atoi(temp);
    for(i=0;i<t;i++)
    {
        inp_file>>a;
        inp_file>>b;
        count=0;
        for(j=a;j<=b;j++)
        {
            k=j;
            itoa(k,n,10);
            len=strlen(n);
            for(o=0;o<len;o++)
            {
                tmp=n[0];
                for(m=0;m<len-1;m++)
                n[m]=n[m+1];
                n[m]=tmp;
                number=atoi(n);
                if(number>k&&number<=b)
                count++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    return 0;
}
