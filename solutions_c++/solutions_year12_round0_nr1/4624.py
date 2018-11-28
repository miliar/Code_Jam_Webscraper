#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    ifstream in("A-small-attempt5.in");
    //ofstream out("A-small-attempt3.in");
    freopen("oo","w",stdout);
    string S="yhesocvxduiglbkrztnwjpfmaq";
    int T=0;
    in>>T;
    int k=1;
    string G="";
    getline(in,G);
    while(T--)
    {
        getline(in,G);
        G+='\n';
        //out<<"Case #"<<k<<"： ";
        printf("Case #%d: ",k);
        k++;
        int i=0;
        while(G[i]!='\n')
        {
            if(G[i]>'z'||G[i]<'a')
                //out<<G[i];
                printf("%c",G[i]);
            else
            //out<<S[G[i]-'a'];
            printf("%c",S[G[i]-'a']);
            i++;
        }
      printf("\n");
    }

in.close();
fclose(stdout);
//out.close();
    return 0;
}
