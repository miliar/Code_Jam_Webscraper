#include <fstream>
#include <iostream>
#include <conio.h>
int strlen(char s[])                          
{
int i = 0 ;                                      
while (s[i++] != '\0' ) ;
return i-1 ;                                    
}
int main()
{
    std::ifstream f("A-small-attempt1.in");
    std::ofstream g("iesire.txt");
    char alfabet[2][27]={"abcdefghijklmnopqrstuvwxyz","ynficwlbkuomxsevzpdrjgthaq"};
    char mapping[30][101];
    int T;
    f>>T;
    f.getline(mapping[0],700);
    for(int i=0;i<T;i++)
    f.getline(mapping[i],700);
    
    for(int i=0;i<T;i++){
    int l_ph=strlen(mapping[i]);
    
    for(int j=0;j<l_ph;j++)
            for(int i_a=0;i_a<26;i_a++)
                    if(mapping[i][j]==alfabet[1][i_a]){mapping[i][j]=alfabet[0][i_a];break;}
    }
    for(int i=0;i<T;i++){
    g<<"Case #"<<i+1<<": ";
    g<<mapping[i]<<std::endl;}
     return 0;
     }
