#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("A-small-attempt3.in");
    ofstream out("codejam1.txt");
    char str1[110];
    char data[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t,i,no=1;
    in>>t;
    in.getline(str1,110);
    while(t--)
    {
        char str[110];
        in.getline(str,110);
        out<<"Case #"<<no<<": ";
        no++;
        for(i=0;str[i];i++)
        {
            if(str[i]==' ')
            out<<" ";
            else
            out<<data[str[i]-97];
        }
        out<<"\n";
    }
    return 0;
}
