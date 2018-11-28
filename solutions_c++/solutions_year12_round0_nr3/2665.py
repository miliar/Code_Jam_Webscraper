#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <map>
 
using namespace std;
 
string inttostr(int n)
{
        char buffer[20];
        sprintf(buffer, "%i", n);
        return string(buffer);
}
 
int strtoint(string s)
{
        int n=0;
        int i=0;
        int tam=s.length();
        for(int i=0;i<tam;i++)
        {
                n+=(s[i]-'0');
                n*=10;
        }
        return n/10;
}
 
int main()
{
        int n;
        int caso = 1;
        scanf("%i", &n);
        while(n>0)
        {
                int a,b;
                scanf("%i %i", &a, &b);
                map<string, int> mapa;
                int total=0;
                for(int i=a;i<b;i++)
                {
                        string si = inttostr(i);
                        int tam = si.length();
                        for(int j=1;j<tam;j++)
                        {
                                string novo = si.substr(j, tam-j)+si.substr(0, j);
                                int novon = strtoint(novo);
                                if(novo.compare(si)!=0 && novon>=a && novon<=b && (mapa[novo+"-"+si]==0 && mapa[si+"-"+novo]==0))
                                {
                                        total++;
                                        mapa[novo+"-"+si]=1;
                                        mapa[si+"-"+novo]=1;
                                }
                        }
                }
                cout<<"Case #"<<caso<<": "<<total<<endl;
                n--;
                caso++;
        }
        return 0;
}