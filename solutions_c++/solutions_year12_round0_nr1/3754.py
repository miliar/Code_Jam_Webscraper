#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    FILE *ip = fopen("IP.txt","r");
    FILE *op = fopen("OP.txt","w");
    char remap[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t;
    char ch;
    char buffer[200];
    fscanf(ip,"%d",&t);
    fgets(buffer,200,ip);
    for(int i=1;i<=t;i++)
    {
        fgets(buffer,200,ip);

        fprintf(op,"Case #%d: ",i);
        for(int j=0; j<strlen(buffer); j++)
        {
            ch = buffer[j];
            if(ch != ' ' && ch>='a' && ch<='z')
            {
                fprintf(op,"%c", remap[ch-97]);
            }
            else if(ch == ' ')
            {
                fprintf(op," ");
            }
        }
        fprintf(op,"\n");
    }
    return 0;
}
