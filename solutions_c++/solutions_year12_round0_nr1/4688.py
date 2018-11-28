#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <set>
#include <utility>
#include <queue>
#include <stack>
#include <list>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <ctype.h>

using namespace std;

int main()
{
    int T;
    char str[200];
    char s[26];
    char input[100];
    char output[100];
    strcpy(s,"yhesocvxduiglbkrztnwjpfmaq");

    int num = 0;
    strcpy(input,"D:\\A-small-attempt6.in");
    strcpy(output,"A.out");

    FILE *fpin;
    FILE *fpout;
    fpin = fopen(input,"rb");
    fpout = fopen(output,"wb+");
    fscanf(fpin,"%d\n",&T);
    //scanf("%d\n",&T);
    while(T--)
    {

        memset(str,0,sizeof(str));

        fgets(str,150,fpin);
        //gets(str);

        int len = strlen(str);
        int i;
        num++;
        fprintf(fpout,"Case #%d: ",num);
        printf("Case #%d: ",num);
        for(i = 0; i < len-1; i++)
        {
            if(str[i]!=' ')
            {
                fprintf(fpout,"%c",s[str[i] - 'a']);
                printf("%c",s[str[i] - 'a']);
            }
            else
            {
                fprintf(fpout," ");
                printf(" ");
            }
        }
        fprintf(fpout,"\n");
        printf("\n");
    }
    fclose(fpin);
    fclose(fpout);
    return 0;
}
