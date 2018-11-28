#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
ofstream gaga("output.txt");

char mapa(char t)
{
    return map[((int)t-97)];
}
void convert(char G[],char C[])
{
int i;
    for( i=0;i<strlen(G);i++)
    {
        C[i]=mapa(G[i]);
    gaga<<C[i];
    }
    C[i]='\0';

    }


int main()
{
    ifstream baba("input.txt");
    int t;
    baba>>t;
    baba.ignore();
        for(int i=0;i<t;i++)
    {
    char C[150];
        char G[150];
        baba.getline(G,150);
    gaga<<"Case #"<<i+1<<": ";
                convert(G,C);
        gaga<<"\n";
    }

}
