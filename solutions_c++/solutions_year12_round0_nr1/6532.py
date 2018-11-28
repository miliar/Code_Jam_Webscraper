#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;
char S[110],A[110];
//string S;
FILE* f1;
FILE* f2;
int main()
{
    int T,i,len,j;
    f1 = fopen ("out.txt", "a");
    f2 = fopen ("inp.in", "r");
    fscanf(f2,"%d\n",&T);
    //T=1;
    for(i=1;i<=T;i++)
    {
        fprintf(f1,"Case #%d: ",i);
        //scanf("%s\n",S);
        //cin>>S;
        //gets(S);
        fgets(S,101,f2);
        //fscanf(f2,"%s",S);
        //cout<<S<<len<<endl;
        //len=S.length();
        len=strlen(S);
        for(j=0;j<len;j++)
        {
            switch(S[j])
            {
                case ' ':
                    fprintf(f1," ");
                    break;
                case 'a':
                    fprintf(f1,"y");
                    break;
                case 'b':
                    fprintf(f1,"h");
                    break;
                case 'c':
                    fprintf(f1,"e");
                    break;
                case 'd':
                    fprintf(f1,"s");
                    break;
                case 'e':
                    fprintf(f1,"o");
                    break;
                case 'f':
                    fprintf(f1,"c");
                    break;
                case 'g':
                    fprintf(f1,"v");
                    break;
                case 'h':
                    fprintf(f1,"x");
                    break;
                case 'i':
                    fprintf(f1,"d");
                    break;
                case 'j':
                    fprintf(f1,"u");
                    break;
                case 'k':
                    fprintf(f1,"i");
                    break;
                case 'l':
                    fprintf(f1,"g");
                    break;
                case 'm':
                    fprintf(f1,"l");
                    break;
                case 'n':
                    fprintf(f1,"b");
                    break;
                case 'o':
                    fprintf(f1,"k");
                    break;
                case 'p':
                    fprintf(f1,"r");
                    break;
                case 'q':
                    fprintf(f1,"z");
                    break;
                case 'r':
                    fprintf(f1,"t");
                    break;
                case 's':
                    fprintf(f1,"n");
                    break;
                case 't':
                    fprintf(f1,"w");
                    break;
                case 'u':
                    fprintf(f1,"j");
                    break;
                case 'v':
                    fprintf(f1,"p");
                    break;
                case 'w':
                    fprintf(f1,"f");
                    break;
                case 'x':
                    fprintf(f1,"m");
                    break;
                case 'y':
                    fprintf(f1,"a");
                    break;
                case 'z':
                    fprintf(f1,"q");
                    break;
            }

        }
        fprintf(f1,"\n");
    }
    return 0;
}
