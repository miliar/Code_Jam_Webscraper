#include<iostream>
#include<string.h>
#include<fstream>
using std::cin;
using std::cout;

char arr[26] = { 'y' , 'h' ,'e' , 's' , 'o', 'c' ,'v','x','d','u' , 'i' ,'g' ,'l','b','k','r', 'z' ,'t','n','w','j' , 'p','f','m','a', 'q' };


std::ofstream fout("Output.in");

inline void convert(char* str,int p)
{
    int i=0;
    while(str[i]!='\0')
    {
        if(str[i]==' ')
        {
            i++;
            continue;
        }
        str[i]=arr[str[i]-97];
        i++;
    }
    fout<<"Case #"<<p<<": "<<str;
}


int main(void)
{
    int n=0;
    char str[101]={'\0'};

    std::ifstream fin("A-small-attempt0.in");
    if(!fin)
    {
        std::cerr<<"\nEroror!";
        return 0;
    }

    fin>>n;
    fin.ignore(1,'\n');

    for(int i=1;i<=n;i++)
    {
        memset(str,'\0',101);
        fin.getline(str,101);
        convert(str,i);
        if(i!=n)
        fout<<"\n";
    }

    return 0;
}
